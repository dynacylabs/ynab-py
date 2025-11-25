"""
Tests for ynab_py.endpoints module.

Tests the Endpoints class that constructs API endpoint URLs.
"""

import pytest
from unittest.mock import Mock, patch
import responses

from ynab_py.endpoints import Endpoints


@pytest.mark.unit
class TestEndpointsInit:
    """Test Endpoints initialization."""
    
    def test_init(self, ynab_client):
        """Test Endpoints initialization."""
        endpoints = Endpoints(ynab_py=ynab_client)
        assert endpoints.ynab_py == ynab_client
        assert endpoints.http_utils is not None


@pytest.mark.unit
class TestEndpointsUserRequests:
    """Test user endpoint requests."""
    
    @responses.activate
    def test_request_get_user(self, ynab_client):
        """Test request_get_user endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/user",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_user()
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsBudgetRequests:
    """Test budget endpoint requests."""
    
    @responses.activate
    def test_request_get_budgets(self, ynab_client):
        """Test request_get_budgets endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_budgets()
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_budgets_with_accounts(self, ynab_client):
        """Test request_get_budgets with include_accounts."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets?include_accounts=true",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_budgets(include_accounts=True)
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_budget(self, ynab_client):
        """Test request_get_budget endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_budget(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_budget_with_server_knowledge(self, ynab_client):
        """Test request_get_budget with server knowledge."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123?last_knowledge_of_server=100",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_budget(budget_id="budget-123", last_knowledge_of_server=100)
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsAccountRequests:
    """Test account endpoint requests."""
    
    @responses.activate
    def test_request_get_accounts(self, ynab_client):
        """Test request_get_accounts endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/accounts",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_accounts(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_create_account(self, ynab_client):
        """Test request_create_account endpoint."""
        responses.add(
            responses.POST,
            "https://api.ynab.com/v1/budgets/budget-123/accounts",
            json={"data": {}},
            status=201
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        request_body = {"account": {"name": "Test"}}
        response = endpoints.request_create_account(budget_id="budget-123", request_body=request_body)
        
        assert response.status_code == 201
    
    @responses.activate
    def test_request_get_account(self, ynab_client):
        """Test request_get_account endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/accounts/account-456",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_account(budget_id="budget-123", account_id="account-456")
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsTransactionRequests:
    """Test transaction endpoint requests."""
    
    @responses.activate
    def test_request_get_transactions(self, ynab_client):
        """Test request_get_transactions endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/transactions",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_transactions(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_transactions_with_filters(self, ynab_client):
        """Test request_get_transactions with filters."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/transactions?since_date=2025-01-01&type=unapproved",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_transactions(
            budget_id="budget-123",
            since_date="2025-01-01",
            type="unapproved"
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_create_transactions(self, ynab_client):
        """Test request_create_transactions endpoint."""
        responses.add(
            responses.POST,
            "https://api.ynab.com/v1/budgets/budget-123/transactions",
            json={"data": {}},
            status=201
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        request_body = {"transaction": {}}
        response = endpoints.request_create_transactions(budget_id="budget-123", request_body=request_body)
        
        assert response.status_code == 201
    
    @responses.activate
    def test_request_update_transaction(self, ynab_client):
        """Test request_update_transaction endpoint."""
        responses.add(
            responses.PUT,
            "https://api.ynab.com/v1/budgets/budget-123/transactions/txn-456",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        request_body = {"transaction": {}}
        response = endpoints.request_update_transaction(
            budget_id="budget-123",
            transaction_id="txn-456",
            request_body=request_body
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_delete_transaction(self, ynab_client):
        """Test request_delete_transaction endpoint."""
        responses.add(
            responses.DELETE,
            "https://api.ynab.com/v1/budgets/budget-123/transactions/txn-456",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_delete_transaction(budget_id="budget-123", transaction_id="txn-456")
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsCategoryRequests:
    """Test category endpoint requests."""
    
    @responses.activate
    def test_request_get_categories(self, ynab_client):
        """Test request_get_categories endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/categories",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_categories(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_category(self, ynab_client):
        """Test request_get_category endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/categories/cat-456",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_category(budget_id="budget-123", category_id="cat-456")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_update_category(self, ynab_client):
        """Test request_update_category endpoint."""
        responses.add(
            responses.PATCH,
            "https://api.ynab.com/v1/budgets/budget-123/categories/cat-456",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        request_body = {"category": {}}
        response = endpoints.request_update_category(
            budget_id="budget-123",
            category_id="cat-456",
            request_body=request_body
        )
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsPayeeRequests:
    """Test payee endpoint requests."""
    
    @responses.activate
    def test_request_get_payees(self, ynab_client):
        """Test request_get_payees endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payees",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_payees(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_payee(self, ynab_client):
        """Test request_get_payee endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payees/payee-456",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_payee(budget_id="budget-123", payee_id="payee-456")
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsMonthRequests:
    """Test month endpoint requests."""
    
    @responses.activate
    def test_request_get_months(self, ynab_client):
        """Test request_get_months endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/months",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_months(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_month(self, ynab_client):
        """Test request_get_month endpoint."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/months/current",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_month(budget_id="budget-123", month_id="current")
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsServerKnowledge:
    """Test endpoints with server knowledge parameters."""
    
    @responses.activate
    def test_request_get_accounts_with_server_knowledge(self, ynab_client):
        """Test request_get_accounts with server knowledge."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/accounts?last_knowledge_of_server=50",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_accounts(
            budget_id="budget-123",
            last_knowledge_of_server=50
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_categories_with_server_knowledge(self, ynab_client):
        """Test request_get_categories with server knowledge."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/categories?last_knowledge_of_server=75",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_categories(
            budget_id="budget-123",
            last_knowledge_of_server=75
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_transactions_with_since_date(self, ynab_client):
        """Test request_get_transactions with since_date."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/transactions?since_date=2023-01-01",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_transactions(
            budget_id="budget-123",
            since_date="2023-01-01"
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_transactions_with_type_filter(self, ynab_client):
        """Test request_get_transactions with type filter."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/transactions?type=uncategorized",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_transactions(
            budget_id="budget-123",
            type="uncategorized"
        )
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsPayeeLocationRequests:
    """Test payee location endpoint requests."""
    
    @responses.activate
    def test_request_get_all_payee_locations(self, ynab_client):
        """Test request_get_all_payee_locations."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payee_locations",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_all_payee_locations(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_payee_location(self, ynab_client):
        """Test request_get_payee_location."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payee_locations/loc-123",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_payee_location(
            budget_id="budget-123",
            payee_location_id="loc-123"
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_payee_locations_for_payee(self, ynab_client):
        """Test request_get_payee_locations with payee_id."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/payees/payee-123/payee_locations",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_payee_locations(
            budget_id="budget-123",
            payee_id="payee-123"
        )
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsScheduledTransactionRequests:
    """Test scheduled transaction endpoint requests."""
    
    @responses.activate
    def test_request_get_scheduled_transactions(self, ynab_client):
        """Test request_get_scheduled_transactions."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/scheduled_transactions",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_scheduled_transactions(budget_id="budget-123")
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_scheduled_transaction(self, ynab_client):
        """Test request_get_scheduled_transaction."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/scheduled_transactions/sched-123",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_scheduled_transaction(
            budget_id="budget-123",
            scheduled_transaction_id="sched-123"
        )
        
        assert response.status_code == 200


@pytest.mark.unit
class TestEndpointsUpdateRequests:
    """Test update endpoint requests."""
    
    @responses.activate
    def test_request_update_payee(self, ynab_client):
        """Test request_update_payee."""
        responses.add(
            responses.PATCH,
            "https://api.ynab.com/v1/budgets/budget-123/payees/payee-123",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_update_payee(
            budget_id="budget-123",
            payee_id="payee-123",
            request_body={"payee": {"name": "New Name"}}
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_update_transactions(self, ynab_client):
        """Test request_update_transactions."""
        responses.add(
            responses.PATCH,
            "https://api.ynab.com/v1/budgets/budget-123/transactions",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_update_transactions(
            budget_id="budget-123",
            request_body={"transactions": [{"id": "t1", "amount": 5000}]}
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_update_transaction(self, ynab_client):
        """Test request_update_transaction."""
        responses.add(
            responses.PUT,
            "https://api.ynab.com/v1/budgets/budget-123/transactions/txn-123",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_update_transaction(
            budget_id="budget-123",
            transaction_id="txn-123",
            request_body={"transaction": {"amount": 5000}}
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_get_category_for_month(self, ynab_client):
        """Test request_get_category_for_month."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/budget-123/months/2023-01/categories/cat-123",
            json={"data": {}},
            status=200
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_get_category_for_month(
            budget_id="budget-123",
            month="2023-01",
            category_id="cat-123"
        )
        
        assert response.status_code == 200
    
    @responses.activate
    def test_request_import_transactions(self, ynab_client):
        """Test request_import_transactions."""
        responses.add(
            responses.POST,
            "https://api.ynab.com/v1/budgets/budget-123/transactions/import",
            json={"data": {}},
            status=201
        )
        
        endpoints = Endpoints(ynab_py=ynab_client)
        response = endpoints.request_import_transactions(budget_id="budget-123")
        
        assert response.status_code == 201




