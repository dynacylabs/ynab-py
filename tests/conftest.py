"""
Test configuration and fixtures for ynab-py.
"""

import os
import pytest
import responses as responses_lib
from typing import Dict, Any


# Test configuration
TEST_BASE_URL = "https://api.ynab.com/v1"
TEST_API_KEY = "test_api_key_12345"
TEST_TIMEOUT = 30


@pytest.fixture
def api_key():
    """Return a test API key."""
    return TEST_API_KEY


@pytest.fixture
def base_url():
    """Return the test base URL."""
    return TEST_BASE_URL


@pytest.fixture
def responses():
    """Enable responses mock for HTTP requests."""
    with responses_lib.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def sample_budget_response() -> Dict[str, Any]:
    """Sample budget response data for testing."""
    return {
        "data": {
            "budgets": [
                {
                    "id": "budget-123",
                    "name": "Test Budget",
                    "last_modified_on": "2023-01-01T00:00:00.000Z",
                    "first_month": "2023-01-01",
                    "last_month": "2023-12-01"
                }
            ]
        }
    }


@pytest.fixture
def sample_account_response() -> Dict[str, Any]:
    """Sample account response data for testing."""
    return {
        "data": {
            "accounts": [
                {
                    "id": "account-456",
                    "name": "Checking Account",
                    "type": "checking",
                    "on_budget": True,
                    "closed": False,
                    "balance": 100000
                }
            ]
        }
    }


@pytest.fixture
def sample_transaction_response() -> Dict[str, Any]:
    """Sample transaction response data for testing."""
    return {
        "data": {
            "transactions": [
                {
                    "id": "transaction-789",
                    "date": "2023-01-15",
                    "amount": -25000,
                    "memo": "Test transaction",
                    "cleared": "cleared",
                    "approved": True,
                    "account_id": "account-456"
                }
            ]
        }
    }


@pytest.fixture
def sample_error_response() -> Dict[str, Any]:
    """Sample error response data for testing."""
    return {
        "error": {
            "id": "400",
            "name": "bad_request",
            "detail": "Something went wrong"
        }
    }
