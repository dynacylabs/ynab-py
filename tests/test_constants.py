"""
Tests for ynab_py.constants module.
"""

import pytest
from datetime import datetime, timezone
from ynab_py import constants


@pytest.mark.unit
class TestConstants:
    """Test module constants."""
    
    def test_epoch_constant(self):
        """Test EPOCH constant is correct."""
        assert constants.EPOCH == str(datetime(1970, 1, 1, tzinfo=timezone.utc))
        # Verify it's parseable
        dt = datetime.fromisoformat(constants.EPOCH.replace('+00:00', '+00:00'))
        assert dt.year == 1970
        assert dt.month == 1
        assert dt.day == 1
    
    def test_ynab_api_constant(self):
        """Test YNAB_API constant is correct."""
        assert constants.YNAB_API == "https://api.ynab.com/v1"
        assert constants.YNAB_API.startswith("https://")
        assert "api.ynab.com" in constants.YNAB_API
        assert constants.YNAB_API.endswith("/v1")
