"""
Tests for ynab_py.schemas module.

Tests schema classes for data models.
"""

import pytest
from datetime import datetime, date
from dateutil.parser import isoparse

from ynab_py import schemas


@pytest.mark.unit
class TestUser:
    """Test User schema."""
    
    def test_init(self, ynab_client):
        """Test User initialization."""
        user_json = {"id": "user-123"}
        user = schemas.User(ynab_py=ynab_client, _json=user_json)
        
        assert user.id == "user-123"
        assert user.ynab_py == ynab_client
    
    def test_to_dict(self, ynab_client):
        """Test User to_dict method."""
        user_json = {"id": "user-123"}
        user = schemas.User(ynab_py=ynab_client, _json=user_json)
        
        result = user.to_dict()
        assert result == {"id": "user-123"}
    
    def test_to_json(self, ynab_client):
        """Test User to_json method."""
        user_json = {"id": "user-123"}
        user = schemas.User(ynab_py=ynab_client, _json=user_json)
        
        result = user.to_json()
        assert "user-123" in result


@pytest.mark.unit
class TestError:
    """Test Error schema."""
    
    def test_init(self, ynab_client):
        """Test Error initialization."""
        error_json = {
            "id": "err-123",
            "name": "validation_error",
            "detail": "Invalid input"
        }
        error = schemas.Error(ynab_py=ynab_client, _json=error_json)
        
        assert error.id == "err-123"
        assert error.name == "validation_error"
        assert error.detail == "Invalid input"
    
    def test_str(self, ynab_client):
        """Test Error __str__ method."""
        error_json = {
            "id": "err-123",
            "name": "validation_error",
            "detail": "Invalid input"
        }
        error = schemas.Error(ynab_py=ynab_client, _json=error_json)
        
        result = str(error)
        assert "err-123" in result
        assert "validation_error" in result
        assert "Invalid input" in result


@pytest.mark.unit
class TestBudget:
    """Test Budget schema."""
    
    def test_init(self, ynab_client, sample_budget_json):
        """Test Budget initialization."""
        budget = schemas.Budget(ynab_py=ynab_client, _json=sample_budget_json)
        
        assert budget.id == "budget-123"
        assert budget.name == "Test Budget"
        assert isinstance(budget.last_modified_on, datetime)
        assert isinstance(budget.first_month, date)
        assert isinstance(budget.last_month, date)
    
    def test_date_format(self, ynab_client, sample_budget_json):
        """Test Budget date_format attribute."""
        budget = schemas.Budget(ynab_py=ynab_client, _json=sample_budget_json)
        
        assert isinstance(budget.date_format, schemas.DateFormat)
    
    def test_currency_format(self, ynab_client, sample_budget_json):
        """Test Budget currency_format attribute."""
        budget = schemas.Budget(ynab_py=ynab_client, _json=sample_budget_json)
        
        assert isinstance(budget.currency_format, schemas.CurrencyFormat)


@pytest.mark.unit
class TestAccount:
    """Test Account schema."""
    
    def test_init(self, ynab_client, sample_account_json):
        """Test Account initialization."""
        account = schemas.Account(ynab_py=ynab_client, _json=sample_account_json)
        
        assert account.id == "account-123"
        assert account.name == "Checking Account"
        assert account.type.value == "checking"
        assert account.balance == 150000
        assert account.closed == False
    
    def test_attributes(self, ynab_client, sample_account_json):
        """Test Account attributes."""
        account = schemas.Account(ynab_py=ynab_client, _json=sample_account_json)
        
        assert account.id == "account-123"
        assert account.name == "Checking Account"
        assert account.on_budget == True
        assert account.note == "Main checking account"


@pytest.mark.unit
class TestTransaction:
    """Test Transaction schema."""
    
    def test_init(self, ynab_client, sample_transaction_json):
        """Test Transaction initialization."""
        transaction = schemas.Transaction(ynab_py=ynab_client, _json=sample_transaction_json)
        
        assert transaction.id == "txn-123"
        assert transaction.amount == -50000
        assert transaction.memo == "Grocery shopping"
        assert transaction.cleared.value == "cleared"
        assert transaction.approved == True
    
    def test_date_parsing(self, ynab_client, sample_transaction_json):
        """Test Transaction date parsing."""
        transaction = schemas.Transaction(ynab_py=ynab_client, _json=sample_transaction_json)
        
        assert isinstance(transaction.date, date)
        assert transaction.date == date(2025, 11, 24)
    
    def test_to_dict(self, ynab_client, sample_transaction_json):
        """Test Transaction to_dict method."""
        transaction = schemas.Transaction(ynab_py=ynab_client, _json=sample_transaction_json)
        
        result = transaction.to_dict()
        assert result["id"] == "txn-123"
        assert result["amount"] == -50000


@pytest.mark.unit
class TestCategory:
    """Test Category schema."""
    
    def test_init(self, ynab_client, sample_category_json):
        """Test Category initialization."""
        category = schemas.Category(ynab_py=ynab_client, _json=sample_category_json)
        
        assert category.id == "cat-123"
        assert category.name == "Groceries"
        assert category.budgeted == 500000
        assert category.activity == -350000
        assert category.balance == 150000
    
    def test_attributes(self, ynab_client, sample_category_json):
        """Test Category attributes."""
        category = schemas.Category(ynab_py=ynab_client, _json=sample_category_json)
        
        assert category.id == "cat-123"
        assert category.name == "Groceries"
        assert category.hidden == False
        assert category.deleted == False


