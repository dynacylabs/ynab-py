import pynab.schemas as schemas
from pynab.endpoints import Endpoints
import pynab.enums as enums
from datetime import datetime
import pynab.utils as utils


class Api:
    def __init__(self, pynab=None):
        """
        Initializes an instance of the API class.

        Parameters:
        - pynab (object): An instance of the Pynab class.

        Returns:
        - None
        """
        self.pynab = pynab
        self.endpoints = Endpoints(pynab=self.pynab)

    def get_user(self):
        """
        Retrieves the user information from the API.

        Returns:
            User: An instance of the User class representing the user information.

        Raises:
            Exception: If the API response status code is not 200, an exception is raised with the error information.
        """
        response = self.endpoints.request_get_user()
        _json = response.json()

        if response.status_code == 200:
            user_json = _json.get("data", {}).get("user", {})
            return schemas.User(pynab=self.pynab, _json=user_json)
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_budgets(self, include_accounts: bool = False):
        """
        Retrieves budgets from the API.

        Args:
            include_accounts (bool, optional): Whether to include accounts in the response. Defaults to False.

        Returns:
            dict: A dictionary containing the budgets retrieved from the API. The keys are the budget IDs and the values are instances of the `Budget` class.

        Raises:
            Exception: If an error occurs while retrieving the budgets.

        """
        response = self.endpoints.request_get_budgets(include_accounts=include_accounts)
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})

            budgets = utils._dict()
            for budget_json in data_json.get("budgets", []):
                budget = schemas.Budget(pynab=self.pynab, _json=budget_json)
                budgets[budget.id] = budget

            if data_json.get("default_budget", []) is not None:
                for default_budget_json in data_json.get("default_budget", []):
                    default_budget = schemas.Budget(
                        pynab=self.pynab, _json=default_budget_json
                    )
                    for budget in budgets:
                        if budget.id == default_budget.id:
                            budget.default = True

            return budgets

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_budget(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
    ):
        """
        Retrieves a budget from the server.

        Args:
            budget (schemas.Budget, optional): The budget object to retrieve. Defaults to None.
            budget_id (str, optional): The ID of the budget to retrieve. Defaults to "last-used".

        Returns:
            schemas.Budget: The retrieved budget object.

        Raises:
            Exception: If there is an error retrieving the budget.
        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_budget(
            budget_id=budget_id,
            last_knowledge_of_server=self.pynab.server_knowledges("get_budget"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_budget"] = data_json.get(
                "server_knowledge", 0
            )
            return schemas.Budget(pynab=self.pynab, _json=data_json.get("budget", {}))
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_budget_settings(
        self, budget: schemas.Budget = None, budget_id: str = "last-used"
    ):
        """
        Retrieves the budget settings for a given budget or the last-used budget.

        Parameters:
        - budget (schemas.Budget, optional): The budget object for which to retrieve the settings. If not provided, the last-used budget will be used.
        - budget_id (str, optional): The ID of the budget for which to retrieve the settings. Defaults to "last-used" if not provided.

        Returns:
        - schemas.BudgetSettings: The budget settings object.

        Raises:
        - Exception: If the API request fails or returns an error.

        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_budget_settings(budget_id=budget_id)
        _json = response.json()

        if response.status_code == 200:
            settings_json = _json.get("data", {}).get("settings", {})
            return schemas.BudgetSettings(pynab=self.pynab, _json=settings_json)
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_accounts(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
    ):
        """
        Retrieves the accounts associated with the specified budget.

        Parameters:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            dict: A dictionary containing the retrieved accounts, where the keys are the account IDs and the values are the account objects.

        Raises:
            Exception: If the response status code is not 200, an exception is raised with the error details.
        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_accounts(
            budget_id=budget_id,
            last_knowledge_of_server=self.pynab.server_knowledges("get_accounts"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_accounts"] = data_json.get(
                "server_knowledge", 0
            )
            accounts = utils._dict()
            for account_json in data_json.get("accounts", []):
                account = schemas.Account(
                    pynab=self.pynab, budget=budget, _json=account_json
                )
                accounts[account.id] = account
            return accounts
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def create_account(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        account_name: str = None,
        account_type: enums.AccountType = None,
        account_balance: int = 0,
    ):
        """
        Creates a new account.

        Args:
            budget (schemas.Budget, optional): The budget to associate the account with. Defaults to None.
            budget_id (str, optional): The ID of the budget to associate the account with. Defaults to "last-used".
            account_name (str, optional): The name of the account. Defaults to None.
            account_type (enums.AccountType, optional): The type of the account. Defaults to None.
            account_balance (int, optional): The initial balance of the account. Defaults to 0.

        Returns:
            schemas.Account: The created account.

        Raises:
            Exception: If there is an error creating the account.
        """
        budget_id = budget.id if budget else budget_id

        request_body = {
            "account": {
                "name": account_name,
                "type": account_type.value,
                "balance": account_balance,
            }
        }

        response = self.endpoints.request_create_account(
            budget_id=budget_id, request_body=request_body
        )
        _json = response.json()

        if response.status_code == 201:
            data_json = _json.get("data", {})
            account = schemas.Account(
                pynab=self.pynab, budget=budget, _json=data_json.get("account", {})
            )
            budget.accounts[account.id] = account
            return account

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_account(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        account: schemas.Account = None,
        account_id: str = None,
    ):
        """
        Retrieves an account from the specified budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            account (schemas.Account, optional): The account object. Defaults to None.
            account_id (str, optional): The ID of the account. Defaults to None.

        Returns:
            schemas.Account: The retrieved account.

        Raises:
            Exception: If there is an error retrieving the account.
        """
        budget_id = budget.id if budget else budget_id
        account_id = account.id if account else account_id

        response = self.endpoints.request_get_account(
            budget_id=budget_id, account_id=account_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            return schemas.Account(pynab=self.pynab, _json=data_json.get("account", {}))
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_categories(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
    ):
        """
        Retrieves the categories for a given budget or the last-used budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            dict: A dictionary containing the category groups, where the keys are the category group IDs and the values are the category group objects.

        Raises:
            Exception: If there is an error in the API response.

        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_categories(
            budget_id=budget_id,
            last_knowledge_of_server=self.pynab.server_knowledges("get_categories"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_categories"] = data_json.get(
                "server_knowledge", 0
            )
            category_groups = utils._dict()
            for category_group in data_json.get("category_groups", []):
                category_group = schemas.CategoryGroup(
                    pynab=self.pynab, budget=budget, _json=category_group
                )
                category_groups[category_group.id] = category_group
            return category_groups

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_category(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        category: schemas.Category = None,
        category_id: str = None,
    ):
        """
        Retrieves a category from the API.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            category (schemas.Category, optional): The category object. Defaults to None.
            category_id (str, optional): The ID of the category. Defaults to None.

        Returns:
            schemas.Category: The retrieved category.

        Raises:
            Exception: If the API request fails.
        """
        budget_id = budget.id if budget else budget_id
        category_id = category.id if category else category_id

        response = self.endpoints.request_get_category(
            budget_id=budget_id, category_id=category_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            category = schemas.Category(
                pynab=self.pynab, budget=budget, _json=data_json.get("category", [])
            )
            return category

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def update_category(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        category_group: schemas.CategoryGroup = None,
        category_group_id: str = None,
        category: schemas.Category = None,
        category_id: str = None,
        name=None,
        note: str = None,
    ):
        """
        Update a category in the budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            category_group (schemas.CategoryGroup, optional): The category group object. Defaults to None.
            category_group_id (str, optional): The ID of the category group. Defaults to None.
            category (schemas.Category, optional): The category object. Defaults to None.
            category_id (str, optional): The ID of the category. Defaults to None.
            name (any, optional): The name of the category. Defaults to None.
            note (str, optional): The note for the category. Defaults to None.

        Returns:
            schemas.Category: The updated category object.

        Raises:
            Exception: If there is an error updating the category.
        """
        budget_id = budget.id if budget else budget_id
        category_group_id = category_group.id if category else category_group
        category_id = category.id if category else category

        request_body = {
            "category": {
                "name": name,
                "note": note,
                "category_group_id": category_group_id,
            }
        }
        response = self.endpoints.request_update_category(
            budget_id=budget_id,
            category_id=category_id,
            request_body=request_body,
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            category = schemas.Category(
                pynab=self.pynab, budget=budget, _json=data_json
            )
            return category

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_category_for_month(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        month: str = "current",
        category: schemas.Category = None,
        category_id: str = None,
    ):
        """
        Retrieves the category for a specific month in a budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month (str, optional): The month to retrieve the category for. Defaults to "current".
            category (schemas.Category, optional): The category object. Defaults to None.
            category_id (str, optional): The ID of the category. Defaults to None.

        Returns:
            schemas.Category: The category object for the specified month.

        Raises:
            Exception: If there is an error retrieving the category.
        """
        budget_id = budget.id if budget else budget_id
        category_id = category.id if category else category_id

        response = self.endpoints.request_get_category_for_month(
            budget_id=budget_id, month=month, category_id=category_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            category = schemas.Category(
                pynab=self.pynab, budget=budget, _json=data_json.get("category", [])
            )
            return category

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def update_category_for_month(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        month: schemas.Month = None,
        month_id: str = "current",
        category: schemas.Category = None,
        category_id: str = None,
        budgeted: int = 0,
    ):
        """
        Update the budgeted amount for a category in a specific month.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month (schemas.Month, optional): The month object. Defaults to None.
            month_id (str, optional): The ID of the month. Defaults to "current".
            category (schemas.Category, optional): The category object. Defaults to None.
            category_id (str, optional): The ID of the category. Defaults to None.
            budgeted (int, optional): The new value for the amount assigned to this category

        Returns:
            schemas.Category: The updated category object.

        Raises:
            Exception: If the response status code is not 200, an exception is raised with the error details.
        """
        budget_id = budget.id if budget else budget_id
        month_id = month.month if month else month_id
        category_id = category.id if category else category_id

        request_body = {"category": {"budgeted": budgeted}}
        response = self.endpoints.request_update_category_for_month(
            budget_id=budget_id,
            month_id=month_id,
            category_id=category_id,
            request_body=request_body,
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            category = schemas.Category(
                pynab=self.pynab, budget=budget, _json=data_json.get("category", [])
            )
            budget.category_groups[category.category_group_id].categories[
                category.id
            ] = category
            budget.categories[category.id] = category

            return category

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_payees(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
    ):
        """
        Retrieves the payees associated with a budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            dict: A dictionary containing the payees, where the key is the payee ID and the value is the payee object.

            If the request is successful, the dictionary will contain the payees associated with the budget.
            If the request fails, an error object will be returned.

        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_payees(
            budget_id=budget_id,
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            payees = utils._dict()
            for payee in data_json.get("payees", []):
                payee = schemas.Payee(pynab=self.pynab, budget=budget, _json=payee)
                payees[payee.id] = payee
            return payees

        else:
            return schemas.Error(pynab=self.pynab, _json=_json.get("error", {}))

    def get_payee(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        payee: schemas.Payee = None,
        payee_id: str = None,
    ):
        """
        Retrieves a payee from the specified budget or the last-used budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee (schemas.Payee, optional): The payee object. Defaults to None.
            payee_id (str, optional): The ID of the payee. Defaults to None.

        Returns:
            schemas.Payee: The retrieved payee object.

        Raises:
            Exception: If the API response status code is not 200, an exception is raised with the error details.
        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_payee(
            budget_id=budget_id, payee_id=payee_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            payee = schemas.Payee(
                pynab=self.pynab, budget=budget, _json=data_json.get("payee", [])
            )
            return payee

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def update_payee(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        payee: schemas.Payee = None,
        payee_id: str = None,
        name: str = None,
    ):
        """
        Update a payee with the given information.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee (schemas.Payee, optional): The payee object. Defaults to None.
            payee_id (str, optional): The ID of the payee. Defaults to None.
            name (str, optional): The new name for the payee. Defaults to None.

        Returns:
            schemas.Payee: The updated payee object.

        Raises:
            Exception: If the API request fails.
        """
        budget_id = budget.id if budget else budget_id
        payee_id = payee.id if payee else payee_id

        request_body = {"payee": {"name": name}}
        response = self.endpoints.request_update_payee(
            budget_id=budget_id, payee_id=payee_id, request_body=request_body
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            payee = schemas.Payee(
                pynab=self.pynab, budget=budget, _json=data_json.get("payee", [])
            )
            budget.payees[payee.id] = payee

            return payee

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_budget_payee_locations(
        self, budget: schemas.Budget = None, budget_id: str = "last-used"
    ):
        """
        Retrieves the payee locations for a given budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            dict: A dictionary containing the payee locations, where the keys are the payee location IDs and the values are the payee location objects.

        Raises:
            Exception: If there is an error retrieving the payee locations.
        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_all_payee_locations(budget_id=budget_id)
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            payee_locations = utils._dict()
            for payee_location in data_json.get("payee_locations", []):
                payee_location = schemas.PayeeLocation(
                    pynab=self.pynab, budget=budget, _json=payee_location
                )
                payee_locations[payee_location.id] = payee_location
            return payee_locations

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_payee_location(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        payee_location: schemas.PayeeLocation = None,
        payee_location_id: str = None,
    ):
        """
        Retrieves a payee location from the API.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The budget ID. Defaults to "last-used".
            payee_location (schemas.PayeeLocation, optional): The payee location object. Defaults to None.
            payee_location_id (str, optional): The payee location ID. Defaults to None.

        Returns:
            schemas.PayeeLocation: The retrieved payee location.

        Raises:
            Exception: If the API request fails.
        """
        budget_id = budget.id if budget else budget_id
        payee_location_id = payee_location.id if payee_location else payee_location_id

        response = self.endpoints.request_get_payee_location(
            budget_id=budget_id, payee_location_id=payee_location_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            payee_location = schemas.PayeeLocation(
                pynab=self.pynab,
                budget=budget,
                _json=data_json.get("payee_location", []),
            )
            return payee_location

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_payee_locations(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        payee: schemas.Payee = None,
        payee_id: str = None,
    ):
        """
        Retrieves the payee locations for a given budget and payee.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee (schemas.Payee, optional): The payee object. Defaults to None.
            payee_id (str, optional): The ID of the payee. Defaults to None.

        Returns:
            dict: A dictionary of payee locations, where the keys are the payee location IDs and the values are the payee location objects.

        Raises:
            Exception: If the API response status code is not 200, an exception is raised with the error details.
        """
        budget_id = budget.id if budget else budget_id
        payee_id = payee.id if payee else payee_id

        response = self.endpoints.request_get_payee_locations(
            budget_id=budget_id, payee_id=payee_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            payee_locations = utils._dict()
            for payee_location in data_json.get("payee_locations", []):
                payee_location = schemas.PayeeLocation(
                    pynab=self.pynab, budget=budget, _json=payee_location
                )
                payee_locations[payee_location.id] = payee_location
            return payee_locations

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_months(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
    ):
        """
        Retrieves the months for a given budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            dict: A dictionary containing the months as keys and their corresponding Month objects as values.

        Raises:
            Exception: If there is an error retrieving the months.
        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_months(
            budget_id=budget_id,
            last_knowledge_of_server=self.pynab.server_knowledges("get_months"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_months"] = data_json.get(
                "server_knowledge", 0
            )
            months = utils._dict()
            for month in data_json.get("months", []):
                month = schemas.Month(pynab=self.pynab, budget=budget, _json=month)
                month.month = datetime.fromisoformat(str(month.month))
                year = month.month.strftime("%Y")
                month_name = month.month.strftime("%B")
                months[f"{year} - {month_name}"] = month
            return months

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_month(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        month: schemas.Month = None,
        month_id: str = "current",
    ):
        """
        Retrieves a specific month from the budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month (schemas.Month, optional): The month object. Defaults to None.
            month_id (str, optional): The ID of the month. Defaults to "current".

        Returns:
            schemas.Month: The retrieved month object.

        Raises:
            Exception: If there is an error retrieving the month.
        """
        budget_id = budget.id if budget else budget_id
        month_id = month.month if month else month_id

        response = self.endpoints.request_get_month(
            budget_id=budget_id, month_id=month_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            month = schemas.Month(
                pynab=self.pynab, budget=budget, _json=data_json.get("month", {})
            )
            return month

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        since_date: str = None,
        type: str = None,
    ):
        """
        Retrieves transactions from the specified budget or the last-used budget.

        Args:
            budget (schemas.Budget, optional): The budget object to retrieve transactions from. Defaults to None.
            budget_id (str, optional): The ID of the budget to retrieve transactions from. Defaults to "last-used".
            since_date (str, optional): The date to retrieve transactions from. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.

        Returns:
            dict: A dictionary of transactions, where the keys are the transaction IDs and the values are the transaction objects.

        Raises:
            Exception: If there is an error retrieving the transactions.
        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_transactions(
            budget_id=budget_id,
            since_date=since_date,
            type=type,
            last_knowledge_of_server=self.pynab.server_knowledges("get_transactions"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_transactions"] = data_json.get(
                "server_knowledge", 0
            )
            transactions = utils._dict()
            for transaction in data_json.get("transactions", []):
                transaction = schemas.Transaction(
                    pynab=self.pynab, budget=budget, _json=transaction
                )
                transactions[transaction.id] = transaction
            return transactions

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def create_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        transactions: list = None,
    ):
        """
        Create transactions in the specified budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transactions (list, optional): The list of transactions to create. Defaults to None.

        Returns:
            Union[List[schemas.Transaction], Dict[str, Any]]: If a single transaction is created, returns the created transaction as a dictionary. If multiple transactions are created, returns a list of created transactions.

        Raises:
            Exception: If there is an error creating the transactions.
        """
        budget_id = budget.id if budget else budget_id

        if len(transactions) == 1:
            transaction_dict = transactions[0].to_dict()

            request_body = {
                "transaction": {
                    "account_id": transaction_dict.get("account_id"),
                    "date": transaction_dict.get("date"),
                    "amount": transaction_dict.get("amount"),
                    "payee_id": transaction_dict.get("payee_id"),
                    "payee_name": transaction_dict.get("payee_name"),
                    "category_id": transaction_dict.get("category_id"),
                    "memo": transaction_dict.get("memo"),
                    "flag_color": transaction_dict.get("flag_color"),
                    "cleared": transaction_dict.get("cleared"),
                    "approved": transaction_dict.get("approved"),
                    "flag_color": transaction_dict.get("flag_color"),
                    "subtransactions": transaction_dict.get("subtransactions"),
                    "import_id": transaction_dict.get("import_id"),
                }
            }
        else:
            transactions_list = []
            for transaction in transactions:
                transaction_dict = transactions[0].to_dict()

                transactions_list.append(
                    {
                        "account_id": transaction_dict.get("account_id"),
                        "date": transaction_dict.get("date"),
                        "amount": transaction_dict.get("amount"),
                        "payee_id": transaction_dict.get("payee_id"),
                        "payee_name": transaction_dict.get("payee_name"),
                        "category_id": transaction_dict.get("category_id"),
                        "memo": transaction_dict.get("memo"),
                        "flag_color": transaction_dict.get("flag_color"),
                        "cleared": transaction_dict.get("cleared"),
                        "approved": transaction_dict.get("approved"),
                        "flag_color": transaction_dict.get("flag_color"),
                        "subtransactions": transaction_dict.get("subtransactions"),
                        "import_id": transaction_dict.get("import_id"),
                    }
                )
            request_body = {"transactions": transactions_list}

        response = self.endpoints.request_create_transactions(
            budget_id=budget_id, request_body=request_body
        )
        _json = response.json()

        if response.status_code == 201:
            data_json = _json.get("data", {})

            ret_val = {
                "transaction_ids": data_json.get("transaction_ids", []),
                "duplicate_import_ids": data_json.get("duplicate_import_ids", []),
                "server_knowledge": data_json.get("server_knowledge", 0),
            }

            if "transaction" in data_json:
                ret_val["transaction"] = schemas.Transaction(
                    pynab=self.pynab,
                    budget=budget,
                    _json=data_json.get("transaction", {}),
                )
            else:
                transactions = []
                for transaction in data_json.get("transactions", []):
                    transaction = schemas.Transaction(
                        pynab=self.pynab, budget=budget, _json=transaction
                    )
                    transactions.append(transaction)
                return transactions

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def update_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        transactions: list = None,
    ):
        """
        Update transactions in the budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transactions (list, optional): List of transactions to update. Defaults to None.

        Returns:
            dict: A dictionary containing the updated transaction information.

        Raises:
            Exception: If there is an error in the update process.
        """
        budget_id = budget.id if budget else budget_id

        request_body = {
            "transactions": [transaction.to_dict() for transaction in transactions]
        }

        response = self.endpoints.request_update_transactions(
            budget_id=budget_id, request_body=request_body
        )
        _json = response.json()

        if response.status_code == 209:
            data_json = _json.get("data", {})

            ret_val = {
                "transaction_ids": data_json.get("transaction_ids", []),
                "duplicate_import_ids": data_json.get("duplicate_import_ids", []),
                "server_knowledge": data_json.get("server_knowledge", 0),
            }

            if "transaction" in data_json:
                ret_val["transaction"] = schemas.Transaction(
                    pynab=self.pynab,
                    budget=budget,
                    _json=data_json.get("transaction", {}),
                )
            else:
                for transaction in data_json.get("transactions", []):
                    transaction = schemas.Transaction(
                        pynab=self.pynab, budget=budget, _json=transaction
                    )
                    ret_val["transactions"].append(transaction)

            return ret_val

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def import_transactions(
        self, budget: schemas.Budget = None, budget_id: str = "last-used"
    ):
        """
        Imports transactions into the budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".

        Returns:
            list: A list of transaction IDs if the import is successful.
            schemas.Error: An error object if the import fails.
        """
        budget_id = budget.id if budget else budget_id
        response = self.endpoints.request_import_transactions(budget_id=budget_id)
        _json = response.json()

        if response.status_code in [200, 201]:
            return _json.get("data", {}).get("transaction_ids", [])
        else:
            return schemas.Error(pynab=self.pynab, _json=_json.get("error", {}))

    def get_transaction(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        transaction: schemas.Transaction = None,
        transaction_id: str = None,
    ):
        """
        Retrieves a transaction from the specified budget or the last-used budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transaction (schemas.Transaction, optional): The transaction object. Defaults to None.
            transaction_id (str, optional): The ID of the transaction. Defaults to None.

        Returns:
            schemas.Transaction: The retrieved transaction.

        Raises:
            Exception: If there is an error retrieving the transaction.
        """
        budget_id = budget.id if budget else budget_id
        transaction_id = transaction.id if transaction else transaction_id

        response = self.endpoints.request_get_transaction(
            budget_id=budget_id, transaction_id=transaction_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            return schemas.Transaction(
                pynab=self.pynab, _json=data_json.get("transaction", [])
            )

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def update_transaction(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        transaction: schemas.Transaction = None,
        transaction_id: str = None,
        request_body: str = None,
    ):
        """
        Update a transaction in the budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transaction (schemas.Transaction, optional): The transaction object. Defaults to None.
            transaction_id (str, optional): The ID of the transaction. Defaults to None.
            request_body (str, optional): The request body. Defaults to None.

        Returns:
            schemas.Transaction: The updated transaction object.

        Raises:
            Exception: If there is an error updating the transaction.
        """
        budget_id = budget.id if budget else budget_id
        transaction_id = transaction.id if transaction else transaction_id

        request_body = {"transaction": transaction.to_dict()}
        response = self.endpoints.request_update_transaction(
            budget_id=budget_id,
            transaction_id=transaction_id,
            request_body=request_body,
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            return schemas.Transaction(
                pynab=self.pynab, _json=data_json.get("transaction", [])
            )
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def delete_transaction(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        transaction: schemas.Transaction = None,
        transaction_id: str = None,
    ):
        """
        Deletes a transaction from the specified budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            transaction (schemas.Transaction, optional): The transaction object. Defaults to None.
            transaction_id (str, optional): The ID of the transaction. Defaults to None.

        Returns:
            schemas.Transaction: The deleted transaction.

        Raises:
            Exception: If the deletion fails, an exception is raised with the error details.
        """
        budget_id = budget.id if budget else budget_id
        transaction_id = transaction.id if transaction else transaction_id

        response = self.endpoints.request_delete_transaction(
            budget_id=budget_id, transaction_id=transaction_id
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            return schemas.Transaction(
                pynab=self.pynab, _json=data_json.get("transaction", [])
            )
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_account_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        account: schemas.Account = None,
        account_id: str = None,
        since_date: str = None,
        type: str = None,
    ):
        """
        Retrieves account transactions from the API.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The budget ID. Defaults to "last-used".
            account (schemas.Account, optional): The account object. Defaults to None.
            account_id (str, optional): The account ID. Defaults to None.
            since_date (str, optional): The date to retrieve transactions since. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.

        Returns:
            dict: A dictionary of transactions, where the transaction ID is the key and the transaction object is the value.

        Raises:
            Exception: If there is an error retrieving the transactions.
        """
        budget_id = budget.id if budget else budget_id
        account_id = account.id if account else account_id

        response = self.endpoints.request_get_account_transactions(
            budget_id=budget_id,
            account_id=account_id,
            since_date=since_date,
            type=type,
            last_knowledge_of_server=self.pynab.server_knowledges("get_account_transactions"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_account_transactions"] = data_json.get(
                "server_knowledge", 0
            )
            transactions = utils._dict()
            for transaction in data_json.get("transactions", []):
                transaction = schemas.Transaction(
                    pynab=self.pynab, budget=budget, _json=transaction
                )
                transactions[transaction.id] = transaction
            return transactions

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_category_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        category: schemas.Category = None,
        category_id: str = None,
        since_date: str = None,
        type: str = None,
    ):
        """
        Retrieves transactions for a specific category.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The budget ID. Defaults to "last-used".
            category (schemas.Category, optional): The category object. Defaults to None.
            category_id (str, optional): The category ID. Defaults to None.
            since_date (str, optional): The starting date for the transactions. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.

        Returns:
            dict: A dictionary of transactions, where the keys are the transaction IDs and the values are the transaction objects.

        Raises:
            Exception: If there is an error retrieving the transactions.
        """
        budget_id = budget.id if budget else budget_id
        category_id = category.id if category else category_id

        response = self.endpoints.request_get_category_transactions(
            budget_id=budget_id,
            category_id=category_id,
            since_date=since_date,
            type=type,
            last_knowledge_of_server=self.pynab.server_knowledges("get_category_transactions"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_category_transactions"] = data_json.get(
                "server_knowledge", 0
            )
            transactions = utils._dict()
            for transaction in data_json.get("transactions", []):
                transaction = schemas.Transaction(
                    pynab=self.pynab, budget=budget, _json=transaction
                )
                transactions[transaction.id] = transaction
            return transactions
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_payee_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        payee: schemas.Payee = None,
        payee_id: str = None,
        since_date: str = None,
        type: str = None,
    ):
        """
        Retrieves transactions associated with a specific payee.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            payee (schemas.Payee, optional): The payee object. Defaults to None.
            payee_id (str, optional): The ID of the payee. Defaults to None.
            since_date (str, optional): The starting date for the transactions. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.

        Returns:
            dict: A dictionary of transactions, where the transaction ID is the key and the transaction object is the value.

        Raises:
            Exception: If there is an error retrieving the transactions.
        """
        budget_id = budget.id if budget else budget_id
        payee_id = payee.id if payee else payee_id

        response = self.endpoints.request_get_payee_transactions(
            budget_id=budget_id,
            payee_id=payee_id,
            since_date=since_date,
            type=type,
            last_knowledge_of_server=self.pynab.server_knowledges("get_payee_transactions"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_payee_transactions"] = data_json.get(
                "server_knowledge", 0
            )
            transactions = utils._dict()
            for transaction in data_json.get("transactions", []):
                transaction = schemas.Transaction(
                    pynab=self.pynab, budget=budget, _json=transaction
                )
                transactions[transaction.id] = transaction
            return transactions
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_month_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        month: schemas.Month = None,
        month_id: str = "current",
        since_date: str = None,
        type: str = None,
    ):
        """
        Retrieves the transactions for a specific month in a budget.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The ID of the budget. Defaults to "last-used".
            month (schemas.Month, optional): The month object. Defaults to None.
            month_id (str, optional): The ID of the month. Defaults to "current".
            since_date (str, optional): The starting date for the transactions. Defaults to None.
            type (str, optional): The type of transactions to retrieve. Defaults to None.

        Returns:
            dict: A dictionary of transactions, where the keys are the transaction IDs and the values are the transaction objects.

        Raises:
            Exception: If there is an error retrieving the transactions.
        """
        budget_id = budget.id if budget else budget_id
        month_id = month.month if month else month_id

        response = self.endpoints.request_get_month_transactions(
            budget_id=budget_id,
            month=month_id,
            since_date=since_date,
            type=type,
            last_knowledge_of_server=self.pynab.server_knowledges("get_month_transactions"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_month_transactions"] = data_json.get(
                "server_knowledge", 0
            )
            transactions = utils._dict()
            for transaction in data_json.get("transactions", []):
                transaction = schemas.Transaction(
                    pynab=self.pynab, budget=budget, _json=transaction
                )
                transactions[transaction.id] = transaction
            return transactions
        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def get_scheduled_transactions(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
    ):
        """
        Retrieves the scheduled transactions from the specified budget or the last-used budget.

        Args:
            budget (schemas.Budget, optional): The budget object to retrieve scheduled transactions from. Defaults to None.
            budget_id (str, optional): The ID of the budget to retrieve scheduled transactions from. Defaults to "last-used".

        Returns:
            dict: A dictionary of scheduled transactions, where the keys are the transaction IDs and the values are the corresponding ScheduledTransaction objects.

        Raises:
            Exception: If there is an error retrieving the scheduled transactions.

        """
        budget_id = budget.id if budget else budget_id

        response = self.endpoints.request_get_scheduled_transactions(
            budget_id=budget_id,
            last_knowledge_of_server=self.pynab.server_knowledges("get_scheduled_transactions"),
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            self.pynab._server_knowledges["get_scheduled_transactions"] = data_json.get(
                "server_knowledge", 0
            )
            transactions = utils._dict()
            for scheduled_transaction in data_json.get("scheduled_transactions", []):
                scheduled_transaction = schemas.ScheduledTransaction(
                    pynab=self.pynab, budget=budget, _json=scheduled_transaction
                )
                transactions[scheduled_transaction.id] = scheduled_transaction
            return transactions

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))

    def create_scheduled_transaction(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        scheduled_transaction: schemas.ScheduledTransaction = None,
    ):
        """
        Creates a scheduled transaction.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The budget ID. Defaults to "last-used".
            scheduled_transaction (schemas.ScheduledTransaction, optional): The scheduled transaction object. Defaults to None.

        Returns:
            Union[schemas.ScheduledTransaction, schemas.Error]: The created scheduled transaction object or an error object.
        """
        budget_id = budget.id if budget else budget_id

        scheduled_transaction_dict = scheduled_transaction.to_dict()

        # Ensure the scheduled_transaction is converted to a dictionary correctly
        request_body = {
            "scheduled_transaction": {
                "account_id": scheduled_transaction_dict.get("account_id"),
                "date": scheduled_transaction_dict.get("date"),
                "amount": scheduled_transaction_dict.get("amount"),
                "payee_id": scheduled_transaction_dict.get("payee_id"),
                "payee_name": scheduled_transaction_dict.get("payee_name"),
                "category_id": scheduled_transaction_dict.get("category_id"),
                "memo": scheduled_transaction_dict.get("memo"),
                "flag_color": scheduled_transaction_dict.get("flag_color"),
                "frequency": scheduled_transaction_dict.get("frequency"),
            }
        }

        response = self.endpoints.request_create_scheduled_transaction(
            budget_id=budget_id, request_body=request_body
        )
        _json = response.json()

        if response.status_code == 201:
            data_json = _json.get("data", {})
            scheduled_transaction = schemas.ScheduledTransaction(
                pynab=self.pynab,
                budget=budget,
                _json=data_json.get("scheduled_transaction", {}),
            )
            return scheduled_transaction
        else:
            error_json = _json.get("error", {})
            return schemas.Error(pynab=self.pynab, _json=error_json)

    def get_scheduled_transaction(
        self,
        budget: schemas.Budget = None,
        budget_id: str = "last-used",
        schedule_transaction: schemas.ScheduledTransaction = None,
        scheduled_transaction_id: str = None,
    ):
        """
        Retrieves a scheduled transaction from the API.

        Args:
            budget (schemas.Budget, optional): The budget object. Defaults to None.
            budget_id (str, optional): The budget ID. Defaults to "last-used".
            schedule_transaction (schemas.ScheduledTransaction, optional): The scheduled transaction object. Defaults to None.
            scheduled_transaction_id (str, optional): The scheduled transaction ID. Defaults to None.

        Returns:
            schemas.ScheduledTransaction: The retrieved scheduled transaction.

        Raises:
            Exception: If the API request fails.
        """
        budget_id = budget.id if budget else budget_id
        scheduled_transaction_id = (
            schedule_transaction.id
            if schedule_transaction
            else scheduled_transaction_id
        )

        response = self.endpoints.request_get_scheduled_transaction(
            budget_id=budget_id,
            scheduled_transaction_id=scheduled_transaction_id,
        )
        _json = response.json()

        if response.status_code == 200:
            data_json = _json.get("data", {})
            scheduled_transaction = schemas.ScheduledTransaction(
                pynab=self.pynab,
                budget=budget,
                _json=data_json.get("scheduled_transaction", {}),
            )
            return scheduled_transaction

        else:
            error_json = _json.get("error", {})
            raise Exception(schemas.Error(pynab=self.pynab, _json=error_json))
