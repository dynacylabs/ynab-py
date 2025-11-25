from typing import Optional, Dict
import logging

from ynab_py.api import Api
from ynab_py import constants
from ynab_py.rate_limiter import RateLimiter
from ynab_py.cache import Cache

logger = logging.getLogger(__name__)


class YnabPy:
    def __init__(
        self,
        bearer: Optional[str] = None,
        enable_rate_limiting: bool = True,
        enable_caching: bool = True,
        cache_ttl: int = 300,
        log_level: Optional[str] = None
    ):
        """
        Initialize the YNAB API client.

        Args:
            bearer: The bearer token for authentication
            enable_rate_limiting: Enable automatic rate limiting (default: True)
            enable_caching: Enable response caching (default: True)
            cache_ttl: Default cache time-to-live in seconds (default: 300)
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
            
        Raises:
            ValueError: If bearer token is not provided
            
        Example:
            >>> ynab = YnabPy(
            ...     bearer="your_token",
            ...     enable_caching=True,
            ...     cache_ttl=600
            ... )
        """
        if not bearer:
            raise ValueError("Bearer token is required. Get one from https://app.ynab.com/settings")
        
        # Configure logging if level specified
        if log_level:
            logging.basicConfig(
                level=getattr(logging, log_level.upper()),
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        
        self.api_url = constants.YNAB_API

        self._bearer = bearer
        self._fetch = True
        self._track_server_knowledge = False

        self._requests_remaining = 0
        self._headers: Dict[str, str] = {
            "Authorization": f"Bearer {self._bearer}",
            "accept": "application/json",
        }

        self._server_knowledges: Dict[str, int] = {
            "get_budget": 0,
            "get_accounts": 0,
            "get_categories": 0,
            "get_months": 0,
            "get_transactions": 0,
            "get_account_transactions": 0,
            "get_category_transactions": 0,
            "get_payee_transactions": 0,
            "get_month_transactions": 0,
            "get_scheduled_transactions": 0,
        }
        
        # Initialize rate limiter
        self._rate_limiter: Optional[RateLimiter] = None
        if enable_rate_limiting:
            self._rate_limiter = RateLimiter()
            logger.info("Rate limiting enabled")
        
        # Initialize cache
        self._cache: Optional[Cache] = None
        if enable_caching:
            self._cache = Cache(default_ttl=cache_ttl)
            logger.info(f"Caching enabled with TTL={cache_ttl}s")

        self.api = Api(ynab_py=self)
        logger.info("YnabPy initialized successfully")

    def server_knowledges(self, endpoint: Optional[str] = None) -> int:
        """
        Retrieves the server knowledge for a specific endpoint.
        
        Server knowledge is used for delta syncing with YNAB API.

        Args:
            endpoint: The endpoint for which to retrieve the server knowledge

        Returns:
            The server knowledge for the specified endpoint. If server knowledge 
            tracking is disabled, returns 0.
        """
        if self._track_server_knowledge and endpoint:
            return self._server_knowledges.get(endpoint, 0)
        return 0
    
    def get_rate_limit_stats(self) -> Dict:
        """
        Get rate limiter statistics.
        
        Returns:
            Dictionary with rate limit usage statistics
        """
        if self._rate_limiter:
            return self._rate_limiter.get_stats()
        return {"enabled": False}
    
    def get_cache_stats(self) -> Dict:
        """
        Get cache statistics.
        
        Returns:
            Dictionary with cache usage statistics
        """
        if self._cache:
            return self._cache.get_stats()
        return {"enabled": False}
    
    def clear_cache(self) -> None:
        """
        Clear all cached API responses.
        """
        if self._cache:
            self._cache.clear()
            logger.info("Cache cleared")

    @property
    def user(self):
        """
        Retrieves the user information from the API.

        Returns:
            dict: A dictionary containing the user information.
        """
        return self.api.get_user()

    @property
    def budgets(self):
        """
        Retrieves the budgets from the API.

        Returns:
            list: A list of budgets.
        """
        return self.api.get_budgets()
