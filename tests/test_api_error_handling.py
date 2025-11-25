"""
Tests for API error handling and edge cases.
Covers uncovered lines in api.py.
"""

import pytest
import responses

from ynab_py import YnabPy
from ynab_py import constants
from ynab_py import schemas


class TestApiErrorHandling:
    """Test error handling in API methods."""

    @responses.activate
    def test_get_user_error_response(self, mock_bearer_token):
        """Test get_user handles error responses."""
        from ynab_py.exceptions import AuthenticationError
        
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/user",
            json={
                "error": {
                    "id": "401",
                    "name": "unauthorized",
                    "detail": "Unauthorized"
                }
            },
            status=401
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(AuthenticationError):
            client.api.get_user()

    @responses.activate
    def test_get_budgets_error_response(self, mock_bearer_token):
        """Test get_budgets handles error responses."""
        from ynab_py.exceptions import ServerError
        
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets",
            json={
                "error": {
                    "id": "500",
                    "name": "internal_error",
                    "detail": "Internal server error"
                }
            },
            status=500
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(ServerError):
            client.api.get_budgets()

    @responses.activate
    def test_get_budget_error_response(self, mock_bearer_token):
        """Test get_budget handles error responses."""
        from ynab_py.exceptions import NotFoundError
        
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Budget not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(NotFoundError):
            client.api.get_budget()

    @responses.activate
    def test_get_accounts_error_response(self, mock_bearer_token):
        """Test get_accounts handles error responses."""
        from ynab_py.exceptions import AuthorizationError
        
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/accounts",
            json={
                "error": {
                    "id": "403",
                    "name": "forbidden",
                    "detail": "Access forbidden"
                }
            },
            status=403
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(AuthorizationError):
            client.api.get_accounts()

    @responses.activate
    def test_get_account_error_response(self, mock_bearer_token):
        """Test get_account handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/accounts/account-123",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Account not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception) as exc_info:
            client.api.get_account(account_id="account-123")


class TestApiGetCategories:
    """Test get_categories and related methods."""

    @responses.activate
    def test_get_categories_error_response(self, mock_bearer_token):
        """Test get_categories handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/categories",
            json={
                "error": {
                    "id": "500",
                    "name": "error",
                    "detail": "Server error"
                }
            },
            status=500
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_categories()

    @responses.activate
    def test_get_category_error_response(self, mock_bearer_token):
        """Test get_category handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/categories/cat-123",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Category not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_category(category_id="cat-123")


class TestApiGetPayees:
    """Test get_payees and related methods."""

    @responses.activate
    def test_get_payees_error_response(self, mock_bearer_token):
        """Test get_payees handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/payees",
            json={
                "error": {
                    "id": "500",
                    "name": "error",
                    "detail": "Server error"
                }
            },
            status=500
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_payees()

    @responses.activate
    def test_get_payee_error_response(self, mock_bearer_token):
        """Test get_payee handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/payees/payee-123",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Payee not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_payee(payee_id="payee-123")


class TestApiGetMonths:
    """Test get_months and related methods."""

    @responses.activate
    def test_get_months_error_response(self, mock_bearer_token):
        """Test get_months handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/months",
            json={
                "error": {
                    "id": "500",
                    "name": "error",
                    "detail": "Server error"
                }
            },
            status=500
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_months()

    @responses.activate
    def test_get_month_error_response(self, mock_bearer_token):
        """Test get_month handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/months/2025-11-01",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Month not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_month(month="2025-11-01")


class TestApiGetTransactions:
    """Test transaction retrieval error handling."""

    @responses.activate
    def test_get_transactions_error_response(self, mock_bearer_token):
        """Test get_transactions handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/transactions",
            json={
                "error": {
                    "id": "500",
                    "name": "error",
                    "detail": "Server error"
                }
            },
            status=500
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_transactions()

    @responses.activate
    def test_get_transaction_error_response(self, mock_bearer_token):
        """Test get_transaction handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/transactions/txn-123",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Transaction not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_transaction(transaction_id="txn-123")

    @responses.activate
    def test_get_account_transactions_error_response(self, mock_bearer_token):
        """Test get_account_transactions handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/accounts/account-123/transactions",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Account not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_account_transactions(account_id="account-123")

    @responses.activate
    def test_get_category_transactions_error_response(self, mock_bearer_token):
        """Test get_category_transactions handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/categories/cat-123/transactions",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Category not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_category_transactions(category_id="cat-123")

    @responses.activate
    def test_get_payee_transactions_error_response(self, mock_bearer_token):
        """Test get_payee_transactions handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/payees/payee-123/transactions",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Payee not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_payee_transactions(payee_id="payee-123")

    @responses.activate
    def test_get_month_transactions_error_response(self, mock_bearer_token):
        """Test get_month_transactions handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/months/2025-11-01/transactions",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Month not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_month_transactions(month="2025-11-01")


class TestApiScheduledTransactions:
    """Test scheduled transaction error handling."""

    @responses.activate
    def test_get_scheduled_transactions_error_response(self, mock_bearer_token):
        """Test get_scheduled_transactions handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/scheduled_transactions",
            json={
                "error": {
                    "id": "500",
                    "name": "error",
                    "detail": "Server error"
                }
            },
            status=500
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_scheduled_transactions()

    @responses.activate
    def test_get_scheduled_transaction_error_response(self, mock_bearer_token):
        """Test get_scheduled_transaction handles error responses."""
        responses.add(
            responses.GET,
            f"{constants.YNAB_API}/budgets/last-used/scheduled_transactions/scheduled-123",
            json={
                "error": {
                    "id": "404",
                    "name": "not_found",
                    "detail": "Scheduled transaction not found"
                }
            },
            status=404
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        with pytest.raises(Exception):
            client.api.get_scheduled_transaction(scheduled_transaction_id="scheduled-123")
