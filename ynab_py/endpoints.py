import ynab_py.utils as utils
from ynab_py.ynab_py import YnabPy


class Endpoints:

    def __init__(self, ynab_py: YnabPy = None):
        """
        Initializes an instance of the endpoints class.

        Parameters:
        - ynab_py (YnabPy): An instance of the YnabPy class.

        Returns:
        - None
        """
        self.ynab_py = ynab_py
        self.http_utils = utils.http_utils(ynab_py=self.ynab_py)

    # GET /user
    def request_get_user(self):
        """
        Sends a GET request to retrieve user information.

        Returns:
            The response from the GET request.
        """
        endpoint = f"/user"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets
    def request_get_budgets(self, include_accounts: bool = False):
        """
        Sends a GET request to retrieve budgets.

        Args:
            include_accounts (bool, optional): Whether to include accounts in the response. Defaults to False.

        Returns:
            dict: The response from the API.

        Raises:
            None
        """
        endpoint = f"/budgets"
        if include_accounts:
            endpoint += "?include_accounts=true"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}
    def request_get_budget(
        self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
    ):
        """
        Retrieves the budget information from the server.

        Args:
            budget_id (str, optional): The ID of the budget to retrieve. Defaults to "last-used".
            last_knowledge_of_server (int, optional): The knowledge of the server to determine if the budget has been updated. Defaults to 0.

        Returns:
            dict: The budget information.

        Raises:
            HTTPException: If an error occurs during the HTTP request.
        """
        endpoint = f"/budgets/{budget_id}"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/settings
    def request_get_budget_settings(self, budget_id: str = "last-used"):
        """
        Retrieves the budget settings for the specified budget ID.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            dict: The budget settings.

        Raises:
            HTTPError: If an HTTP error occurs.
        """
        endpoint = f"/budgets/{budget_id}/settings"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/accounts
    def request_get_accounts(
        self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
    ):
        """
        Retrieves the accounts associated with a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The response from the HTTP GET request.
        """
        endpoint = f"/budgets/{budget_id}/accounts"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # POST /budgets/{budget_id}/accounts
    def request_create_account(
        self, budget_id: str = "last-used", request_body: str = None
    ):
        """
        Creates a new account in the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget to create the account in. Defaults to "last-used".
            request_body (str, optional): The JSON request body containing the account details. Defaults to None.

        Returns:
            The response from the API call.
        """
        endpoint = f"/budgets/{budget_id}/accounts"
        return self.http_utils.post(endpoint=endpoint, json=request_body)

    # GET /budgets/{budget_id}/accounts/{account_id}
    def request_get_account(self, budget_id: str = "last-used", account_id: str = None):
        """
        Retrieves information about a specific account in a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            account_id (str, optional): The ID of the account. If not provided, information about all accounts will be returned.

        Returns:
            dict: A dictionary containing the account information.

        Raises:
            HTTPException: If the request fails or the account is not found.
        """
        endpoint = f"/budgets/{budget_id}/accounts/{account_id}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/categories
    def request_get_categories(
        self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
    ):
        """
        Retrieves the categories for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The response from the HTTP GET request.
        """
        endpoint = f"/budgets/{budget_id}/categories"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/categories/{category_id}
    def request_get_category(
        self, budget_id: str = "last-used", category_id: str = None
    ):
        """
        Retrieves a specific category from a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            category_id (str, optional): The ID of the category. If not provided, retrieves all categories.

        Returns:
            dict: The category information.

        Raises:
            HTTPError: If the request fails.
        """
        endpoint = f"/budgets/{budget_id}/categories/{category_id}"
        return self.http_utils.get(endpoint=endpoint)

    # PATCH /budgets/{budget_id}/categories/{category_id}
    def request_update_category(
        self,
        budget_id: str = "last-used",
        category_id: str = None,
        request_body: str = None,
    ):
        """
        Sends a PATCH request to update a category in the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            category_id (str, optional): The ID of the category to update.
            request_body (str, optional): The JSON request body containing the updated category data.

        Returns:
            The response from the PATCH request.

        Raises:
            None.
        """
        endpoint = f"/budgets/{budget_id}/categories/{category_id}"
        return self.http_utils.patch(endpoint=endpoint, json=request_body)

    # GET /budgets/{budget_id}/months/{month}/categories/{category_id}
    def request_get_category_for_month(
        self,
        budget_id: str = "last-used",
        month: str = "current",
        category_id: str = None,
    ):
        """
        Retrieves the category for a specific month in a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month (str, optional): The month to retrieve the category for. Defaults to "current".
            category_id (str, optional): The ID of the category. Defaults to None.

        Returns:
            The response from the API call.
        """
        endpoint = f"/budgets/{budget_id}/months/{month}/categories/{category_id}"
        return self.http_utils.get(endpoint=endpoint)

    # PATCH /budgets/{budget_id}/months/{month}/categories/{category_id}
    def request_update_category_for_month(
        self,
        budget_id: str = "last-used",
        month_id: str = "current",
        category_id: str = None,
        request_body: str = None,
    ):
        """
        Sends a PATCH request to update a category for a specific month in a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month_id (str, optional): The ID of the month. Defaults to "current".
            category_id (str, optional): The ID of the category to update.
            request_body (str, optional): The JSON request body.

        Returns:
            The response from the PATCH request.
        """
        endpoint = f"/budgets/{budget_id}/months/{month_id}/categories/{category_id}"
        return self.http_utils.patch(endpoint=endpoint, json=request_body)

    # GET /budgets/{budget_id}/payees
    def request_get_payees(
        self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
    ):
        """
        Retrieves the payees for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The response from the HTTP GET request.
        """
        endpoint = f"/budgets/{budget_id}/payees"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/payees/{payee_id}
    def request_get_payee(self, budget_id: str = "last-used", payee_id: str = None):
        """
        Retrieves a specific payee from the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee_id (str, optional): The ID of the payee. If not provided, all payees will be returned.

        Returns:
            dict: The payee information.

        Raises:
            HTTPError: If the request fails.
        """
        endpoint = f"/budgets/{budget_id}/payees/{payee_id}"
        return self.http_utils.get(endpoint=endpoint)

    # PATCH /budgets/{budget_id}/payees/{payee_id}
    def request_update_payee(
        self,
        budget_id: str = "last-used",
        payee_id: str = None,
        request_body: str = None,
    ):
        """
        Sends a PATCH request to update a payee.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee_id (str, optional): The ID of the payee to update.
            request_body (str, optional): The JSON request body.

        Returns:
            The response from the PATCH request.
        """
        endpoint = f"/budgets/{budget_id}/payees/{payee_id}"
        return self.http_utils.patch(endpoint=endpoint, json=request_body)

    # GET /budgets/{budget_id}/payee_locations
    def request_get_all_payee_locations(self, budget_id: str = "last-used"):
        """
        Retrieves all payee locations for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            dict: A dictionary containing the response data.

        Raises:
            None
        """
        endpoint = f"/budgets/{budget_id}/payee_locations"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/payee_locations/{payee_location_id}
    def request_get_payee_location(
        self, budget_id: str = "last-used", payee_location_id: str = None
    ):
        """
        Retrieves a specific payee location from the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee_location_id (str, optional): The ID of the payee location. Defaults to None.

        Returns:
            dict: The payee location information.

        Raises:
            HTTPError: If the request fails.
        """
        endpoint = f"/budgets/{budget_id}/payee_locations/{payee_location_id}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/payees/{payee_id}/payee_locations
    def request_get_payee_locations(
        self, budget_id: str = "last-used", payee_id: str = None
    ):
        """
        Retrieves the payee locations for a specific payee in a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee_id (str, optional): The ID of the payee. Defaults to None.

        Returns:
            dict: The payee locations for the specified payee in the budget.
        """
        endpoint = f"/budgets/{budget_id}/payees/{payee_id}/payee_locations"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/months
    def request_get_months(
        self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
    ):
        """
        Retrieves the months for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The response from the server.
        """
        endpoint = f"/budgets/{budget_id}/months"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/months/{month}
    def request_get_month(
        self, budget_id: str = "last-used", month_id: str = "current"
    ):
        """
        Retrieves the details of a specific month in a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month_id (str, optional): The ID of the month. Defaults to "current".

        Returns:
            dict: The details of the requested month.

        Raises:
            HTTPError: If the request fails.
        """
        endpoint = f"/budgets/{budget_id}/months/{month_id}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/transactions
    def request_get_transactions(
        self,
        budget_id: str = "last-used",
        since_date: str = None,
        type: str = None,
        last_knowledge_of_server: int = 0,
    ):
        """
        Sends a GET request to retrieve transactions from the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget to retrieve transactions from. Defaults to "last-used".
            since_date (str, optional): The date to retrieve transactions since. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.
            last_knowledge_of_server (int, optional): The knowledge of the server to retrieve transactions from. Defaults to 0.

        Returns:
            dict: The response from the server containing the retrieved transactions.
        """
        endpoint = f"/budgets/{budget_id}/transactions"
        if since_date:
            endpoint += f"?since_date={since_date}"
        if type:
            endpoint += f"?type={type}"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # POST /budgets/{budget_id}/transactions
    def request_create_transactions(
        self, budget_id: str = "last-used", request_body: str = None
    ):
        """
        Sends a request to create transactions for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            request_body (str, optional): The JSON request body containing the transaction data. Defaults to None.

        Returns:
            The response from the API call.
        """
        endpoint = f"/budgets/{budget_id}/transactions"
        return self.http_utils.post(endpoint=endpoint, json=request_body)

    # PATCH /budgets/{budget_id}/transactions
    def request_update_transactions(
        self, budget_id: str = "last-used", request_body: str = None
    ):
        """
        Sends a PATCH request to update transactions for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            request_body (str, optional): The JSON request body. Defaults to None.

        Returns:
            The response from the PATCH request.
        """
        endpoint = f"/budgets/{budget_id}/transactions"
        return self.http_utils.patch(endpoint=endpoint, json=request_body)

    # POST /budgets/{budget_id}/transactions/import
    def request_import_transactions(self, budget_id: str = "last-used"):
        """
        Sends a request to import transactions for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget to import transactions for. Defaults to "last-used".

        Returns:
            The response from the HTTP POST request.
        """
        endpoint = f"/budgets/{budget_id}/transactions/import"
        return self.http_utils.post(endpoint=endpoint)

    # GET /budgets/{budget_id}/transactions/{transaction_id}
    def request_get_transaction(
        self, budget_id: str = "last-used", transaction_id: str = None
    ):
        """
        Retrieves a specific transaction from a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transaction_id (str, optional): The ID of the transaction. If not provided, all transactions will be returned.

        Returns:
            dict: The retrieved transaction information.

        Raises:
            HTTPError: If the request fails or the transaction is not found.
        """
        endpoint = f"/budgets/{budget_id}/transactions/{transaction_id}"
        return self.http_utils.get(endpoint=endpoint)

    # PUT /budgets/{budget_id}/transactions/{transaction_id}
    def request_update_transaction(
        self,
        budget_id: str = "last-used",
        transaction_id: str = None,
        request_body: str = None,
    ):
        """
        Updates a transaction in the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transaction_id (str, optional): The ID of the transaction to update.
            request_body (str, optional): The JSON request body containing the updated transaction data.

        Returns:
            The response from the API call.
        """
        endpoint = f"/budgets/{budget_id}/transactions/{transaction_id}"
        return self.http_utils.put(endpoint=endpoint, json=request_body)

    # DELETE /budgets/{budget_id}/transactions/{transaction_id}
    def request_delete_transaction(
        self, budget_id: str = "last-used", transaction_id: str = None
    ):
        """
        Sends a request to delete a transaction.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transaction_id (str, optional): The ID of the transaction to be deleted.

        Returns:
            The response from the HTTP request.
        """
        endpoint = f"/budgets/{budget_id}/transactions/{transaction_id}"
        return self.http_utils.delete(endpoint=endpoint)

    # GET /budgets/{budget_id}/accounts/{account_id}/transactions
    def request_get_account_transactions(
        self,
        budget_id: str = "last-used",
        account_id: str = None,
        since_date: str = None,
        type: str = None,
        last_knowledge_of_server: int = 0,
    ):
        """
        Retrieves the account transactions for a specific budget and account.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            account_id (str, optional): The ID of the account. Defaults to None.
            since_date (str, optional): The date to retrieve transactions from. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The account transactions.

        """
        endpoint = f"/budgets/{budget_id}/accounts/{account_id}/transactions"
        if since_date:
            endpoint += f"?since_date={since_date}"
        if type:
            endpoint += f"?type={type}"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/categories/{category_id}/transactions
    def request_get_category_transactions(
        self,
        budget_id: str = "last-used",
        category_id: str = None,
        since_date: str = None,
        type: str = None,
        last_knowledge_of_server: int = 0,
    ):
        """
        Retrieves transactions for a specific category.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            category_id (str, optional): The ID of the category. Defaults to None.
            since_date (str, optional): The starting date to retrieve transactions from. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.
            last_knowledge_of_server (int, optional): The knowledge of the server to retrieve transactions from. Defaults to 0.

        Returns:
            dict: The response containing the retrieved transactions.
        """
        endpoint = f"/budgets/{budget_id}/categories/{category_id}/transactions"
        if since_date:
            endpoint += f"?since_date={since_date}"
        if type:
            endpoint += f"?type={type}"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/payees/{payee_id}/transactions
    def request_get_payee_transactions(
        self,
        budget_id: str = "last-used",
        payee_id: str = None,
        since_date: str = None,
        type: str = None,
        last_knowledge_of_server: int = 0,
    ):
        """
        Retrieves transactions for a specific payee.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee_id (str, optional): The ID of the payee. Defaults to None.
            since_date (str, optional): The date to retrieve transactions since. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The response from the API containing the payee transactions.
        """
        endpoint = f"/budgets/{budget_id}/payees/{payee_id}/transactions"
        if since_date:
            endpoint += f"?since_date={since_date}"
        if type:
            endpoint += f"?type={type}"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/months/{month}/transactions
    def request_get_month_transactions(
        self,
        budget_id: str = "last-used",
        month: str = "current",
        since_date: str = None,
        type: str = None,
        last_knowledge_of_server: int = 0,
    ):
        """
        Retrieves the transactions for a specific month in a budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month (str, optional): The month to retrieve transactions for. Defaults to "current".
            since_date (str, optional): The starting date for the transactions. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The response from the API containing the transactions for the specified month.
        """
        endpoint = f"/budgets/{budget_id}/months/{month}/transactions"
        if since_date:
            endpoint += f"?since_date={since_date}"
        if type:
            endpoint += f"?type={type}"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # GET /budgets/{budget_id}/scheduled_transactions
    def request_get_scheduled_transactions(
        self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
    ):
        """
        Retrieves the scheduled transactions for a specific budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            last_knowledge_of_server (int, optional): The knowledge of the server. Defaults to 0.

        Returns:
            The response from the server containing the scheduled transactions.
        """
        endpoint = f"/budgets/{budget_id}/scheduled_transactions"
        if last_knowledge_of_server:
            endpoint += f"?last_knowledge_of_server={last_knowledge_of_server}"
        return self.http_utils.get(endpoint=endpoint)

    # POST /budgets/{budget_id}/scheduled_transactions
    def request_create_scheduled_transaction(
        self, budget_id: str = "last-used", request_body: str = None
    ):
        """
        Creates a new scheduled transaction for the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            request_body (str, optional): The request body containing the details of the scheduled transaction. Defaults to None.

        Returns:
            The response from the API call.
        """
        endpoint = f"/budgets/{budget_id}/scheduled_transactions"
        return self.http_utils.post(endpoint=endpoint, json=request_body)

    # GET /budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id}
    def request_get_scheduled_transaction(
        self, budget_id: str = "last-used", scheduled_transaction_id: str = None
    ):
        """
        Retrieves a scheduled transaction from the specified budget.

        Args:
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            scheduled_transaction_id (str, optional): The ID of the scheduled transaction.

        Returns:
            dict: The scheduled transaction information.

        Raises:
            HTTPException: If the request fails.
        """
        endpoint = (
            f"/budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id}"
        )
        return self.http_utils.get(endpoint=endpoint)
