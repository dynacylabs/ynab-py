"""
Caching functionality for ynab-py library.

Provides LRU cache with TTL (time-to-live) for API responses
to reduce unnecessary API calls and improve performance.
"""

import time
import threading
from typing import Any, Optional, Callable, Tuple
from functools import wraps
import logging

logger = logging.getLogger(__name__)


class CacheEntry:
    """Represents a cached value with expiration time."""
    
    def __init__(self, value: Any, ttl: int):
        """
        Create a cache entry.
        
        Args:
            value: The value to cache
            ttl: Time-to-live in seconds
        """
        self.value = value
        self.expiry = time.time() + ttl if ttl > 0 else float('inf')
    
    def is_expired(self) -> bool:
        """Check if this cache entry has expired."""
        return time.time() > self.expiry


class Cache:
    """
    Thread-safe LRU cache with TTL support.
    
    This cache automatically evicts expired entries and enforces
    a maximum size limit using LRU (Least Recently Used) policy.
    """
    
    def __init__(self, max_size: int = 100, default_ttl: int = 300):
        """
        Initialize the cache.
        
        Args:
            max_size: Maximum number of entries (default: 100)
            default_ttl: Default time-to-live in seconds (default: 300 = 5 minutes)
        """
        self.max_size = max_size
        self.default_ttl = default_ttl
        self._cache = {}
        self._access_order = []
        self._lock = threading.Lock()
        self._hits = 0
        self._misses = 0
        logger.info(f"Cache initialized: max_size={max_size}, default_ttl={default_ttl}s")
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from cache if it exists and hasn't expired.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value if found and not expired, None otherwise
        """
        with self._lock:
            if key not in self._cache:
                self._misses += 1
                logger.debug(f"Cache miss: {key}")
                return None
            
            entry = self._cache[key]
            if entry.is_expired():
                del self._cache[key]
                self._access_order.remove(key)
                self._misses += 1
                logger.debug(f"Cache expired: {key}")
                return None
            
            # Move to end (most recently used)
            self._access_order.remove(key)
            self._access_order.append(key)
            self._hits += 1
            logger.debug(f"Cache hit: {key}")
            return entry.value
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Store a value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (uses default_ttl if None)
        """
        with self._lock:
            if ttl is None:
                ttl = self.default_ttl
            
            # Remove if already exists
            if key in self._cache:
                self._access_order.remove(key)
            
            # Evict LRU entry if at max size
            if len(self._cache) >= self.max_size and key not in self._cache:
                lru_key = self._access_order.pop(0)
                del self._cache[lru_key]
                logger.debug(f"Cache evicted (LRU): {lru_key}")
            
            self._cache[key] = CacheEntry(value, ttl)
            self._access_order.append(key)
            logger.debug(f"Cache stored: {key} (ttl={ttl}s)")
    
    def delete(self, key: str) -> None:
        """
        Remove a specific key from cache.
        
        Args:
            key: Cache key to remove
        """
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                self._access_order.remove(key)
                logger.debug(f"Cache deleted: {key}")
    
    def clear(self) -> None:
        """Clear all cached entries."""
        with self._lock:
            self._cache.clear()
            self._access_order.clear()
            logger.info("Cache cleared")
    
    def get_stats(self) -> dict:
        """
        Get cache statistics.
        
        Returns:
            Dictionary with cache statistics
        """
        with self._lock:
            total_requests = self._hits + self._misses
            hit_rate = (self._hits / total_requests * 100) if total_requests > 0 else 0
            return {
                "size": len(self._cache),
                "max_size": self.max_size,
                "hits": self._hits,
                "misses": self._misses,
                "total_requests": total_requests,
                "hit_rate_percent": hit_rate
            }


def cache_key(*args, **kwargs) -> str:
    """
    Generate a cache key from function arguments.
    
    Args:
        *args: Positional arguments
        **kwargs: Keyword arguments
        
    Returns:
        String cache key
    """
    # Convert args to strings
    key_parts = [str(arg) for arg in args if arg is not None]
    
    # Add kwargs sorted by key
    for k in sorted(kwargs.keys()):
        v = kwargs[k]
        if v is not None:
            key_parts.append(f"{k}={v}")
    
    return ":".join(key_parts)


def cached(cache_instance: Cache, ttl: Optional[int] = None, key_prefix: str = ""):
    """
    Decorator to cache function results.
    
    Args:
        cache_instance: Cache instance to use
        ttl: Time-to-live for cached result (uses cache default if None)
        key_prefix: Prefix to add to cache key
        
    Returns:
        Decorated function
        
    Example:
        @cached(my_cache, ttl=300, key_prefix="budgets")
        def get_budget(budget_id):
            return fetch_budget(budget_id)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key
            key = f"{key_prefix}:{func.__name__}:{cache_key(*args, **kwargs)}"
            
            # Try to get from cache
            cached_value = cache_instance.get(key)
            if cached_value is not None:
                return cached_value
            
            # Call function and cache result
            result = func(*args, **kwargs)
            cache_instance.set(key, result, ttl)
            return result
        
        return wrapper
    return decorator
