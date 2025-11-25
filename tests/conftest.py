"""
Pytest configuration and shared fixtures for ynab-py tests.
"""

import pytest
from datetime import datetime, date
from unittest.mock import Mock, MagicMock
import responses

from ynab_py import YnabPy
from ynab_py.cache import Cache
from ynab_py.rate_limiter import RateLimiter
import ynab_py.enums as enums


@pytest.fixture
def mock_bearer_token():
    """Fixture providing a mock bearer token."""
    return "test_bearer_token_12345"


@pytest.fixture
def ynab_client(mock_bearer_token):
    """Fixture providing a YnabPy instance with mocked settings."""
    return YnabPy(
        bearer=mock_bearer_token,
        enable_rate_limiting=False,
        enable_caching=False
    )


@pytest.fixture
def ynab_client_with_features(mock_bearer_token):
    """Fixture providing a YnabPy instance with all features enabled."""
    return YnabPy(
        bearer=mock_bearer_token,
        enable_rate_limiting=True,
        enable_caching=True,
        cache_ttl=60
    )


@pytest.fixture
def cache():
    """Fixture providing a fresh Cache instance."""
    return Cache(max_size=50, default_ttl=60)


@pytest.fixture
def rate_limiter():
    """Fixture providing a fresh RateLimiter instance."""
    return RateLimiter(requests_per_hour=200, safety_margin=0.9)


@pytest.fixture
def sample_user_json():
    """Fixture providing sample user JSON data."""
    return {
        "data": {
            "user": {
                "id": "user-123"
            }
        }
    }


@pytest.fixture
def sample_budget_json():
    """Fixture providing sample budget JSON data."""
    return {
        "id": "budget-123",
        "name": "Test Budget",
        "last_modified_on": "2025-11-24T12:00:00Z",
        "first_month": "2025-01-01",
        "last_month": "2025-12-01",
        "date_format": {"format": "DD/MM/YYYY"},
        "currency_format": {
            "iso_code": "USD",
            "example_format": "$1,234.56",
            "decimal_digits": 2,
            "decimal_separator": ".",
            "symbol_first": True,
            "group_separator": ",",
            "currency_symbol": "$",
            "display_symbol": True
        }
    }


@pytest.fixture
def sample_budgets_response(sample_budget_json):
    """Fixture providing sample budgets API response."""
    return {
        "data": {
            "budgets": [sample_budget_json],
            "default_budget": None
        }
    }


@pytest.fixture
def sample_account_json():
    """Fixture providing sample account JSON data."""
    return {
        "id": "account-123",
        "name": "Checking Account",
        "type": "checking",
        "on_budget": True,
        "closed": False,
        "note": "Main checking account",
        "balance": 150000,  # $150.00 in milliunits
        "cleared_balance": 145000,
        "uncleared_balance": 5000,
        "transfer_payee_id": "payee-transfer-123",
        "direct_import_linked": False,
        "direct_import_in_error": False,
        "last_reconciled_at": None,
        "debt_original_balance": None,
        "debt_interest_rates": {},
        "debt_minimum_payments": {},
        "debt_escrow_amounts": {}
    }


@pytest.fixture
def sample_transaction_json():
    """Fixture providing sample transaction JSON data."""
    return {
        "id": "txn-123",
        "date": "2025-11-24",
        "amount": -50000,  # -$50.00 in milliunits
        "memo": "Grocery shopping",
        "cleared": "cleared",
        "approved": True,
        "flag_color": "red",
        "account_id": "account-123",
        "account_name": "Checking Account",
        "payee_id": "payee-123",
        "payee_name": "Grocery Store",
        "category_id": "cat-123",
        "category_name": "Groceries",
        "transfer_account_id": None,
        "transfer_transaction_id": None,
        "matched_transaction_id": None,
        "import_id": None,
        "import_payee_name": None,
        "import_payee_name_original": None,
        "debt_transaction_type": None,
        "deleted": False,
        "subtransactions": []
    }


@pytest.fixture
def sample_category_json():
    """Fixture providing sample category JSON data."""
    return {
        "id": "cat-123",
        "category_group_id": "catgroup-123",
        "category_group_name": "Monthly Bills",
        "name": "Groceries",
        "hidden": False,
        "original_category_group_id": None,
        "note": "Food and household items",
        "budgeted": 500000,  # $500.00
        "activity": -350000,  # -$350.00 spent
        "balance": 150000,  # $150.00 remaining
        "goal_type": None,
        "goal_needs_whole_amount": False,
        "goal_day": None,
        "goal_cadence": None,
        "goal_cadence_frequency": None,
        "goal_creation_month": None,
        "goal_target": None,
        "goal_target_month": None,
        "goal_percentage_complete": None,
        "goal_months_to_budget": None,
        "goal_under_funded": None,
        "goal_overall_funded": None,
        "goal_overall_left": None,
        "deleted": False
    }


@pytest.fixture
def sample_payee_json():
    """Fixture providing sample payee JSON data."""
    return {
        "id": "payee-123",
        "name": "Grocery Store",
        "transfer_account_id": None,
        "deleted": False
    }


@pytest.fixture
def sample_month_json():
    """Fixture providing sample month JSON data."""
    return {
        "month": "2025-11-01",
        "note": "November budget",
        "income": 500000,  # $500.00
        "budgeted": 450000,  # $450.00
        "activity": -400000,  # -$400.00
        "to_be_budgeted": 50000,  # $50.00
        "age_of_money": 30,
        "deleted": False,
        "categories": []
    }


@pytest.fixture
def mock_responses():
    """Fixture that activates responses mocking for requests."""
    with responses.RequestsMock() as rsps:
        yield rsps


# Marker helpers
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests with mocked dependencies")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "slow: Slow running tests")
