"""
Tests for ynab_py.utils module.

Tests utility functions for HTTP, conversions, formatting, and data operations.
"""

import pytest
import io
from datetime import date, datetime
from enum import Enum
from unittest.mock import Mock, patch, MagicMock
import requests
import responses

from ynab_py import utils
from ynab_py.exceptions import (
    AuthenticationError, AuthorizationError, NotFoundError,
    RateLimitError, ConflictError, ServerError, NetworkError, YnabApiError
)


@pytest.mark.unit
class TestHttpUtils:
    """Test http_utils class."""
    
    def test_init(self, ynab_client):
        """Test http_utils initialization."""
        http = utils.http_utils(ynab_py=ynab_client)
        assert http.ynab_py == ynab_client
    
    @responses.activate
    def test_get_success(self, ynab_client):
        """Test successful GET request."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/user",
            json={"data": {"user": {"id": "user-123"}}},
            status=200,
            headers={"x-rate-limit": "5/200"}
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        response = http.get("/user")
        
        assert response.status_code == 200
        assert response.json()["data"]["user"]["id"] == "user-123"
        assert ynab_client._requests_remaining == 195
    
    @responses.activate
    def test_get_authentication_error(self, ynab_client):
        """Test GET request with 401 error."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/user",
            json={"error": {"id": "401", "name": "unauthorized", "detail": "Invalid token"}},
            status=401
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(AuthenticationError):
            http.get("/user")
    
    @responses.activate
    def test_get_not_found_error(self, ynab_client):
        """Test GET request with 404 error."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets/bad-id",
            json={"error": {"detail": "Budget not found"}},
            status=404
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(NotFoundError):
            http.get("/budgets/bad-id")
    
    @responses.activate
    def test_get_rate_limit_error(self, ynab_client):
        """Test GET request with 429 error."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/user",
            json={"error": {"detail": "Rate limit exceeded"}},
            status=429,
            headers={"Retry-After": "3600"}
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(RateLimitError) as exc_info:
            http.get("/user")
        assert exc_info.value.retry_after == 3600
    
    @responses.activate
    def test_get_server_error(self, ynab_client):
        """Test GET request with 500 error."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/user",
            json={"error": {"detail": "Internal server error"}},
            status=500
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(ServerError):
            http.get("/user")
    
    @responses.activate
    def test_post_success(self, ynab_client):
        """Test successful POST request."""
        responses.add(
            responses.POST,
            "https://api.ynab.com/v1/budgets/123/transactions",
            json={"data": {"transaction": {"id": "txn-123"}}},
            status=201
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        response = http.post("/budgets/123/transactions", json={"transaction": {}})
        
        assert response.status_code == 201
    
    @responses.activate
    def test_patch_success(self, ynab_client):
        """Test successful PATCH request."""
        responses.add(
            responses.PATCH,
            "https://api.ynab.com/v1/budgets/123/transactions",
            json={"data": {}},
            status=200
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        response = http.patch("/budgets/123/transactions", json={})
        
        assert response.status_code == 200
    
    @responses.activate
    def test_put_success(self, ynab_client):
        """Test successful PUT request."""
        responses.add(
            responses.PUT,
            "https://api.ynab.com/v1/budgets/123/transactions/txn-1",
            json={"data": {}},
            status=200
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        response = http.put("/budgets/123/transactions/txn-1", json={})
        
        assert response.status_code == 200
    
    @responses.activate
    def test_delete_success(self, ynab_client):
        """Test successful DELETE request."""
        responses.add(
            responses.DELETE,
            "https://api.ynab.com/v1/budgets/123/transactions/txn-1",
            json={"data": {}},
            status=200
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        response = http.delete("/budgets/123/transactions/txn-1")
        
        assert response.status_code == 200
    
    def test_get_network_error(self, ynab_client):
        """Test GET request with network error."""
        http = utils.http_utils(ynab_py=ynab_client)
        
        with patch('requests.get', side_effect=requests.exceptions.ConnectionError("Connection failed")):
            with pytest.raises(NetworkError):
                http.get("/user")
    
    def test_rate_limiting_integration(self, ynab_client_with_features):
        """Test that rate limiting is called."""
        http = utils.http_utils(ynab_py=ynab_client_with_features)
        
        with patch.object(ynab_client_with_features._rate_limiter, 'wait_if_needed') as mock_wait:
            with responses.RequestsMock() as rsps:
                rsps.add(responses.GET, "https://api.ynab.com/v1/user", json={}, status=200)
                http.get("/user")
                assert mock_wait.called


@pytest.mark.unit
class TestCustomJsonEncoder:
    """Test CustomJsonEncoder class."""
    
    def test_encode_enum(self):
        """Test encoding enum values."""
        from ynab_py.enums import AccountType
        import json
        
        data = {"type": AccountType.CHECKING}
        result = json.dumps(data, cls=utils.CustomJsonEncoder)
        assert "checking" in result
    
    def test_encode_datetime(self):
        """Test encoding datetime."""
        import json
        
        dt = datetime(2025, 11, 24, 12, 0, 0)
        data = {"date": dt}
        result = json.dumps(data, cls=utils.CustomJsonEncoder)
        assert "2025-11-24" in result
    
    def test_encode_date(self):
        """Test encoding date."""
        import json
        
        d = date(2025, 11, 24)
        data = {"date": d}
        result = json.dumps(data, cls=utils.CustomJsonEncoder)
        assert "2025-11-24" in result


@pytest.mark.unit
class TestDictClass:
    """Test custom _dict class."""
    
    def test_by_method_first(self):
        """Test by method returning first match."""
        class MockObj:
            def __init__(self, id, name):
                self.id = id
                self.name = name
        
        d = utils._dict()
        d["1"] = MockObj("1", "Alice")
        d["2"] = MockObj("2", "Bob")
        d["3"] = MockObj("3", "Alice")
        
        result = d.by(field="name", value="Alice", first=True)
        assert result.id == "1"
    
    def test_by_method_all(self):
        """Test by method returning all matches."""
        class MockObj:
            def __init__(self, id, name):
                self.id = id
                self.name = name
        
        d = utils._dict()
        d["1"] = MockObj("1", "Alice")
        d["2"] = MockObj("2", "Bob")
        d["3"] = MockObj("3", "Alice")
        
        result = d.by(field="name", value="Alice", first=False)
        assert len(result) == 2
        assert "1" in result
        assert "3" in result
    
    def test_by_method_no_match(self):
        """Test by method with no matches."""
        class MockObj:
            def __init__(self, id, name):
                self.id = id
                self.name = name
        
        d = utils._dict()
        d["1"] = MockObj("1", "Alice")
        
        result = d.by(field="name", value="Charlie", first=False)
        assert len(result) == 0


@pytest.mark.unit
class TestAmountConversions:
    """Test amount conversion utilities."""
    
    def test_milliunits_to_dollars(self):
        """Test converting milliunits to dollars."""
        assert utils.milliunits_to_dollars(25000) == 25.0
        assert utils.milliunits_to_dollars(-15500) == -15.5
        assert utils.milliunits_to_dollars(0) == 0.0
        assert utils.milliunits_to_dollars(1) == 0.001
    
    def test_dollars_to_milliunits(self):
        """Test converting dollars to milliunits."""
        assert utils.dollars_to_milliunits(25.0) == 25000
        assert utils.dollars_to_milliunits(15.50) == 15500
        assert utils.dollars_to_milliunits(0.0) == 0
        assert utils.dollars_to_milliunits(-100.25) == -100250
    
    def test_format_amount(self):
        """Test formatting amounts for display."""
        assert utils.format_amount(25000) == "$25.00"
        assert utils.format_amount(-15500) == "-$15.50"
        assert utils.format_amount(0) == "$0.00"
        assert utils.format_amount(100) == "$0.10"
    
    def test_format_amount_custom_symbol(self):
        """Test formatting with custom currency symbol."""
        assert utils.format_amount(25000, currency_symbol="€") == "€25.00"
    
    def test_format_amount_custom_decimals(self):
        """Test formatting with custom decimal places."""
        assert utils.format_amount(25000, decimal_places=0) == "$25"


@pytest.mark.unit
class TestDateUtilities:
    """Test date utility functions."""
    
    def test_parse_date(self):
        """Test parsing ISO date string."""
        result = utils.parse_date("2025-11-24")
        assert result == date(2025, 11, 24)
    
    def test_format_date_for_api_from_date(self):
        """Test formatting date object."""
        d = date(2025, 11, 24)
        result = utils.format_date_for_api(d)
        assert result == "2025-11-24"
    
    def test_format_date_for_api_from_datetime(self):
        """Test formatting datetime object."""
        dt = datetime(2025, 11, 24, 12, 30, 0)
        result = utils.format_date_for_api(dt)
        assert result == "2025-11-24"
    
    def test_format_date_for_api_from_string(self):
        """Test formatting date string."""
        result = utils.format_date_for_api("2025-11-24")
        assert result == "2025-11-24"
    
    def test_format_date_for_api_invalid_type(self):
        """Test formatting invalid type raises error."""
        with pytest.raises(ValueError):
            utils.format_date_for_api(12345)


@pytest.mark.unit
class TestExportUtilities:
    """Test export utility functions."""
    
    def test_export_transactions_to_csv_empty(self):
        """Test exporting empty transactions."""
        result = utils.export_transactions_to_csv({})
        assert result == ""
    
    def test_export_transactions_to_csv_string(self):
        """Test exporting transactions to CSV string."""
        # Create mock transaction
        class MockTransaction:
            def __init__(self):
                self.date = date(2025, 11, 24)
                self.payee_name = "Store"
                self.category_name = "Groceries"
                self.memo = "Shopping"
                self.amount = -50000
                self.cleared = "cleared"
                self.approved = True
                self.account_name = "Checking"
        
        transactions = {"1": MockTransaction()}
        csv_data = utils.export_transactions_to_csv(transactions)
        
        assert "date,payee_name,category_name" in csv_data
        assert "Store" in csv_data
        assert "Groceries" in csv_data
    
    def test_export_transactions_to_csv_file(self, tmp_path):
        """Test exporting transactions to CSV file."""
        class MockTransaction:
            def __init__(self):
                self.date = date(2025, 11, 24)
                self.payee_name = "Store"
                self.category_name = "Groceries"
                self.memo = "Shopping"
                self.amount = -50000
                self.cleared = "cleared"
                self.approved = True
                self.account_name = "Checking"
        
        transactions = {"1": MockTransaction()}
        file_path = tmp_path / "transactions.csv"
        
        result = utils.export_transactions_to_csv(transactions, file_path=str(file_path))
        assert result is None
        assert file_path.exists()
        
        content = file_path.read_text()
        assert "Store" in content


@pytest.mark.unit
class TestFilterTransactions:
    """Test transaction filtering utilities."""
    
    def test_filter_transactions_by_date_range(self):
        """Test filtering transactions by date range."""
        class MockTransaction:
            def __init__(self, txn_date):
                self.date = txn_date
        
        transactions = utils._dict({
            "1": MockTransaction(date(2025, 11, 1)),
            "2": MockTransaction(date(2025, 11, 15)),
            "3": MockTransaction(date(2025, 11, 30)),
            "4": MockTransaction(date(2025, 12, 1)),
        })
        
        result = utils.filter_transactions_by_date_range(
            transactions,
            start_date=date(2025, 11, 10),
            end_date=date(2025, 11, 25)
        )
        
        assert len(result) == 1
        assert "2" in result
    
    def test_filter_transactions_by_date_range_with_strings(self):
        """Test filtering with string dates."""
        class MockTransaction:
            def __init__(self, txn_date):
                self.date = txn_date
        
        transactions = utils._dict({
            "1": MockTransaction(date(2025, 11, 15)),
        })
        
        result = utils.filter_transactions_by_date_range(
            transactions,
            start_date="2025-11-01",
            end_date="2025-11-30"
        )
        
        assert len(result) == 1


@pytest.mark.unit
class TestCalculations:
    """Test calculation utility functions."""
    
    def test_calculate_net_worth(self):
        """Test calculating net worth."""
        class MockAccount:
            def __init__(self, balance, closed=False):
                self.balance = balance
                self.closed = closed
        
        class MockBudget:
            def __init__(self):
                self.accounts = utils._dict({
                    "1": MockAccount(100000),
                    "2": MockAccount(50000),
                    "3": MockAccount(-25000),
                    "4": MockAccount(10000, closed=True),
                })
        
        budget = MockBudget()
        net_worth = utils.calculate_net_worth(budget)
        assert net_worth == 125000  # 100k + 50k - 25k (closed account excluded)
    
    def test_calculate_net_worth_include_closed(self):
        """Test calculating net worth including closed accounts."""
        class MockAccount:
            def __init__(self, balance, closed=False):
                self.balance = balance
                self.closed = closed
        
        class MockBudget:
            def __init__(self):
                self.accounts = utils._dict({
                    "1": MockAccount(100000),
                    "2": MockAccount(10000, closed=True),
                })
        
        budget = MockBudget()
        net_worth = utils.calculate_net_worth(budget, include_closed=True)
        assert net_worth == 110000
    
    def test_get_spending_by_category(self):
        """Test calculating spending by category."""
        class MockTransaction:
            def __init__(self, amount, category_name):
                self.amount = amount
                self.category_name = category_name
        
        transactions = utils._dict({
            "1": MockTransaction(-50000, "Groceries"),
            "2": MockTransaction(-30000, "Groceries"),
            "3": MockTransaction(-20000, "Gas"),
            "4": MockTransaction(100000, "Income"),  # Should be excluded
        })
        
        spending = utils.get_spending_by_category(transactions)
        assert spending["Groceries"] == 80000
        assert spending["Gas"] == 20000
        assert "Income" not in spending
    
    def test_get_spending_by_payee(self):
        """Test calculating spending by payee."""
        class MockTransaction:
            def __init__(self, amount, payee_name):
                self.amount = amount
                self.payee_name = payee_name
        
        transactions = utils._dict({
            "1": MockTransaction(-50000, "Store A"),
            "2": MockTransaction(-30000, "Store A"),
            "3": MockTransaction(-20000, "Store B"),
        })
        
        spending = utils.get_spending_by_payee(transactions)
        assert spending["Store A"] == 80000
        assert spending["Store B"] == 20000


@pytest.mark.unit
class TestHttpUtilsEdgeCases:
    """Test edge cases in HTTP utilities."""
    
    @responses.activate
    def test_403_authorization_error(self, ynab_client):
        """Test 403 authorization error."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/resource",
            json={"error": {"detail": "Forbidden"}},
            status=403
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(AuthorizationError):
            http.get("/resource")
    
    @responses.activate
    def test_409_conflict_error(self, ynab_client):
        """Test 409 conflict error."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/resource",
            json={"error": {"detail": "Conflict"}},
            status=409
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(ConflictError):
            http.get("/resource")
    
    @responses.activate
    def test_error_malformed_json(self, ynab_client):
        """Test error with malformed JSON."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/resource",
            body="Not JSON",
            status=500
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(ServerError):
            http.get("/resource")
    
    @responses.activate
    def test_generic_api_error(self, ynab_client):
        """Test generic API error with custom status code."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/resource",
            json={"error": {"id": "err-123", "name": "custom_error", "detail": "Custom"}},
            status=418
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(YnabApiError) as exc_info:
            http.get("/resource")
        assert exc_info.value.status_code == 418
    
    @responses.activate
    def test_rate_limit_with_retry_after(self, ynab_client):
        """Test rate limit error with retry-after header."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/resource",
            json={"error": {"detail": "Rate limit"}},
            status=429,
            headers={"Retry-After": "60"}
        )
        
        http = utils.http_utils(ynab_py=ynab_client)
        with pytest.raises(RateLimitError) as exc_info:
            http.get("/resource")
        assert exc_info.value.retry_after == 60

