"""
Configuration for test modes (mock vs live API).

Set YNAB_TEST_MODE environment variable:
- 'mock' (default): Use mocked responses
- 'live': Use real API calls (requires YNAB_API_TOKEN)
"""

import os
import pytest

# Test mode configuration
TEST_MODE = os.environ.get("YNAB_TEST_MODE", "mock").lower()
LIVE_API_TOKEN = os.environ.get("YNAB_API_TOKEN", None)

# Skip live API tests if token not provided
skip_if_no_token = pytest.mark.skipif(
    TEST_MODE == "live" and not LIVE_API_TOKEN,
    reason="Live API tests require YNAB_API_TOKEN environment variable"
)

skip_if_mock_mode = pytest.mark.skipif(
    TEST_MODE == "mock",
    reason="Test only runs in live API mode"
)

skip_if_live_mode = pytest.mark.skipif(
    TEST_MODE == "live",
    reason="Test only runs in mock mode"
)


def is_live_mode():
    """Check if tests are running in live API mode."""
    return TEST_MODE == "live" and LIVE_API_TOKEN is not None


def is_mock_mode():
    """Check if tests are running in mock mode."""
    return TEST_MODE == "mock"
