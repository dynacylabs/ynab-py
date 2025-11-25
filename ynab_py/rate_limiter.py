"""
Rate limiting functionality for YNAB API.

YNAB API allows 200 requests per hour per access token.
This module helps prevent exceeding the rate limit.
"""

import time
import threading
from collections import deque
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class RateLimiter:
    """
    Token bucket rate limiter for YNAB API.
    
    YNAB allows 200 requests per hour. This implements a sliding window
    rate limiter to track requests and prevent exceeding the limit.
    """
    
    def __init__(self, requests_per_hour: int = 200, safety_margin: float = 0.9):
        """
        Initialize the rate limiter.
        
        Args:
            requests_per_hour: Maximum requests allowed per hour (default: 200)
            safety_margin: Fraction of limit to use (default: 0.9 = 90%)
                          This provides a safety buffer
        """
        self.max_requests = int(requests_per_hour * safety_margin)
        self.window_seconds = 3600  # 1 hour
        self.requests = deque()
        self.lock = threading.Lock()
        logger.info(f"Rate limiter initialized: {self.max_requests} requests per hour")
    
    def _clean_old_requests(self, current_time: float) -> None:
        """Remove requests older than the time window."""
        cutoff_time = current_time - self.window_seconds
        while self.requests and self.requests[0] < cutoff_time:
            self.requests.popleft()
    
    def wait_if_needed(self) -> None:
        """
        Block if necessary to respect rate limits.
        
        This method will sleep if the rate limit would be exceeded.
        """
        with self.lock:
            current_time = time.time()
            self._clean_old_requests(current_time)
            
            if len(self.requests) >= self.max_requests:
                # Calculate how long to wait
                oldest_request = self.requests[0]
                wait_time = oldest_request + self.window_seconds - current_time
                if wait_time > 0:
                    logger.warning(
                        f"Rate limit approaching. Waiting {wait_time:.1f} seconds. "
                        f"({len(self.requests)}/{self.max_requests} requests used)"
                    )
                    time.sleep(wait_time)
                    current_time = time.time()
                    self._clean_old_requests(current_time)
            
            self.requests.append(current_time)
            logger.debug(f"Request recorded. {len(self.requests)}/{self.max_requests} requests used")
    
    def get_stats(self) -> dict:
        """
        Get current rate limiter statistics.
        
        Returns:
            Dictionary with usage statistics
        """
        with self.lock:
            current_time = time.time()
            self._clean_old_requests(current_time)
            return {
                "requests_used": len(self.requests),
                "requests_remaining": self.max_requests - len(self.requests),
                "max_requests": self.max_requests,
                "window_seconds": self.window_seconds,
                "usage_percentage": (len(self.requests) / self.max_requests * 100) if self.max_requests > 0 else 0
            }
    
    def reset(self) -> None:
        """Reset the rate limiter (clear all tracked requests)."""
        with self.lock:
            self.requests.clear()
            logger.info("Rate limiter reset")
