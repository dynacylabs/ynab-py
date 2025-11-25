"""
Tests for ynab_py.cache module.

Tests Cache, CacheEntry, and cached decorator functionality.
"""

import pytest
import time
from unittest.mock import Mock, patch
from ynab_py.cache import Cache, CacheEntry, cache_key, cached


@pytest.mark.unit
class TestCacheEntry:
    """Test CacheEntry class."""
    
    def test_init_with_ttl(self):
        """Test CacheEntry initialization with TTL."""
        entry = CacheEntry("test_value", ttl=60)
        assert entry.value == "test_value"
        assert entry.expiry > time.time()
        assert entry.expiry <= time.time() + 60
    
    def test_init_with_zero_ttl(self):
        """Test CacheEntry with TTL of 0 never expires."""
        entry = CacheEntry("test_value", ttl=0)
        assert entry.value == "test_value"
        assert entry.expiry == float('inf')
        assert not entry.is_expired()
    
    def test_is_expired_false(self):
        """Test entry that hasn't expired."""
        entry = CacheEntry("test", ttl=60)
        assert not entry.is_expired()
    
    def test_is_expired_true(self):
        """Test entry that has expired."""
        entry = CacheEntry("test", ttl=0.01)
        time.sleep(0.02)
        assert entry.is_expired()


@pytest.mark.unit
class TestCache:
    """Test Cache class."""
    
    def test_init_default_values(self):
        """Test Cache initialization with defaults."""
        cache = Cache()
        assert cache.max_size == 100
        assert cache.default_ttl == 300
        stats = cache.get_stats()
        assert stats["size"] == 0
        assert stats["max_size"] == 100
    
    def test_init_custom_values(self):
        """Test Cache initialization with custom values."""
        cache = Cache(max_size=50, default_ttl=600)
        assert cache.max_size == 50
        assert cache.default_ttl == 600
    
    def test_set_and_get(self):
        """Test setting and getting values."""
        cache = Cache()
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"
    
    def test_get_nonexistent_key(self):
        """Test getting a key that doesn't exist."""
        cache = Cache()
        assert cache.get("nonexistent") is None
    
    def test_get_expired_entry(self):
        """Test getting an expired entry returns None."""
        cache = Cache()
        cache.set("key1", "value1", ttl=0.01)
        time.sleep(0.02)
        assert cache.get("key1") is None
    
    def test_set_updates_existing(self):
        """Test setting an existing key updates it."""
        cache = Cache()
        cache.set("key1", "value1")
        cache.set("key1", "value2")
        assert cache.get("key1") == "value2"
    
    def test_lru_eviction(self):
        """Test LRU eviction when max size is reached."""
        cache = Cache(max_size=3)
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")
        cache.set("key4", "value4")  # Should evict key1
        assert cache.get("key1") is None
        assert cache.get("key2") == "value2"
        assert cache.get("key3") == "value3"
        assert cache.get("key4") == "value4"
    
    def test_lru_reordering_on_get(self):
        """Test that getting a value moves it to end (most recent)."""
        cache = Cache(max_size=3)
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")
        
        # Access key1 to make it most recent
        cache.get("key1")
        
        # Add key4, should evict key2 (now least recent)
        cache.set("key4", "value4")
        assert cache.get("key1") == "value1"
        assert cache.get("key2") is None
        assert cache.get("key3") == "value3"
        assert cache.get("key4") == "value4"
    
    def test_delete(self):
        """Test deleting a key."""
        cache = Cache()
        cache.set("key1", "value1")
        cache.delete("key1")
        assert cache.get("key1") is None
    
    def test_delete_nonexistent(self):
        """Test deleting a nonexistent key doesn't error."""
        cache = Cache()
        cache.delete("nonexistent")  # Should not raise
    
    def test_clear(self):
        """Test clearing the cache."""
        cache = Cache()
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.clear()
        assert cache.get("key1") is None
        assert cache.get("key2") is None
        stats = cache.get_stats()
        assert stats["size"] == 0
    
    def test_get_stats(self):
        """Test getting cache statistics."""
        cache = Cache(max_size=10)
        cache.set("key1", "value1")
        cache.get("key1")  # Hit
        cache.get("key2")  # Miss
        
        stats = cache.get_stats()
        assert stats["size"] == 1
        assert stats["max_size"] == 10
        assert stats["hits"] >= 1
        assert stats["misses"] >= 1
        assert stats["total_requests"] >= 2
        assert 0 <= stats["hit_rate_percent"] <= 100
    
    def test_thread_safety(self):
        """Test basic thread safety with lock."""
        cache = Cache()
        # Basic check that lock exists and is used
        assert hasattr(cache, '_lock')
        
        # Set and get should work (using lock internally)
        cache.set("key", "value")
        assert cache.get("key") == "value"


@pytest.mark.unit
class TestCacheKeyFunction:
    """Test cache_key helper function."""
    
    def test_empty_args(self):
        """Test cache_key with no arguments."""
        key = cache_key()
        assert key == ""
    
    def test_with_args(self):
        """Test cache_key with positional arguments."""
        key = cache_key("budget-123", "account-456")
        assert key == "budget-123:account-456"
    
    def test_with_kwargs(self):
        """Test cache_key with keyword arguments."""
        key = cache_key(budget_id="budget-123", account_id="account-456")
        assert "budget_id=budget-123" in key
        assert "account_id=account-456" in key
    
    def test_with_mixed_args(self):
        """Test cache_key with both args and kwargs."""
        key = cache_key("budget-123", account_id="account-456")
        assert "budget-123" in key
        assert "account_id=account-456" in key
    
    def test_filters_none_values(self):
        """Test that None values are filtered out."""
        key = cache_key("budget-123", None, account_id="account-456", other=None)
        assert "budget-123" in key
        assert "account_id=account-456" in key
        assert "None" not in key


@pytest.mark.unit
class TestCachedDecorator:
    """Test cached decorator."""
    
    def test_caches_result(self):
        """Test that decorator caches function results."""
        cache = Cache()
        call_count = 0
        
        @cached(cache, ttl=60)
        def expensive_function(x):
            nonlocal call_count
            call_count += 1
            return x * 2
        
        result1 = expensive_function(5)
        result2 = expensive_function(5)
        
        assert result1 == 10
        assert result2 == 10
        assert call_count == 1  # Function only called once
    
    def test_different_args_not_cached(self):
        """Test that different arguments aren't cached together."""
        cache = Cache()
        call_count = 0
        
        @cached(cache)
        def func(x):
            nonlocal call_count
            call_count += 1
            return x * 2
        
        func(5)
        func(10)
        
        assert call_count == 2  # Called twice for different args
    
    def test_key_prefix(self):
        """Test key_prefix parameter."""
        cache = Cache()
        
        @cached(cache, key_prefix="test_prefix")
        def func(x):
            return x * 2
        
        result = func(5)
        assert result == 10
        # Check that cache has an entry with the prefix
        stats = cache.get_stats()
        assert stats["size"] == 1
    
    def test_custom_ttl(self):
        """Test custom TTL parameter."""
        cache = Cache()
        
        @cached(cache, ttl=0.01)
        def func(x):
            return x * 2
        
        result1 = func(5)
        time.sleep(0.02)
        
        # After TTL expires, function should be called again
        call_count = 0
        
        @cached(cache, ttl=0.01)
        def func2(x):
            nonlocal call_count
            call_count += 1
            return x * 2
        
        func2(5)
        time.sleep(0.02)
        func2(5)
        assert call_count == 2  # Called twice due to expiry
