from datetime import datetime, timezone

"""
This module contains constants used in the ynab_py package.

Attributes:
    EPOCH (str): The string representation of the UTC datetime for the epoch (January 1, 1970).
    YNAB_API (str): The URL for the YNAB API.
"""

EPOCH = str(datetime(1970, 1, 1, tzinfo=timezone.utc))

YNAB_API = "https://api.ynab.com/v1"
