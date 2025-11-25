"""
Tests for ynab_py.api module.

Tests the Api class methods that interact with the YNAB API.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import responses

from ynab_py.api import Api
from ynab_py import schemas
from ynab_py.exceptions import YnabError


@pytest.mark.unit
class TestApiInit:
    """Test Api initialization."""
    
    def test_init(self, ynab_client):
        """Test Api initialization."""
        api = Api(ynab_py=ynab_client)
        assert api.ynab_py == ynab_client
        assert api.endpoints is not None


@pytest.mark.unit
class TestApiUserMethods:
    """Test user-related API methods."""
    
    @responses.activate
    def test_get_user_success(self, ynab_client, sample_user_json):
        """Test get_user with successful response."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/user",
            json=sample_user_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        user = api.get_user()
        
        assert isinstance(user, schemas.User)
        assert user.id == "user-123"
    
    @responses.activate
    def test_get_user_error(self, ynab_client):
        """Test get_user with error response."""
        error_json = {"error": {"id": "err-1", "name": "error", "detail": "Error"}}
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/user",
            json=error_json,
            status=400
        )
        
        api = Api(ynab_py=ynab_client)
        with pytest.raises(Exception):
            api.get_user()


@pytest.mark.unit
class TestApiBudgetMethods:
    """Test budget-related API methods."""
    
    @responses.activate
    def test_get_budgets_success(self, ynab_client, sample_budgets_response):
        """Test get_budgets with successful response."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets",
            json=sample_budgets_response,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        budgets = api.get_budgets()
        
        assert len(budgets) == 1
        assert "budget-123" in budgets
        assert isinstance(budgets["budget-123"], schemas.Budget)
    
    @responses.activate
    def test_get_budgets_with_accounts(self, ynab_client, sample_budgets_response):
        """Test get_budgets with include_accounts=True."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets?include_accounts=true",
            json=sample_budgets_response,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        budgets = api.get_budgets(include_accounts=True)
        
        assert len(budgets) == 1
    
    @responses.activate
    def test_get_budget_success(self, ynab_client, sample_budget_json):
        """Test get_budget with successful response."""
        response_json = {
            "data": {
                "budget": sample_budget_json,
                "server_knowledge": 100
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        budget = api.get_budget(budget_id="budget-123")
        
        assert isinstance(budget, schemas.Budget)
        assert budget.id == "budget-123"
        assert ynab_client._server_knowledges["get_budget"] == 100
    
    @responses.activate
    def test_get_budget_settings_success(self, ynab_client):
        """Test get_budget_settings with successful response."""
        settings_json = {
            "data": {
                "settings": {
                    "date_format": {"format": "DD/MM/YYYY"},
                    "currency_format": {"iso_code": "USD"}
                }
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/settings",
            json=settings_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        settings = api.get_budget_settings(budget_id="budget-123")
        
        assert isinstance(settings, schemas.BudgetSettings)


@pytest.mark.unit
class TestApiAccountMethods:
    """Test account-related API methods."""
    
    @responses.activate
    def test_get_accounts_success(self, ynab_client, sample_account_json):
        """Test get_accounts with successful response."""
        response_json = {
            "data": {
                "accounts": [sample_account_json],
                "server_knowledge": 50
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/accounts",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        accounts = api.get_accounts(budget_id="budget-123")
        
        assert len(accounts) == 1
        assert "account-123" in accounts
        assert ynab_client._server_knowledges["get_accounts"] == 50
    
    @responses.activate
    def test_get_account_success(self, ynab_client, sample_account_json):
        """Test get_account with successful response."""
        response_json = {
            "data": {
                "account": sample_account_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/accounts/account-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        account = api.get_account(budget_id="budget-123", account_id="account-123")
        
        assert isinstance(account, schemas.Account)


@pytest.mark.unit
class TestApiTransactionMethods:
    """Test transaction-related API methods."""
    
    @responses.activate
    def test_get_transactions_success(self, ynab_client, sample_transaction_json):
        """Test get_transactions with successful response."""
        response_json = {
            "data": {
                "transactions": [sample_transaction_json],
                "server_knowledge": 200
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/transactions",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        transactions = api.get_transactions(budget_id="budget-123")
        
        assert len(transactions) == 1
        assert "txn-123" in transactions
        assert ynab_client._server_knowledges["get_transactions"] == 200
    
    @responses.activate
    def test_get_transaction_success(self, ynab_client, sample_transaction_json):
        """Test get_transaction with successful response."""
        response_json = {
            "data": {
                "transaction": sample_transaction_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/transactions/txn-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        transaction = api.get_transaction(budget_id="budget-123", transaction_id="txn-123")
        
        assert isinstance(transaction, schemas.Transaction)
    
    @responses.activate
    def test_delete_transaction_success(self, ynab_client, sample_transaction_json):
        """Test delete_transaction with successful response."""
        response_json = {
            "data": {
                "transaction": sample_transaction_json
            }
        }
        responses.add(
            responses.DELETE,
            "https://api.ynab.com/v1/budgets/budget-123/transactions/txn-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        result = api.delete_transaction(budget_id="budget-123", transaction_id="txn-123")
        
        assert isinstance(result, schemas.Transaction)


@pytest.mark.unit
class TestApiCategoryMethods:
    """Test category-related API methods."""
    
    @responses.activate
    def test_get_categories_success(self, ynab_client):
        """Test get_categories with successful response."""
        response_json = {
            "data": {
                "category_groups": [
                    {
                        "id": "catgroup-123",
                        "name": "Monthly Bills",
                        "hidden": False,
                        "deleted": False,
                        "categories": []
                    }
                ],
                "server_knowledge": 75
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/categories",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        category_groups = api.get_categories(budget_id="budget-123")
        
        assert len(category_groups) == 1
        assert "catgroup-123" in category_groups
        assert ynab_client._server_knowledges["get_categories"] == 75
    
    @responses.activate
    def test_get_category_success(self, ynab_client, sample_category_json):
        """Test get_category with successful response."""
        response_json = {
            "data": {
                "category": sample_category_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/categories/cat-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        category = api.get_category(budget_id="budget-123", category_id="cat-123")
        
        assert isinstance(category, schemas.Category)


@pytest.mark.unit
class TestApiPayeeMethods:
    """Test payee-related API methods."""
    
    @responses.activate
    def test_get_payees_success(self, ynab_client, sample_payee_json):
        """Test get_payees with successful response."""
        response_json = {
            "data": {
                "payees": [sample_payee_json]
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payees",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        payees = api.get_payees(budget_id="budget-123")
        
        assert len(payees) == 1
        assert "payee-123" in payees
    
    @responses.activate
    def test_get_payee_success(self, ynab_client, sample_payee_json):
        """Test get_payee with successful response."""
        response_json = {
            "data": {
                "payee": sample_payee_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payees/payee-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        payee = api.get_payee(budget_id="budget-123", payee_id="payee-123")
        
        assert isinstance(payee, schemas.Payee)


@pytest.mark.unit
class TestApiMonthMethods:
    """Test month-related API methods."""
    
    @responses.activate
    def test_get_months_success(self, ynab_client, sample_month_json):
        """Test get_months with successful response."""
        response_json = {
            "data": {
                "months": [sample_month_json],
                "server_knowledge": 60
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/months",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        months = api.get_months(budget_id="budget-123")
        
        assert len(months) == 1
        assert ynab_client._server_knowledges["get_months"] == 60
    
    @responses.activate
    def test_get_month_success(self, ynab_client, sample_month_json):
        """Test get_month with successful response."""
        response_json = {
            "data": {
                "month": sample_month_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/months/current",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        month = api.get_month(budget_id="budget-123", month_id="current")
        
        assert isinstance(month, schemas.Month)


@pytest.mark.unit
class TestApiAccountCreation:
    """Test account creation."""
    
    @responses.activate
    def test_create_account_returns_account(self, ynab_client, sample_account_json):
        """Test that create_account returns an Account object."""
        from ynab_py.enums import AccountType
        from unittest.mock import Mock
        
        response_json = {
            "data": {
                "account": sample_account_json
            }
        }
        responses.add(
            responses.POST,
            "https://api.ynab.com/v1/budgets/budget-123/accounts",
            json=response_json,
            status=201
        )
        
        # Create a mock budget with accounts dict
        mock_budget = Mock()
        mock_budget.id = "budget-123"
        mock_budget.accounts = {}
        
        api = Api(ynab_py=ynab_client)
        account = api.create_account(
            budget=mock_budget,
            account_name="Test Account",
            account_type=AccountType.CHECKING,
            account_balance=100000
        )
        
        assert isinstance(account, schemas.Account)
        assert account.id == "account-123"
        # Verify account was added to budget
        assert "account-123" in mock_budget.accounts



@pytest.mark.unit
class TestApiTransactionOperations:
    """Test transaction create/update operations."""
    
    @responses.activate
    def test_get_account_transactions(self, ynab_client, sample_transaction_json):
        """Test get_account_transactions."""
        response_json = {
            "data": {
                "transactions": [sample_transaction_json]
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/accounts/acc-123/transactions",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        transactions = api.get_account_transactions(
            budget_id="budget-123",
            account_id="acc-123"
        )
        
        assert isinstance(transactions, dict)
        assert len(transactions) == 1
    
    @responses.activate
    def test_get_category_transactions(self, ynab_client, sample_transaction_json):
        """Test get_category_transactions."""
        response_json = {
            "data": {
                "transactions": [sample_transaction_json]
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/categories/cat-123/transactions",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        transactions = api.get_category_transactions(
            budget_id="budget-123",
            category_id="cat-123"
        )
        
        assert isinstance(transactions, dict)
    
    @responses.activate
    def test_get_payee_transactions(self, ynab_client, sample_transaction_json):
        """Test get_payee_transactions."""
        response_json = {
            "data": {
                "transactions": [sample_transaction_json]
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payees/payee-123/transactions",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        transactions = api.get_payee_transactions(
            budget_id="budget-123",
            payee_id="payee-123"
        )
        
        assert isinstance(transactions, dict)
    
    @responses.activate
    def test_import_transactions(self, ynab_client):
        """Test import_transactions."""
        response_json = {
            "data": {
                "transaction_ids": ["t1", "t2", "t3"]
            }
        }
        responses.add(
            responses.POST,
            "https://api.ynab.com/v1/budgets/budget-123/transactions/import",
            json=response_json,
            status=201
        )
        
        api = Api(ynab_py=ynab_client)
        result = api.import_transactions(budget_id="budget-123")
        
        assert result == ["t1", "t2", "t3"]


@pytest.mark.unit
class TestApiPayeeOperations:
    """Test payee operations."""
    
    @responses.activate
    def test_get_payee_locations(self, ynab_client):
        """Test get_payee_locations."""
        location_json = {
            "id": "loc-123",
            "payee_id": "payee-123",
            "latitude": "40.7128",
            "longitude": "-74.0060",
            "deleted": False
        }
        response_json = {
            "data": {
                "payee_locations": [location_json]
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payees/payee-123/payee_locations",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        locations = api.get_payee_locations(
            budget_id="budget-123",
            payee_id="payee-123"
        )
        
        assert isinstance(locations, dict)
        assert len(locations) == 1
    
    @responses.activate
    def test_get_payee_location(self, ynab_client):
        """Test get_payee_location."""
        location_json = {
            "id": "loc-123",
            "payee_id": "payee-123",
            "latitude": "40.7128",
            "longitude": "-74.0060",
            "deleted": False
        }
        response_json = {
            "data": {
                "payee_location": location_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payee_locations/loc-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        location = api.get_payee_location(
            budget_id="budget-123",
            payee_location_id="loc-123"
        )
        
        assert isinstance(location, schemas.PayeeLocation)
        assert location.id == "loc-123"


@pytest.mark.unit
class TestApiScheduledTransactions:
    """Test scheduled transaction operations."""
    
    @responses.activate
    def test_get_scheduled_transactions(self, ynab_client):
        """Test get_scheduled_transactions."""
        scheduled_json = {
            "id": "sched-123",
            "date_first": "2023-01-01",
            "date_next": "2023-02-01",
            "frequency": "monthly",
            "amount": -100000,
            "account_id": "account-123",
            "deleted": False
        }
        response_json = {
            "data": {
                "scheduled_transactions": [scheduled_json]
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/scheduled_transactions",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        scheduled = api.get_scheduled_transactions(budget_id="budget-123")
        
        assert isinstance(scheduled, dict)
        assert len(scheduled) == 1
    
    @responses.activate
    def test_get_scheduled_transaction(self, ynab_client):
        """Test get_scheduled_transaction."""
        scheduled_json = {
            "id": "sched-123",
            "date_first": "2023-01-01",
            "date_next": "2023-02-01",
            "frequency": "monthly",
            "amount": -100000,
            "account_id": "account-123",
            "deleted": False
        }
        response_json = {
            "data": {
                "scheduled_transaction": scheduled_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/scheduled_transactions/sched-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        scheduled = api.get_scheduled_transaction(
            budget_id="budget-123",
            scheduled_transaction_id="sched-123"
        )
        
        assert isinstance(scheduled, schemas.ScheduledTransaction)
        assert scheduled.id == "sched-123"


@pytest.mark.unit
class TestApiCategoryOperations:
    """Test category operations."""
    
    @responses.activate
    def test_get_category_for_month(self, ynab_client, sample_category_json):
        """Test get_category_for_month."""
        response_json = {
            "data": {
                "category": sample_category_json
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/months/2023-01/categories/cat-123",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        category = api.get_category_for_month(
            budget_id="budget-123",
            month="2023-01",
            category_id="cat-123"
        )
        
        assert isinstance(category, schemas.Category)
        assert category.id == "cat-123"


@pytest.mark.unit
class TestApiMonthTransactions:
    """Test month-specific transaction operations."""
    
    @responses.activate
    def test_get_month_transactions_with_string(self, ynab_client, sample_transaction_json):
        """Test get_month_transactions with month string."""
        response_json = {
            "data": {
                "transactions": [sample_transaction_json]
            }
        }
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/months/2023-01/transactions",
            json=response_json,
            status=200
        )
        
        api = Api(ynab_py=ynab_client)
        transactions = api.get_month_transactions(
            budget_id="budget-123",
            month_id="2023-01"
        )
        
        assert isinstance(transactions, dict)



