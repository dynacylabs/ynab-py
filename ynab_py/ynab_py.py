from ynab_py.api import Api
from ynab_py import constants


class YnabPy:
    def __init__(self, bearer: str = None):
        """
        Initializes a new instance of the `ynab_py` class.

        Args:
            bearer (str, optional): The bearer token for authentication. Defaults to None.
        """
        self.api_url = constants.YNAB_API

        self._bearer = bearer
        self._fetch = True
        self._track_server_knowledge = False

        self._requests_remaining = 0
        self._headers = {
            "Authorization": f"Bearer {self._bearer}",
            "accept": "application/json",
        }

        self._server_knowledges = {
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

        self.api = Api(ynab_py=self)

    def server_knowledges(self, endpoint: str = None):
        """
        Retrieves the server knowledge for a specific endpoint.

        Parameters:
            endpoint (str): The endpoint for which to retrieve the server knowledge. If not provided, the default value is None.

        Returns:
            int: The server knowledge for the specified endpoint. If server knowledge tracking is disabled, returns 0.
        """
        if self._track_server_knowledge:
            return self._server_knowledges[endpoint]
        else:
            return 0

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
