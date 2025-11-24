from datetime import datetime, date
from enum import Enum
from ynab_py.ynab_py import YnabPy

import json
import requests
import logging


class http_utils:
    def __init__(self, ynab_py: YnabPy = None):
        """
        Initializes an instance of the class.

        Args:
            ynab_py (YnabPy, optional): The YnabPy object. Defaults to None.
        """
        self.ynab_py = ynab_py

    def get(self, endpoint: str = None):
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str, optional): The endpoint to send the request to. Defaults to None.

        Returns:
            Response: The response object returned by the GET request.
        """
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"GET {url}")
        response = requests.get(url, headers=self.ynab_py._headers)
        if "x-rate-limit" in response.headers:
            self.ynab_py._requests_remaining = int(
                response.headers["x-rate-limit"].split("/")[1]
            ) - int(response.headers["x-rate-limit"].split("/")[0])
        else:
            self.ynab_py._requests_remaining -= 1
        return response

    def post(self, endpoint: str = None, json: dict = {}):
        """
        Sends a POST request to the specified endpoint with the provided JSON data.

        Args:
            endpoint (str): The endpoint to send the request to.
            json (dict): The JSON data to include in the request body.

        Returns:
            Response: The response object received from the server.
        """
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"POST {url}\n{json}")
        response = requests.post(url, json=json, headers=self.ynab_py._headers)
        if "x-rate-limit" in response.headers:
            self.ynab_py._requests_remaining = int(
                response.headers["x-rate-limit"].split("/")[1]
            ) - int(response.headers["x-rate-limit"].split("/")[0])
        else:
            self.ynab_py._requests_remaining -= 1
        return response

    def patch(self, endpoint: str = None, json: dict = {}):
        """
        Sends a PATCH request to the specified endpoint with the provided JSON data.

        Args:
            endpoint (str, optional): The endpoint to send the PATCH request to. Defaults to None.
            json (dict, optional): The JSON data to include in the request body. Defaults to {}.

        Returns:
            Response: The response object returned by the PATCH request.
        """
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"PATCH {url}\n{json}")
        response = requests.patch(url, json=json, headers=self.ynab_py._headers)
        if "x-rate-limit" in response.headers:
            self.ynab_py._requests_remaining = int(
                response.headers["x-rate-limit"].split("/")[1]
            ) - int(response.headers["x-rate-limit"].split("/")[0])
        else:
            self.ynab_py._requests_remaining -= 1
        return response

    def put(self, endpoint: str = None, json: dict = {}):
        """
        Sends a PUT request to the specified endpoint with the given JSON payload.

        Args:
            endpoint (str): The endpoint to send the request to.
            json (dict): The JSON payload to include in the request.

        Returns:
            Response: The response object returned by the server.
        """
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.debug(f"PUT {url}\n{json}")
        response = requests.put(url, json=json, headers=self.ynab_py._headers)
        if "x-rate-limit" in response.headers:
            self.ynab_py._requests_remaining = int(
                response.headers["x-rate-limit"].split("/")[1]
            ) - int(response.headers["x-rate-limit"].split("/")[0])
        else:
            self.ynab_py._requests_remaining -= 1
        return response

    def delete(self, endpoint: str = None):
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str, optional): The endpoint to send the request to. Defaults to None.

        Returns:
            requests.Response: The response object returned by the DELETE request.
        """
        url = f"{self.ynab_py.api_url}{endpoint}"
        logging.info(f"DELETE {url}\n{json}")
        response = requests.delete(url, headers=self.ynab_py._headers)
        if "x-rate-limit" in response.headers:
            self.ynab_py._requests_remaining = int(
                response.headers["x-rate-limit"].split("/")[1]
            ) - int(response.headers["x-rate-limit"].split("/")[0])
        else:
            self.ynab_py._requests_remaining -= 1
        return response


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        Returns the default JSON representation of an object.

        Parameters:
        - obj: The object to be serialized.

        Returns:
        The JSON representation of the object.

        Note:
        - If the object is an instance of Enum, the value of the Enum is returned.
        - If the object is an instance of datetime or date, the ISO formatted string representation is returned.
        - For all other objects, the default JSONEncoder's default method is called.

        """
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)  # pragma: no cover


class _dict(dict):
    """
    A custom dictionary class that provides additional functionality.

    This class extends the built-in `dict` class and adds a `by` method
    for filtering the dictionary items based on a specific field and value.

    Attributes:
        None

    Methods:
        by(field: str = "", value: object = None, first: bool = True) -> Union[object, _dict]:
            Filters the dictionary items based on the specified field and value.

    """

    def by(self, field: str = "", value: object = None, first: bool = True):
        """
        Filters the dictionary items based on the specified field and value.

        Args:
            field (str): The name of the field to filter on.
            value (object): The value to filter for.
            first (bool): If True, returns the first matching item. If False, returns a new dictionary with all matching items.

        Returns:
            Union[object, _dict]: If `first` is True, returns the first matching item. If `first` is False, returns a new `_dict` object with all matching items.

        """
        items = _dict()
        for k, v in self.items():
            if getattr(v, field, None) == value:
                if first:
                    return v
                else:
                    items[k] = v
        return items
