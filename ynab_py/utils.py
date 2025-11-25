from datetime import datetime, date
from enum import Enum
from typing import TYPE_CHECKING, Union, List, Dict, Any, Optional
import csv
import io

import json
import requests
import logging

if TYPE_CHECKING:
    from ynab_py.ynab_py import YnabPy
    from ynab_py.schemas import Budget, Account, Transaction


class http_utils:
    def __init__(self, ynab_py: 'YnabPy' = None):
        """
        Initializes HTTP utilities with integrated rate limiting and error handling.

        Args:
            ynab_py: The YnabPy object
        """
        self.ynab_py = ynab_py
    
    def _handle_rate_limiting(self) -> None:
        """Apply rate limiting before making a request."""
        if self.ynab_py and self.ynab_py._rate_limiter:
            self.ynab_py._rate_limiter.wait_if_needed()
    
    def _update_rate_limit_from_headers(self, response: requests.Response) -> None:
        """Extract rate limit info from response headers."""
        if "x-rate-limit" in response.headers:
            rate_limit_str = response.headers["x-rate-limit"]
            used, total = map(int, rate_limit_str.split("/"))
            self.ynab_py._requests_remaining = total - used
        else:
            self.ynab_py._requests_remaining -= 1
    
    def _handle_error_response(self, response: requests.Response) -> None:
        """Handle error responses and raise appropriate exceptions."""
        from ynab_py.exceptions import (
            AuthenticationError, AuthorizationError, NotFoundError,
            RateLimitError, ConflictError, ServerError, YnabApiError
        )
        
        status_code = response.status_code
        
        # Try to parse error details
        try:
            error_data = response.json().get("error", {})
            error_id = error_data.get("id")
            error_name = error_data.get("name")
            error_detail = error_data.get("detail")
        except:
            error_id = None
            error_name = None
            error_detail = response.text
        
        # Raise specific exceptions based on status code
        if status_code == 401:
            raise AuthenticationError()
        elif status_code == 403:
            raise AuthorizationError()
        elif status_code == 404:
            raise NotFoundError(error_detail or "Resource not found")
        elif status_code == 409:
            raise ConflictError(error_detail or "Conflict with current state")
        elif status_code == 429:
            retry_after = response.headers.get("Retry-After")
            raise RateLimitError(retry_after=int(retry_after) if retry_after else None)
        elif status_code >= 500:
            raise ServerError(error_detail or "Server error", status_code=status_code)
        else:
            raise YnabApiError(
                error_detail or f"HTTP {status_code} error",
                error_id=error_id,
                error_name=error_name,
                error_detail=error_detail,
                status_code=status_code
            )

    def get(self, endpoint: str = None):
        """
        Sends a GET request to the specified endpoint with rate limiting.

        Args:
            endpoint: The endpoint to send the request to

        Returns:
            Response: The response object returned by the GET request
            
        Raises:
            YnabApiError: If the API returns an error response
            NetworkError: If a network error occurs
        """
        from ynab_py.exceptions import NetworkError
        
        self._handle_rate_limiting()
        
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"GET {url}")
        
        try:
            response = requests.get(url, headers=self.ynab_py._headers, timeout=30)
            self._update_rate_limit_from_headers(response)
            
            if not response.ok:
                self._handle_error_response(response)
            
            return response
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")

    def post(self, endpoint: str = None, json: dict = {}):
        """
        Sends a POST request to the specified endpoint with the provided JSON data.

        Args:
            endpoint: The endpoint to send the request to
            json: The JSON data to include in the request body

        Returns:
            Response: The response object received from the server
            
        Raises:
            YnabApiError: If the API returns an error response
            NetworkError: If a network error occurs
        """
        from ynab_py.exceptions import NetworkError
        
        self._handle_rate_limiting()
        
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"POST {url}\n{json}")
        
        try:
            response = requests.post(url, json=json, headers=self.ynab_py._headers, timeout=30)
            self._update_rate_limit_from_headers(response)
            
            if not response.ok:
                self._handle_error_response(response)
            
            return response
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")

    def patch(self, endpoint: str = None, json: dict = {}):
        """
        Sends a PATCH request to the specified endpoint with the provided JSON data.

        Args:
            endpoint: The endpoint to send the PATCH request to
            json: The JSON data to include in the request body

        Returns:
            Response: The response object returned by the PATCH request
            
        Raises:
            YnabApiError: If the API returns an error response
            NetworkError: If a network error occurs
        """
        from ynab_py.exceptions import NetworkError
        
        self._handle_rate_limiting()
        
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"PATCH {url}\n{json}")
        
        try:
            response = requests.patch(url, json=json, headers=self.ynab_py._headers, timeout=30)
            self._update_rate_limit_from_headers(response)
            
            if not response.ok:
                self._handle_error_response(response)
            
            return response
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")

    def put(self, endpoint: str = None, json: dict = {}):
        """
        Sends a PUT request to the specified endpoint with the given JSON payload.

        Args:
            endpoint: The endpoint to send the request to
            json: The JSON payload to include in the request

        Returns:
            Response: The response object returned by the server
            
        Raises:
            YnabApiError: If the API returns an error response
            NetworkError: If a network error occurs
        """
        from ynab_py.exceptions import NetworkError
        
        self._handle_rate_limiting()
        
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"PUT {url}\n{json}")
        
        try:
            response = requests.put(url, json=json, headers=self.ynab_py._headers, timeout=30)
            self._update_rate_limit_from_headers(response)
            
            if not response.ok:
                self._handle_error_response(response)
            
            return response
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")

    def delete(self, endpoint: str = None):
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint: The endpoint to send the request to

        Returns:
            Response: The response object returned by the DELETE request
            
        Raises:
            YnabApiError: If the API returns an error response
            NetworkError: If a network error occurs
        """
        from ynab_py.exceptions import NetworkError
        
        self._handle_rate_limiting()
        
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.info(f"DELETE {url}")
        
        try:
            response = requests.delete(url, headers=self.ynab_py._headers, timeout=30)
            self._update_rate_limit_from_headers(response)
            
            if not response.ok:
                self._handle_error_response(response)
            
            return response
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        Returns the default JSON representation of an object.

        Parameters:
        - obj: The object to be serialized.

        Returns:
        The JSON representation of the object.

        Note:
        - If the object is an instance of Enum, the value of the Enum is returned.
        - If the object is an instance of datetime or date, the ISO formatted string representation is returned.
        - For all other objects, the default JSONEncoder's default method is called.

        """
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)  # pragma: no cover


