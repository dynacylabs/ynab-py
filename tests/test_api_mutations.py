"""
Tests for API create/update/delete operations.
Tests basic error handling for mutation operations.
"""

import pytest
import responses

from ynab_py import YnabPy
from ynab_py import constants


class TestApiImportTransactions:
    """Test transaction import operations."""

    @responses.activate
    def test_import_transactions(self, mock_bearer_token):
        """Test importing transactions."""
        responses.add(
            responses.POST,
            f"{constants.YNAB_API}/budgets/last-used/transactions/import",
            json={
                "data": {
                    "transaction_ids": ["txn-1", "txn-2"]
                }
            },
            status=201
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        result = client.api.import_transactions()
        assert result is not None

    @responses.activate
    def test_import_transactions_error(self, mock_bearer_token):
        """Test import_transactions handles error responses."""
        from ynab_py.exceptions import YnabApiError
        
        responses.add(
            responses.POST,
            f"{constants.YNAB_API}/budgets/last-used/transactions/import",
            json={
                "error": {
                    "id": "400",
                    "name": "bad_request",
                    "detail": "Import failed"
                }
            },
            status=400
        )
        
        client = YnabPy(bearer=mock_bearer_token)
        
        with pytest.raises(YnabApiError):
            client.api.import_transactions()
