"""
Comprehensive tests for pynab.py module.
"""

import pytest
import responses
from unittest.mock import Mock, patch, MagicMock

from ynab_py.pynab import YnabPy as PynabClient
from ynab_py.api import Api
from ynab_py import constants
from tests.test_config import is_live_mode, skip_if_no_token


class TestPynabInitialization:
    """Test Pynab YnabPy initialization and configuration."""

    def test_init_with_bearer_token(self):
        """Test initialization with bearer token."""
        bearer = "test_token_123"
        client = PynabClient(bearer=bearer)
        
        assert client._bearer == bearer
        assert client.api_url == constants.YNAB_API
        assert client._fetch is True
        assert client._track_server_knowledge is False
        assert client._requests_remaining == 0
        assert client._headers["Authorization"] == f"Bearer {bearer}"
        assert client._headers["accept"] == "application/json"
        assert isinstance(client.api, Api)

    def test_init_without_bearer_token(self):
        """Test initialization without bearer token."""
        client = PynabClient(bearer=None)
        
        assert client._bearer is None
        assert client._headers["Authorization"] == "Bearer None"

    def test_server_knowledges_initialized(self):
        """Test that server_knowledges dictionary is properly initialized."""
        client = PynabClient(bearer="test_token")
        
        expected_endpoints = [
            "get_budget",
            "get_accounts",
            "get_categories",
            "get_months",
            "get_transactions",
            "get_account_transactions",
            "get_category_transactions",
            "get_payee_transactions",
            "get_month_transactions",
            "get_scheduled_transactions",
        ]
        
        for endpoint in expected_endpoints:
            assert endpoint in client._server_knowledges
            assert client._server_knowledges[endpoint] == 0


class TestPynabServerKnowledge:
    """Test server knowledge tracking functionality."""

    def test_server_knowledges_disabled(self):
        """Test server_knowledges returns 0 when tracking disabled."""
        client = PynabClient(bearer="test_token")
        client._track_server_knowledge = False
        client._server_knowledges["get_budget"] = 100
        
        result = client.server_knowledges("get_budget")
        assert result == 0

    def test_server_knowledges_enabled(self):
        """Test server_knowledges returns actual value when tracking enabled."""
        client = PynabClient(bearer="test_token")
        client._track_server_knowledge = True
        client._server_knowledges["get_budget"] = 100
        
        result = client.server_knowledges("get_budget")
        assert result == 100

    def test_server_knowledges_different_endpoints(self):
        """Test server_knowledges with different endpoints."""
        client = PynabClient(bearer="test_token")
        client._track_server_knowledge = True
        client._server_knowledges["get_transactions"] = 250
        client._server_knowledges["get_accounts"] = 150
        
        assert client.server_knowledges("get_transactions") == 250
        assert client.server_knowledges("get_accounts") == 150