class _dict(dict):
    """
    A custom dictionary class that provides additional functionality.

    This class extends the built-in `dict` class and adds a `by` method
    for filtering the dictionary items based on a specific field and value.

    Attributes:
        None

    Methods:
        by(field: str = "", value: object = None, first: bool = True) -> Union[object, _dict]:
            Filters the dictionary items based on the specified field and value.

    """

    def by(self, field: str = "", value: object = None, first: bool = True):
        """
        Filters the dictionary items based on the specified field and value.

        Args:
            field (str): The name of the field to filter on.
            value (object): The value to filter for.
            first (bool): If True, returns the first matching item. If False, returns a new dictionary with all matching items.

        Returns:
            Union[object, _dict]: If `first` is True, returns the first matching item. If `first` is False, returns a new `_dict` object with all matching items.

        """
        items = _dict()
        for k, v in self.items():
            if getattr(v, field, None) == value:
                if first:
                    return v
                else:
                    items[k] = v
        return items


# Amount conversion utilities
def milliunits_to_dollars(milliunits: int) -> float:
    """
    Convert YNAB milliunits to dollars.
    
    YNAB represents amounts in milliunits (1/1000 of currency unit).
    
    Args:
        milliunits: Amount in milliunits
        
    Returns:
        Amount in dollars
        
    Example:
        >>> milliunits_to_dollars(25000)
        25.0
        >>> milliunits_to_dollars(-15500)
        -15.5
    """
    return milliunits / 1000.0


def dollars_to_milliunits(dollars: float) -> int:
    """
    Convert dollars to YNAB milliunits.
    
    Args:
        dollars: Amount in dollars
        
    Returns:
        Amount in milliunits (rounded to nearest milliunit)
        
    Example:
        >>> dollars_to_milliunits(25.0)
        25000
        >>> dollars_to_milliunits(15.50)
        15500
    """
    return int(round(dollars * 1000))


def format_amount(milliunits: int, currency_symbol: str = "$", decimal_places: int = 2) -> str:
    """
    Format a YNAB amount for display.
    
    Args:
        milliunits: Amount in milliunits
        currency_symbol: Currency symbol to use (default: $)
        decimal_places: Number of decimal places (default: 2)
        
    Returns:
        Formatted amount string
        
    Example:
        >>> format_amount(25000)
        '$25.00'
        >>> format_amount(-15500)
        '-$15.50'
    """
    dollars = milliunits_to_dollars(milliunits)
    if dollars < 0:
        return f"-{currency_symbol}{abs(dollars):.{decimal_places}f}"
    return f"{currency_symbol}{dollars:.{decimal_places}f}"


# Date utilities
def parse_date(date_str: str) -> date:
    """
    Parse a date string in ISO format.
    
    Args:
        date_str: Date string in ISO format (YYYY-MM-DD)
        
    Returns:
        date object
        
    Example:
        >>> parse_date("2025-11-24")
        datetime.date(2025, 11, 24)
    """
    return datetime.fromisoformat(date_str).date()


def format_date_for_api(date_obj: Union[date, datetime, str]) -> str:
    """
    Format a date for YNAB API (ISO format).
    
    Args:
        date_obj: Date to format (date, datetime, or ISO string)
        
    Returns:
        ISO formatted date string (YYYY-MM-DD)
        
    Example:
        >>> from datetime import date
        >>> format_date_for_api(date(2025, 11, 24))
        '2025-11-24'
    """
    if isinstance(date_obj, str):
        # Verify it's a valid date string
        parse_date(date_obj)
        return date_obj
    elif isinstance(date_obj, datetime):
        return date_obj.date().isoformat()
    elif isinstance(date_obj, date):
        return date_obj.isoformat()
    else:
        raise ValueError(f"Cannot format {type(date_obj)} as date")


