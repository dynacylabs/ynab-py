"""
Tests for ynab_py.exceptions module.

Tests all custom exception classes including hierarchy, attributes, and formatting.
"""

import pytest
from ynab_py.exceptions import (
    YnabError,
    YnabApiError,
    AuthenticationError,
    AuthorizationError,
    NotFoundError,
    RateLimitError,
    ValidationError,
    ConflictError,
    ServerError,
    NetworkError
)


@pytest.mark.unit
class TestYnabError:
    """Test base YnabError exception."""
    
    def test_init_with_message_only(self):
        """Test YnabError initialization with just a message."""
        error = YnabError("Something went wrong")
        assert error.message == "Something went wrong"
        assert error.details == {}
        assert str(error) == "Something went wrong"
    
    def test_init_with_details(self):
        """Test YnabError initialization with details."""
        details = {"error_code": 123, "field": "budget_id"}
        error = YnabError("Invalid budget", details=details)
        assert error.message == "Invalid budget"
        assert error.details == details
        assert "Details:" in str(error)
        assert "error_code" in str(error)
    
    def test_inheritance(self):
        """Test YnabError inherits from Exception."""
        error = YnabError("test")
        assert isinstance(error, Exception)


@pytest.mark.unit
class TestYnabApiError:
    """Test YnabApiError exception."""
    
    def test_init_with_all_fields(self):
        """Test YnabApiError with all fields provided."""
        error = YnabApiError(
            message="API Error",
            error_id="err-123",
            error_name="invalid_request",
            error_detail="Budget not found",
            status_code=404
        )
        assert error.message == "API Error"
        assert error.error_id == "err-123"
        assert error.error_name == "invalid_request"
        assert error.error_detail == "Budget not found"
        assert error.status_code == 404
        assert error.details["error_id"] == "err-123"
    
    def test_init_filters_none_values(self):
        """Test that None values are filtered from details."""
        error = YnabApiError(
            message="API Error",
            error_id="err-123",
            error_name=None,
            error_detail=None,
            status_code=None
        )
        assert error.error_id == "err-123"
        assert "error_id" in error.details
        assert "error_name" not in error.details
        assert "error_detail" not in error.details
    
    def test_inheritance(self):
        """Test YnabApiError inherits from YnabError."""
        error = YnabApiError("test")
        assert isinstance(error, YnabError)


@pytest.mark.unit
class TestAuthenticationError:
    """Test AuthenticationError exception."""
    
    def test_default_message(self):
        """Test default authentication error message."""
        error = AuthenticationError()
        assert "Authentication failed" in error.message
        assert "API token" in error.message
        assert error.status_code == 401
    
    def test_custom_message(self):
        """Test custom authentication error message."""
        error = AuthenticationError("Token expired")
        assert error.message == "Token expired"
        assert error.status_code == 401
    
    def test_inheritance(self):
        """Test AuthenticationError inherits from YnabApiError."""
        error = AuthenticationError()
        assert isinstance(error, YnabApiError)


@pytest.mark.unit
class TestAuthorizationError:
    """Test AuthorizationError exception."""
    
    def test_default_message(self):
        """Test default authorization error message."""
        error = AuthorizationError()
        assert "Access denied" in error.message
        assert error.status_code == 403
    
    def test_custom_message(self):
        """Test custom authorization error message."""
        error = AuthorizationError("No permission")
        assert error.message == "No permission"


@pytest.mark.unit
class TestNotFoundError:
    """Test NotFoundError exception."""
    
    def test_default_message(self):
        """Test default not found error message."""
        error = NotFoundError()
        assert "not found" in error.message.lower()
        assert error.status_code == 404
    
    def test_with_resource_type(self):
        """Test NotFoundError with resource type."""
        error = NotFoundError("Budget not found", resource_type="budget")
        assert error.message == "Budget not found"
        assert error.resource_type == "budget"


@pytest.mark.unit
class TestRateLimitError:
    """Test RateLimitError exception."""
    
    def test_default_message(self):
        """Test default rate limit error message."""
        error = RateLimitError()
        assert "Rate limit" in error.message
        assert "200 requests per hour" in error.message
        assert error.status_code == 429
        assert error.retry_after is None
    
    def test_with_retry_after(self):
        """Test RateLimitError with retry_after."""
        error = RateLimitError(retry_after=3600)
        assert error.retry_after == 3600
        assert error.details["retry_after"] == 3600


@pytest.mark.unit
class TestValidationError:
    """Test ValidationError exception."""
    
    def test_basic_validation_error(self):
        """Test basic validation error."""
        error = ValidationError("Invalid input")
        assert error.message == "Invalid input"
        assert error.field is None
        assert error.value is None
    
    def test_with_field_and_value(self):
        """Test ValidationError with field and value."""
        error = ValidationError("Invalid amount", field="amount", value=-100)
        assert error.message == "Invalid amount"
        assert error.field == "amount"
        assert error.value == -100
        assert error.details["field"] == "amount"
        assert error.details["value"] == -100
    
    def test_inheritance(self):
        """Test ValidationError inherits from YnabError."""
        error = ValidationError("test")
        assert isinstance(error, YnabError)


@pytest.mark.unit
class TestConflictError:
    """Test ConflictError exception."""
    
    def test_default_message(self):
        """Test default conflict error message."""
        error = ConflictError()
        assert "conflict" in error.message.lower()
        assert error.status_code == 409
    
    def test_custom_message(self):
        """Test custom conflict error message."""
        error = ConflictError("Duplicate transaction")
        assert error.message == "Duplicate transaction"


@pytest.mark.unit
class TestServerError:
    """Test ServerError exception."""
    
    def test_default_message(self):
        """Test default server error message."""
        error = ServerError()
        assert "server error" in error.message.lower()
        assert error.status_code == 500
    
    def test_custom_status_code(self):
        """Test ServerError with custom status code."""
        error = ServerError("Database error", status_code=503)
        assert error.message == "Database error"
        assert error.status_code == 503


@pytest.mark.unit
class TestNetworkError:
    """Test NetworkError exception."""
    
    def test_default_message(self):
        """Test default network error message."""
        error = NetworkError()
        assert "Network error" in error.message
    
    def test_custom_message(self):
        """Test custom network error message."""
        error = NetworkError("Connection timeout")
        assert error.message == "Connection timeout"
    
    def test_inheritance(self):
        """Test NetworkError inherits from YnabError."""
        error = NetworkError()
        assert isinstance(error, YnabError)
        assert not isinstance(error, YnabApiError)
