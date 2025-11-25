"""
Custom exceptions for ynab-py library.

This module provides detailed exception classes for better error handling
and debugging when interacting with the YNAB API.
"""

from typing import Optional, Dict, Any


class YnabError(Exception):
    """Base exception class for all ynab-py errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        """
        Initialize the exception.
        
        Args:
            message: Human-readable error message
            details: Additional error details from the API
        """
        super().__init__(message)
        self.message = message
        self.details = details or {}
    
    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class YnabApiError(YnabError):
    """
    Exception raised when the YNAB API returns an error response.
    
    This exception contains detailed information about API errors including
    error ID, name, and detail message from the API.
    """
    
    def __init__(
        self,
        message: str,
        error_id: Optional[str] = None,
        error_name: Optional[str] = None,
        error_detail: Optional[str] = None,
        status_code: Optional[int] = None
    ):
        """
        Initialize API error with YNAB-specific error details.
        
        Args:
            message: Human-readable error message
            error_id: YNAB error ID
            error_name: YNAB error name/type
            error_detail: Detailed error description from YNAB
            status_code: HTTP status code of the error response
        """
        details = {
            "error_id": error_id,
            "error_name": error_name,
            "error_detail": error_detail,
            "status_code": status_code
        }
        # Remove None values
        details = {k: v for k, v in details.items() if v is not None}
        super().__init__(message, details)
        self.error_id = error_id
        self.error_name = error_name
        self.error_detail = error_detail
        self.status_code = status_code


class AuthenticationError(YnabApiError):
    """
    Exception raised when authentication fails.
    
    This typically indicates an invalid or expired API token.
    """
    
    def __init__(self, message: str = "Authentication failed. Please check your API token."):
        super().__init__(message, status_code=401)


class AuthorizationError(YnabApiError):
    """
    Exception raised when the user doesn't have permission to access a resource.
    """
    
    def __init__(self, message: str = "Access denied. You don't have permission to access this resource."):
        super().__init__(message, status_code=403)


class NotFoundError(YnabApiError):
    """
    Exception raised when a requested resource is not found.
    """
    
    def __init__(self, message: str = "The requested resource was not found.", resource_type: Optional[str] = None):
        super().__init__(message, status_code=404)
        self.resource_type = resource_type


class RateLimitError(YnabApiError):
    """
    Exception raised when API rate limit is exceeded.
    
    YNAB API allows 200 requests per hour per token.
    """
    
    def __init__(
        self,
        message: str = "Rate limit exceeded. YNAB allows 200 requests per hour.",
        retry_after: Optional[int] = None
    ):
        super().__init__(message, status_code=429)
        self.retry_after = retry_after  # seconds to wait before retry
        if retry_after:
            self.details["retry_after"] = retry_after


class ValidationError(YnabError):
    """
    Exception raised when input validation fails.
    
    This is raised before making an API call when the input parameters
    don't meet the required format or constraints.
    """
    
    def __init__(self, message: str, field: Optional[str] = None, value: Optional[Any] = None):
        details = {}
        if field:
            details["field"] = field
        if value is not None:
            details["value"] = value
        super().__init__(message, details)
        self.field = field
        self.value = value


class ConflictError(YnabApiError):
    """
    Exception raised when there's a conflict with the current state of the resource.
    
    For example, trying to create a transaction that already exists.
    """
    
    def __init__(self, message: str = "The request conflicts with the current state of the resource."):
        super().__init__(message, status_code=409)


class ServerError(YnabApiError):
    """
    Exception raised when the YNAB server encounters an error.
    
    This typically indicates a problem on YNAB's end (5xx status codes).
    """
    
    def __init__(self, message: str = "YNAB server error. Please try again later.", status_code: int = 500):
        super().__init__(message, status_code=status_code)


class NetworkError(YnabError):
    """
    Exception raised when a network error occurs (connection timeout, etc.).
    """
    
    def __init__(self, message: str = "Network error occurred while contacting YNAB API."):
        super().__init__(message)
