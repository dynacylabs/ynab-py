"""
ynab-py: A Pythonic wrapper for the YNAB API

This library provides an intuitive, object-oriented interface to the
You Need A Budget (YNAB) API with features including:
- Automatic rate limiting
- Response caching
- Comprehensive error handling
- Utility functions for common operations
- Type hints for better IDE support

Example:
    >>> from ynab_py import YnabPy
    >>> ynab = YnabPy(bearer="your_token")
    >>> budget = ynab.budgets.by(field="name", value="My Budget", first=True)
    >>> print(f"Budget: {budget.name}")
"""

from .ynab_py import YnabPy
from .exceptions import (
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
from . import utils
from . import enums
from . import schemas

__version__ = "0.1.0"

__all__ = [
    "YnabPy",
    # Exceptions
    "YnabError",
    "YnabApiError",
    "AuthenticationError",
    "AuthorizationError",
    "NotFoundError",
    "RateLimitError",
    "ValidationError",
    "ConflictError",
    "ServerError",
    "NetworkError",
    # Modules
    "utils",
    "enums",
    "schemas",
]
