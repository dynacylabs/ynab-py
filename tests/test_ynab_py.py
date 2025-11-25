"""
Tests for ynab_py.ynab_py module.

Tests the main YnabPy class initialization and methods.
"""

import pytest
from unittest.mock import Mock, patch
from ynab_py import YnabPy
from ynab_py.exceptions import ValidationError
from ynab_py.rate_limiter import RateLimiter
from ynab_py.cache import Cache


@pytest.mark.unit
class TestYnabPyInit:
    """Test YnabPy initialization."""
    
    def test_init_without_token_raises_error(self):
        """Test that initializing without bearer token raises ValueError."""
        with pytest.raises(ValueError, match="Bearer token is required"):
            YnabPy(bearer=None)
    
    def test_init_with_token(self, mock_bearer_token):
        """Test successful initialization with token."""
        ynab = YnabPy(bearer=mock_bearer_token)
        assert ynab._bearer == mock_bearer_token
        assert ynab.api_url == "https://api.ynab.com/v1"
    
    def test_init_with_rate_limiting_enabled(self, mock_bearer_token):
        """Test initialization with rate limiting enabled."""
        ynab = YnabPy(bearer=mock_bearer_token, enable_rate_limiting=True)
        assert ynab._rate_limiter is not None
        assert isinstance(ynab._rate_limiter, RateLimiter)
    
    def test_init_with_rate_limiting_disabled(self, mock_bearer_token):
        """Test initialization with rate limiting disabled."""
        ynab = YnabPy(bearer=mock_bearer_token, enable_rate_limiting=False)
        assert ynab._rate_limiter is None
    
    def test_init_with_caching_enabled(self, mock_bearer_token):
        """Test initialization with caching enabled."""
        ynab = YnabPy(bearer=mock_bearer_token, enable_caching=True)
        assert ynab._cache is not None
        assert isinstance(ynab._cache, Cache)
    
    def test_init_with_caching_disabled(self, mock_bearer_token):
        """Test initialization with caching disabled."""
        ynab = YnabPy(bearer=mock_bearer_token, enable_caching=False)
        assert ynab._cache is None
    
    def test_init_with_custom_cache_ttl(self, mock_bearer_token):
        """Test initialization with custom cache TTL."""
        ynab = YnabPy(bearer=mock_bearer_token, enable_caching=True, cache_ttl=600)
        assert ynab._cache.default_ttl == 600
    
    def test_headers_set_correctly(self, mock_bearer_token):
        """Test that headers are set correctly."""
        ynab = YnabPy(bearer=mock_bearer_token)
        assert "Authorization" in ynab._headers
        assert ynab._headers["Authorization"] == f"Bearer {mock_bearer_token}"
        assert ynab._headers["accept"] == "application/json"
    
    def test_server_knowledges_initialized(self, mock_bearer_token):
        """Test that server knowledges are initialized."""
        ynab = YnabPy(bearer=mock_bearer_token)
        assert "get_budget" in ynab._server_knowledges
        assert "get_accounts" in ynab._server_knowledges
        assert "get_transactions" in ynab._server_knowledges
        assert all(v == 0 for v in ynab._server_knowledges.values())
    
    def test_api_instance_created(self, mock_bearer_token):
        """Test that API instance is created."""
        ynab = YnabPy(bearer=mock_bearer_token)
        assert ynab.api is not None
        assert ynab.api.ynab_py == ynab


@pytest.mark.unit
class TestYnabPyMethods:
    """Test YnabPy methods."""
    
    def test_server_knowledges_with_tracking_disabled(self, ynab_client):
        """Test server_knowledges returns 0 when tracking disabled."""
        ynab_client._track_server_knowledge = False
        result = ynab_client.server_knowledges("get_budget")
        assert result == 0
    
    def test_server_knowledges_with_tracking_enabled(self, ynab_client):
        """Test server_knowledges returns value when tracking enabled."""
        ynab_client._track_server_knowledge = True
        ynab_client._server_knowledges["get_budget"] = 42
        result = ynab_client.server_knowledges("get_budget")
        assert result == 42
    
    def test_server_knowledges_nonexistent_endpoint(self, ynab_client):
        """Test server_knowledges with nonexistent endpoint."""
        ynab_client._track_server_knowledge = True
        result = ynab_client.server_knowledges("nonexistent")
        assert result == 0
    
    def test_get_rate_limit_stats_enabled(self, ynab_client_with_features):
        """Test get_rate_limit_stats when rate limiting enabled."""
        stats = ynab_client_with_features.get_rate_limit_stats()
        assert "requests_used" in stats
        assert "max_requests" in stats
    
    def test_get_rate_limit_stats_disabled(self, ynab_client):
        """Test get_rate_limit_stats when rate limiting disabled."""
        stats = ynab_client.get_rate_limit_stats()
        assert stats == {"enabled": False}
    
    def test_get_cache_stats_enabled(self, ynab_client_with_features):
        """Test get_cache_stats when caching enabled."""
        stats = ynab_client_with_features.get_cache_stats()
        assert "size" in stats
        assert "hits" in stats
    
    def test_get_cache_stats_disabled(self, ynab_client):
        """Test get_cache_stats when caching disabled."""
        stats = ynab_client.get_cache_stats()
        assert stats == {"enabled": False}
    
    def test_clear_cache_enabled(self, ynab_client_with_features):
        """Test clear_cache when caching enabled."""
        ynab_client_with_features._cache.set("key", "value")
        ynab_client_with_features.clear_cache()
        assert ynab_client_with_features._cache.get("key") is None
    
    def test_clear_cache_disabled(self, ynab_client):
        """Test clear_cache when caching disabled (no error)."""
        ynab_client.clear_cache()  # Should not raise


@pytest.mark.unit
class TestYnabPyProperties:
    """Test YnabPy properties."""
    
    @patch('ynab_py.api.Api.get_user')
    def test_user_property(self, mock_get_user, ynab_client):
        """Test user property calls API."""
        mock_get_user.return_value = Mock(id="user-123")
        
        user = ynab_client.user
        
        mock_get_user.assert_called_once()
        assert user.id == "user-123"
    
    @patch('ynab_py.api.Api.get_budgets')
    def test_budgets_property(self, mock_get_budgets, ynab_client):
        """Test budgets property calls API."""
        mock_budgets = Mock()
        mock_get_budgets.return_value = mock_budgets
        
        budgets = ynab_client.budgets
        
        mock_get_budgets.assert_called_once()
        assert budgets == mock_budgets


@pytest.mark.unit
class TestYnabPyLogging:
    """Test YnabPy logging configuration."""
    
    @patch('logging.basicConfig')
    def test_logging_configured_with_level(self, mock_basicConfig, mock_bearer_token):
        """Test that logging is configured when log_level is provided."""
        ynab = YnabPy(bearer=mock_bearer_token, log_level="DEBUG")
        mock_basicConfig.assert_called_once()