# Export utilities
def export_transactions_to_csv(
    transactions: Dict[str, 'Transaction'],
    file_path: Optional[str] = None,
    include_columns: Optional[List[str]] = None
) -> Optional[str]:
    """
    Export transactions to CSV format.
    
    Args:
        transactions: Dictionary of transactions (id -> Transaction)
        file_path: Path to save CSV file (if None, returns CSV string)
        include_columns: List of column names to include (defaults to all)
        
    Returns:
        CSV string if file_path is None, otherwise None
        
    Example:
        # Export to file
        export_transactions_to_csv(account.transactions, "transactions.csv")
        
        # Get CSV string
        csv_data = export_transactions_to_csv(account.transactions)
    """
    if not transactions:
        return "" if file_path is None else None
    
    default_columns = [
        'date', 'payee_name', 'category_name', 'memo',
        'amount', 'cleared', 'approved', 'account_name'
    ]
    columns = include_columns or default_columns
    
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=columns, extrasaction='ignore')
    writer.writeheader()
    
    for txn in transactions.values():
        row = {}
        for col in columns:
            value = getattr(txn, col, '')
            if col == 'amount':
                value = milliunits_to_dollars(value)
            elif col == 'date':
                value = str(value)
            elif isinstance(value, Enum):
                value = value.value
            row[col] = value
        writer.writerow(row)
    
    csv_string = output.getvalue()
    output.close()
    
    if file_path:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            f.write(csv_string)
        return None
    
    return csv_string


def filter_transactions_by_date_range(
    transactions: Dict[str, 'Transaction'],
    start_date: Union[date, str],
    end_date: Optional[Union[date, str]] = None
) -> Dict[str, 'Transaction']:
    """
    Filter transactions by date range.
    
    Args:
        transactions: Dictionary of transactions
        start_date: Start date (inclusive)
        end_date: End date (inclusive, defaults to today)
        
    Returns:
        Filtered dictionary of transactions
        
    Example:
        from datetime import date, timedelta
        last_30_days = date.today() - timedelta(days=30)
        recent = filter_transactions_by_date_range(
            account.transactions,
            last_30_days
        )
    """
    if isinstance(start_date, str):
        start_date = parse_date(start_date)
    if end_date is None:
        end_date = date.today()
    elif isinstance(end_date, str):
        end_date = parse_date(end_date)
    
    return _dict({
        txn_id: txn
        for txn_id, txn in transactions.items()
        if start_date <= txn.date <= end_date
    })


def calculate_net_worth(budget: 'Budget', include_closed: bool = False) -> int:
    """
    Calculate total net worth from all accounts in a budget.
    
    Args:
        budget: Budget object
        include_closed: Whether to include closed accounts (default: False)
        
    Returns:
        Total net worth in milliunits
        
    Example:
        net_worth = calculate_net_worth(my_budget)
        print(f"Net Worth: {format_amount(net_worth)}")
    """
    total = 0
    for account in budget.accounts.values():
        if not include_closed and account.closed:
            continue
        total += account.balance
    return total


def get_spending_by_category(
    transactions: Dict[str, 'Transaction'],
    outflow_only: bool = True
) -> Dict[str, int]:
    """
    Calculate total spending/activity by category.
    
    Args:
        transactions: Dictionary of transactions
        outflow_only: Only include outflows/spending (default: True)
        
    Returns:
        Dictionary mapping category_name -> total amount in milliunits
        
    Example:
        spending = get_spending_by_category(account.transactions)
        for category, amount in sorted(spending.items(), key=lambda x: x[1]):
            print(f"{category}: {format_amount(amount)}")
    """
    category_totals: Dict[str, int] = {}
    
    for txn in transactions.values():
        if outflow_only and txn.amount >= 0:
            continue
        
        category = txn.category_name or "Uncategorized"
        category_totals[category] = category_totals.get(category, 0) + abs(txn.amount)
    
    return category_totals


def get_spending_by_payee(
    transactions: Dict[str, 'Transaction'],
    outflow_only: bool = True
) -> Dict[str, int]:
    """
    Calculate total spending/activity by payee.
    
    Args:
        transactions: Dictionary of transactions
        outflow_only: Only include outflows/spending (default: True)
        
    Returns:
        Dictionary mapping payee_name -> total amount in milliunits
        
    Example:
        spending = get_spending_by_payee(account.transactions)
        top_payees = sorted(spending.items(), key=lambda x: x[1], reverse=True)[:10]
    """
    payee_totals: Dict[str, int] = {}
    
    for txn in transactions.values():
        if outflow_only and txn.amount >= 0:
            continue
        
        payee = txn.payee_name or "Unknown"
        payee_totals[payee] = payee_totals.get(payee, 0) + abs(txn.amount)
    
    return payee_totals
