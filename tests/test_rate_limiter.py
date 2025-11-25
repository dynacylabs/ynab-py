"""
Tests for ynab_py.rate_limiter module.

Tests RateLimiter class for API rate limiting functionality.
"""

import pytest
import time
from unittest.mock import patch, Mock
from ynab_py.rate_limiter import RateLimiter


@pytest.mark.unit
class TestRateLimiter:
    """Test RateLimiter class."""
    
    def test_init_default_values(self):
        """Test RateLimiter initialization with defaults."""
        limiter = RateLimiter()
        assert limiter.max_requests == 180  # 200 * 0.9
        assert limiter.window_seconds == 3600
        stats = limiter.get_stats()
        assert stats["requests_used"] == 0
        assert stats["max_requests"] == 180
    
    def test_init_custom_values(self):
        """Test RateLimiter with custom values."""
        limiter = RateLimiter(requests_per_hour=100, safety_margin=0.8)
        assert limiter.max_requests == 80  # 100 * 0.8
        assert limiter.window_seconds == 3600
    
    def test_wait_if_needed_no_wait(self):
        """Test wait_if_needed when under limit."""
        limiter = RateLimiter(requests_per_hour=200)
        start_time = time.time()
        limiter.wait_if_needed()
        elapsed = time.time() - start_time
        assert elapsed < 0.1  # Should not wait
    
    def test_wait_if_needed_with_wait(self):
        """Test wait_if_needed when at limit."""
        limiter = RateLimiter(requests_per_hour=2, safety_margin=1.0)
        
        # Fill up to limit
        limiter.wait_if_needed()
        limiter.wait_if_needed()
        
        # This should trigger a wait
        with patch('time.sleep') as mock_sleep:
            limiter.wait_if_needed()
            # Should have called sleep
            assert mock_sleep.called
    
    def test_request_tracking(self):
        """Test that requests are tracked correctly."""
        limiter = RateLimiter()
        stats_before = limiter.get_stats()
        assert stats_before["requests_used"] == 0
        
        limiter.wait_if_needed()
        limiter.wait_if_needed()
        
        stats_after = limiter.get_stats()
        assert stats_after["requests_used"] == 2
        assert stats_after["requests_remaining"] == stats_after["max_requests"] - 2
    
    def test_old_requests_cleaned(self):
        """Test that old requests are cleaned from tracking."""
        limiter = RateLimiter()
        
        # Mock time to simulate passage of time
        with patch('time.time') as mock_time:
            mock_time.return_value = 1000.0
            limiter.wait_if_needed()
            
            # Advance time past window
            mock_time.return_value = 5000.0  # More than 1 hour later
            limiter.wait_if_needed()
            
            stats = limiter.get_stats()
            # Old request should be cleaned, only 1 remaining
            assert stats["requests_used"] == 1
    
    def test_get_stats(self):
        """Test get_stats returns correct information."""
        limiter = RateLimiter(requests_per_hour=100, safety_margin=0.9)
        limiter.wait_if_needed()
        limiter.wait_if_needed()
        
        stats = limiter.get_stats()
        assert stats["requests_used"] == 2
        assert stats["requests_remaining"] == 88  # 90 - 2
        assert stats["max_requests"] == 90
        assert stats["window_seconds"] == 3600
        assert 0 <= stats["usage_percentage"] <= 100
        assert stats["usage_percentage"] == pytest.approx(2.22, rel=0.1)
    
    def test_reset(self):
        """Test reset clears all tracked requests."""
        limiter = RateLimiter()
        limiter.wait_if_needed()
        limiter.wait_if_needed()
        
        stats_before = limiter.get_stats()
        assert stats_before["requests_used"] == 2
        
        limiter.reset()
        
        stats_after = limiter.get_stats()
        assert stats_after["requests_used"] == 0
    
    def test_thread_safety(self):
        """Test that rate limiter has thread safety mechanisms."""
        limiter = RateLimiter()
        assert hasattr(limiter, 'lock')
        
        # Basic operations should work
        limiter.wait_if_needed()
        stats = limiter.get_stats()
        assert stats["requests_used"] == 1
    
    def test_usage_percentage_calculation(self):
        """Test usage percentage is calculated correctly."""
        limiter = RateLimiter(requests_per_hour=10, safety_margin=1.0)
        
        stats = limiter.get_stats()
        assert stats["usage_percentage"] == 0
        
        for _ in range(5):
            limiter.wait_if_needed()
        
        stats = limiter.get_stats()
        assert stats["usage_percentage"] == 50.0
    
    def test_zero_max_requests(self):
        """Test behavior with zero max requests."""
        limiter = RateLimiter(requests_per_hour=0, safety_margin=1.0)
        stats = limiter.get_stats()
        assert stats["max_requests"] == 0
        assert stats["usage_percentage"] == 0  # Should handle division by zero