@pytest.mark.unit
class TestPayee:
    """Test Payee schema."""
    
    def test_init(self, ynab_client, sample_payee_json):
        """Test Payee initialization."""
        payee = schemas.Payee(ynab_py=ynab_client, _json=sample_payee_json)
        
        assert payee.id == "payee-123"
        assert payee.name == "Grocery Store"
        assert payee.deleted == False
    
    def test_attributes(self, ynab_client, sample_payee_json):
        """Test Payee attributes."""
        payee = schemas.Payee(ynab_py=ynab_client, _json=sample_payee_json)
        
        assert payee.id == "payee-123"
        assert payee.name == "Grocery Store"
        assert payee.transfer_account_id is None
        assert payee.deleted == False


@pytest.mark.unit
class TestMonth:
    """Test Month schema."""
    
    def test_init(self, ynab_client, sample_month_json):
        """Test Month initialization."""
        month = schemas.Month(ynab_py=ynab_client, _json=sample_month_json)
        
        assert month.income == 500000
        assert month.budgeted == 450000
        assert month.activity == -400000
        assert month.to_be_budgeted == 50000
    
    def test_attributes(self, ynab_client, sample_month_json):
        """Test Month attributes."""
        month = schemas.Month(ynab_py=ynab_client, _json=sample_month_json)
        
        assert month.income == 500000
        assert month.budgeted == 450000
        assert month.note == "November budget"
        assert month.deleted == False


@pytest.mark.unit
class TestDateFormat:
    """Test DateFormat schema."""
    
    def test_init(self, ynab_client):
        """Test DateFormat initialization."""
        date_format_json = {"format": "DD/MM/YYYY"}
        date_format = schemas.DateFormat(ynab_py=ynab_client, _json=date_format_json)
        
        assert date_format.format == "DD/MM/YYYY"


@pytest.mark.unit
class TestCurrencyFormat:
    """Test CurrencyFormat schema."""
    
    def test_init(self, ynab_client):
        """Test CurrencyFormat initialization."""
        currency_json = {
            "iso_code": "USD",
            "example_format": "$1,234.56",
            "decimal_digits": 2,
            "decimal_separator": ".",
            "symbol_first": True,
            "group_separator": ",",
            "currency_symbol": "$",
            "display_symbol": True
        }
        currency = schemas.CurrencyFormat(ynab_py=ynab_client, _json=currency_json)
        
        assert currency.iso_code == "USD"
        assert currency.decimal_digits == 2
        assert currency.currency_symbol == "$"


@pytest.mark.unit
class TestBudgetSettings:
    """Test BudgetSettings schema."""
    
    def test_init(self, ynab_client):
        """Test BudgetSettings initialization."""
        settings_json = {
            "date_format": {"format": "DD/MM/YYYY"},
            "currency_format": {"iso_code": "USD"}
        }
        settings = schemas.BudgetSettings(ynab_py=ynab_client, _json=settings_json)
        
        assert isinstance(settings.date_format, schemas.DateFormat)
        assert isinstance(settings.currency_format, schemas.CurrencyFormat)


@pytest.mark.unit
class TestCategoryGroup:
    """Test CategoryGroup schema."""
    
    def test_init(self, ynab_client):
        """Test CategoryGroup initialization."""
        catgroup_json = {
            "id": "catgroup-123",
            "name": "Monthly Bills",
            "hidden": False,
            "deleted": False,
            "categories": []
        }
        catgroup = schemas.CategoryGroup(ynab_py=ynab_client, _json=catgroup_json)
        
        assert catgroup.id == "catgroup-123"
        assert catgroup.name == "Monthly Bills"
        assert catgroup.hidden == False


@pytest.mark.unit
class TestPayeeLocation:
    """Test PayeeLocation schema."""
    
    def test_init(self, ynab_client):
        """Test PayeeLocation initialization."""
        location_json = {
            "id": "loc-123",
            "payee_id": "payee-123",
            "latitude": "37.7749",
            "longitude": "-122.4194",
            "deleted": False
        }
        location = schemas.PayeeLocation(ynab_py=ynab_client, _json=location_json)
        
        assert location.id == "loc-123"
        assert location.payee_id == "payee-123"
        assert location.deleted == False


@pytest.mark.unit
class TestSubTransaction:
    """Test SubTransaction schema."""
    
    def test_init(self, ynab_client):
        """Test SubTransaction initialization."""
        subtxn_json = {
            "id": "subtxn-123",
            "transaction_id": "txn-123",
            "amount": -25000,
            "memo": "Split",
            "payee_id": "payee-123",
            "category_id": "cat-123",
            "deleted": False
        }
        subtxn = schemas.SubTransaction(ynab_py=ynab_client, _json=subtxn_json)
        
        assert subtxn.id == "subtxn-123"
        assert subtxn.amount == -25000
        assert subtxn.memo == "Split"


@pytest.mark.unit
class TestScheduledTransaction:
    """Test ScheduledTransaction schema."""
    
    def test_init(self, ynab_client):
        """Test ScheduledTransaction initialization."""
        scheduled_json = {
            "id": "sched-123",
            "date_first": "2025-11-01",
            "date_next": "2025-12-01",
            "frequency": "monthly",
            "amount": -100000,
            "account_id": "account-123",
            "payee_id": "payee-123",
            "category_id": "cat-123",
            "flag_color": None,
            "scheduled_subtransactions": [],
            "deleted": False
        }
        scheduled = schemas.ScheduledTransaction(ynab_py=ynab_client, _json=scheduled_json)
        
        assert scheduled.id == "sched-123"
        assert scheduled.frequency.value == "monthly"
        assert scheduled.amount == -100000


