from datetime import date, datetime
import pynab.enums as enums
import pynab.constants as constants
import pynab.utils as utils
import logging

from dateutil.parser import isoparse

import json


class User:
    def __init__(self, pynab=None, _json: str = None):
        """
        Initializes a new instance of the class.

        Args:
            pynab: The pynab object.
            _json: The JSON string.

        Attributes:
            id: The ID attribute.
        """

        self.pynab = pynab
        self._json: str = _json

        self.id: str = self._json.get("id", "")

    def to_dict(self):
        """
        Converts the object to a dictionary.

        Returns:
            dict: A dictionary representation of the object, containing the 'id' attribute.
        """
        return {"id": self.id}

    def to_json(self, indent: int = 4):
        """
        Convert the object to a JSON string representation.

        Args:
            indent (int, optional): The number of spaces to use for indentation. Defaults to 4.

        Returns:
            str: The JSON string representation of the object.
        """
        return json.dumps(self.to_dict(), cls=utils.CustomJsonEncoder, indent=indent)


class Error:
    def __init__(self, pynab=None, _json: str = None):
        """
        Initializes a new instance of the Schema class.

        Args:
            pynab: An instance of the Pynab class.
            _json: A JSON string representing the schema.

        Attributes:
            id (str): The ID of the schema.
            name (str): The name of the schema.
            detail (str): The detail of the schema.

        Raises:
            None.

        Returns:
            None.
        """
        self.pynab = pynab
        self._json: str = _json

        self.id: str = self._json.get("id", "")
        self.name: str = self._json.get("name", "")
        self.detail: str = self._json.get("detail", "")

        logging.error(f"api error: {self.id} - {self.name} - {self.detail}")

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object, formatted as "api error: {id} - {name} - {detail}".
        """
        return f"api error: {self.id} - {self.name} - {self.detail}"


class Budget:
    def __init__(self, pynab=None, _json: str = None):
        """
        Initialize a new instance of the `schemas` class.

        Args:
            pynab: An instance of the `pynab` class.
            _json: A JSON string.

        Attributes:
            id (str): The ID of the schema.
            name (str): The name of the schema.
            last_modified_on (datetime): The last modified date of the schema.
            first_month (date): The first month of the schema.
            last_month (date): The last month of the schema.
            date_format (DateFormat): The date format of the schema.
            currency_format (CurrencyFormat): The currency format of the schema.
            accounts (dict): A dictionary of accounts.
            payees (dict): A dictionary of payees.
            payee_locations (dict): A dictionary of payee locations.
            category_groups (dict): A dictionary of category groups.
            categories (dict): A dictionary of categories.
            months (dict): A dictionary of months.
            transactions (dict): A dictionary of transactions.
            subtransactions (dict): A dictionary of subtransactions.
            scheduled_transactions (dict): A dictionary of scheduled transactions.
            scheduled_subtransactions (dict): A dictionary of scheduled subtransactions.
        """
        self.pynab = pynab
        self._json: str = _json

        self._settings = None

        self.id: str = self._json.get("id", "")
        self.name: str = self._json.get("name", "")
        self.last_modified_on: datetime = isoparse(
            self._json.get("last_modified_on", constants.EPOCH)
        )
        self.first_month: date = isoparse(
            self._json.get("first_month", constants.EPOCH)
        ).date()
        self.last_month: date = isoparse(
            self._json.get("last_month", constants.EPOCH)
        ).date()
        self.date_format: DateFormat = DateFormat(
            pynab=self.pynab, _json=self._json.get("date_format", {})
        )
        self.currency_format: CurrencyFormat = CurrencyFormat(
            pynab=self.pynab, _json=self._json.get("currency_format", {})
        )

        self._accounts = utils._dict()
        if "accounts" in self._json:
            self.accounts = self._json.get("accounts", {})

        self._payees = utils._dict()
        if "payees" in self._json:
            self.payees = self._json.get("payees", {})

        self._payee_locations = utils._dict()
        if "payee_locations" in self._json:
            self.payee_locations = self._json.get("payee_locations", {})

        self._category_groups = utils._dict()
        if "category_groups" in self._json:
            self.category_groups = self._json.get("category_groups", {})

        self._categories = utils._dict()
        if "categories" in self._json:
            self.categories = self._json.get("categories", {})

        self._months = utils._dict()
        if "months" in self._json:
            self.months = self._json.get("months", {})

        self._transactions = utils._dict()
        if "transactions" in self._json:
            self.transactions = self._json.get("transactions", {})

        self._subtransactions = utils._dict()
        if "subtransactions" in self._json:
            self.subtransactions = self._json.get("subtransactions", {})

        self._scheduled_transactions = utils._dict()
        if "scheduled_transactions" in self._json:
            self.scheduled_transactions = self._json.get("scheduled_transactions", {})

        self._scheduled_subtransactions = utils._dict()
        if "scheduled_subtransactions" in self._json:
            self.scheduled_subtransactions = self._json.get(
                "scheduled_subtransactions", {}
            )

    @property
    def accounts(self):
        """
        Returns the accounts associated with the object.

        Returns:
            list: A list of accounts.
        """
        return self._accounts

    @accounts.setter
    def accounts(self, _json: str = ""):
        """
        Process the given JSON string and create Account objects for each account.

        Parameters:
            _json (str): The JSON string containing account information.

        Returns:
            None
        """
        for account in _json:
            account_obj = Account(pynab=self.pynab, _json=account)
            self._accounts[account_obj.id] = account_obj

    @accounts.getter
    def accounts(self):
        """
        Retrieve the accounts associated with the budget.

        Returns:
            dict: A dictionary containing the accounts associated with the budget.
        """
        if len(self._accounts) == 0:
            self._accounts = self.pynab.api.get_accounts(budget=self)
        return self._accounts

    @property
    def payees(self):
        """
        Returns the payees associated with the object.

        Returns:
            The payees associated with the object.
        """
        return self._payees

    @payees.setter
    def payees(self, _json: str = ""):
        """
        Adds payees to the schema.

        Parameters:
            _json (str): A JSON string containing payee information.

        Returns:
            None
        """
        for payee in _json:
            payee_obj = Payee(pynab=self.pynab, _json=payee)
            self._payees[payee_obj.id] = payee_obj

    @payees.getter
    def payees(self):
        """
        Retrieves the payees associated with the budget.

        If the payees have not been fetched yet, it calls the `get_payees` method from the `pynab.api` module
        and stores the result in the `_payees` attribute.

        Returns:
            dict: A dictionary containing the payees associated with the budget.

        """
        if len(self._payees) == 0:
            self._payees = self.pynab.api.get_payees(budget=self)
        return self._payees

    @property
    def payee_locations(self):
        """
        Returns the payee locations associated with the object.

        Returns:
            The payee locations.

        """
        return self._payee_locations

    @payee_locations.setter
    def payee_locations(self, _json: str = ""):
        """
        Adds payee locations to the schema.

        Parameters:
        - _json (str): A string representing the JSON data for payee locations.

        Returns:
        None
        """
        for payee_location in _json:
            payee_location_obj = PayeeLocation(pynab=self.pynab, _json=payee_location)
            self._payee_locations[payee_location_obj.id] = payee_location_obj

    @payee_locations.getter
    def payee_locations(self):
        """
        Retrieves and returns the payee locations associated with the budget.

        If the payee locations have not been fetched yet, it calls the `get_payee_locations` method
        from the `pynab.api` module to retrieve the payee locations and stores them in the `_payee_locations`
        attribute. Subsequent calls to this method will return the cached payee locations.

        Returns:
            dict: A dictionary containing the payee locations associated with the budget.

        """
        if len(self._payee_locations) == 0:
            self._payee_locations = self.pynab.api.get_payee_locations(budget=self)
        return self._payee_locations

    @property
    def category_groups(self):
        """
        Returns the category groups associated with the object.

        :return: The category groups.
        """
        return self._category_groups

    @category_groups.setter
    def category_groups(self, _json: str = ""):
        """
        Parses the given JSON string and creates CategoryGroup objects for each category group.

        Args:
            _json (str): The JSON string containing the category groups.

        Returns:
            None
        """
        for category_group in _json:
            category_group_obj = CategoryGroup(pynab=self.pynab, _json=category_group)
            self._category_groups[category_group_obj.id] = category_group_obj

    @category_groups.getter
    def category_groups(self):
        """
        Retrieves the category groups for the budget.

        If the category groups have not been fetched yet, it calls the `get_categories` method of the `pynab.api` object
        passing the current budget as an argument and assigns the result to the `_category_groups` attribute.

        Returns:
            dict: A dictionary containing the category groups for the budget.
        """
        if len(self._category_groups) == 0:
            self._category_groups = self.pynab.api.get_categories(budget=self)
        return self._category_groups

    @property
    def categories(self):
        """
        Returns the categories associated with the object.

        Returns:
            The categories associated with the object.
        """
        return self._categories

    @categories.setter
    def categories(self, _json: str = ""):
        """
        Process the given JSON string and create Category objects for each category.

        Args:
            _json (str): The JSON string containing the categories.

        Returns:
            None
        """
        for category in _json:
            category_obj = Category(pynab=self.pynab, _json=category)
            self._categories[category_obj.id] = category_obj

    @categories.getter
    def categories(self):
        """
        Retrieves the categories associated with the budget.

        If the categories have not been fetched yet, it makes a request to the Pynab API
        to retrieve the budget's categories. The fetched categories are then stored in
        the `_categories` attribute for future use.

        Returns:
            dict: A dictionary containing the budget's categories.
        """
        if len(self._categories) == 0:
            for category_group in self.category_groups.values():
                for id, category in category_group.categories.items():
                    self._categories[id] = category
        return self._categories

    @property
    def months(self):
        """
        Returns the months attribute.

        :return: The months attribute.
        """
        return self._months

    @months.setter
    def months(self, _json: str = ""):
        """
        Process the given JSON string and create Month objects for each month in the JSON.

        Parameters:
            _json (str): The JSON string containing the months data.

        Returns:
            None
        """
        for month in _json:
            month_obj = Month(pynab=self.pynab, _json=month)
            self._months[month_obj.month] = month_obj

    @months.getter
    def months(self):
        """
        Returns the months associated with the budget.

        If the `_months` attribute is empty, it retrieves the months using the `get_months` method from the `pynab.api` module.

        Returns:
            dict: A dictionary containing the months associated with the budget.
        """
        if len(self._months) == 0:
            self._months = self.pynab.api.get_months(budget=self)
        return self._months

    @property
    def transactions(self):
        """
        Returns the transactions associated with the object.

        :return: The transactions associated with the object.
        """
        return self._transactions

    @transactions.setter
    def transactions(self, _json: str = ""):
        """
        Process the given transactions and store them in the `_transactions` dictionary.

        Parameters:
        - _json (str): A string containing the transactions in JSON format.

        Returns:
        - None

        """
        for transaction in _json:
            transaction_obj = Transaction(pynab=self.pynab, _json=transaction)
            self._transactions[transaction_obj.id] = transaction_obj

    @transactions.getter
    def transactions(self):
        """
        Retrieves the transactions associated with the budget.

        If the transactions have not been fetched yet, it calls the `get_transactions` method of the `pynab.api` object
        passing the current budget as a parameter. The fetched transactions are then stored in the `_transactions`
        attribute of the budget object.

        Returns:
            dict: A dictionary containing the fetched transactions.

        """
        if len(self._transactions) == 0:
            self._transactions = self.pynab.api.get_transactions(budget=self)
        return self._transactions

    @property
    def subtransactions(self):
        """
        Returns the subtransactions of the object.

        :return: The subtransactions.
        """
        return self._subtransactions

    @subtransactions.setter
    def subtransactions(self, _json: str = ""):
        """
        Process the subtransactions from the given JSON string and store them in the `_subtransactions` dictionary.

        Parameters:
            _json (str): The JSON string containing the subtransactions.

        Returns:
            None
        """
        for subtransaction in _json:
            subtransaction_obj = SubTransaction(pynab=self.pynab, _json=subtransaction)
            self._subtransactions[subtransaction_obj.id] = subtransaction_obj

    @subtransactions.getter
    def subtransactions(self):
        """
        Retrieves the subtransactions associated with the budget.

        If the subtransactions have not been fetched yet, it fetches them from the API and stores them in the `_subtransactions` attribute.

        Returns:
            dict: A dictionary containing the subtransactions associated with the budget.
        """
        if len(self._subtransactions) == 0:
            budget = self.pynab.api.get_budget(budget=self)
            self._subtransactions = budget.subtransactions
        return self._subtransactions

    @property
    def scheduled_transactions(self):
        """
        Returns the scheduled transactions.

        :return: The scheduled transactions.
        """
        return self._scheduled_transactions

    @scheduled_transactions.setter
    def scheduled_transactions(self, _json: str = ""):
        """
        Adds scheduled transactions to the schema.

        Parameters:
            _json (str): A JSON string representing the scheduled transactions.

        Returns:
            None
        """
        for scheduled_transaction in _json:
            scheduled_transaction_obj = ScheduledTransaction(
                pynab=self.pynab, _json=scheduled_transaction
            )
            self._scheduled_transactions[scheduled_transaction_obj.id] = (
                scheduled_transaction_obj
            )

    @scheduled_transactions.getter
    def scheduled_transactions(self):
        """
        Retrieves the scheduled transactions for the budget.

        If the scheduled transactions have not been fetched yet, it calls the `get_scheduled_transactions` method
        from the `pynab.api` module to fetch them and stores them in the `_scheduled_transactions` attribute.

        Returns:
            dict: A dictionary containing the scheduled transactions for the budget.
        """
        if len(self._scheduled_transactions) == 0:
            self._scheduled_transactions = self.pynab.api.get_scheduled_transactions(
                budget=self
            )
        return self._scheduled_transactions

    @property
    def scheduled_subtransactions(self):
        """
        Returns the scheduled subtransactions.

        :return: The scheduled subtransactions.
        """
        return self._scheduled_subtransactions

    @scheduled_subtransactions.setter
    def scheduled_subtransactions(self, _json: str = ""):
        """
        Process the scheduled subtransactions from the given JSON string and store them in the `_scheduled_subtransactions` dictionary.

        Parameters:
        - _json (str): The JSON string containing the scheduled subtransactions.

        Returns:
        - None
        """
        for scheduled_subtransaction in _json:
            scheduled_subtransaction_obj = ScheduledSubTransaction(
                pynab=self.pynab, _json=scheduled_subtransaction
            )
            self._scheduled_subtransactions[scheduled_subtransaction_obj.id] = (
                scheduled_subtransaction_obj
            )

    @scheduled_subtransactions.getter
    def scheduled_subtransactions(self):
        """
        Retrieves the scheduled subtransactions for the budget.

        If the scheduled subtransactions have not been fetched yet, it fetches them from the API
        and stores them in the `_scheduled_subtransactions` attribute.

        Returns:
            dict: A dictionary containing the scheduled subtransactions.
        """
        if len(self._scheduled_subtransactions) == 0:
            budget = self.pynab.api.get_budget(budget=self)
            self._scheduled_subtransactions = budget.subtransactions
        return self._scheduled_subtransactions

    @property
    def detail(self):
        """
        Retrieves detailed information about the budget.

        Returns:
            The budget object with additional details.
        """
        self = self.pynab.api.get_budget(budget=self)
        return self

    @property
    def settings(self):
        """
        Retrieves the budget settings from the Pynab API.

        If the settings have already been retrieved, it returns the cached settings.
        Otherwise, it makes a request to the Pynab API to fetch the settings.

        Returns:
            The budget settings.

        """
        if self._settings is None:
            self._settings = self.pynab.api.get_budget_settings(budget=self)
        return self._settings


class BudgetSettings:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initialize a new instance of the Schemas class.

        Args:
            pynab: An instance of the Pynab class.
            _json: A JSON string.

        Attributes:
            date_format: An instance of the DateFormat class.
            currency_format: An instance of the CurrencyFormat class.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.date_format: DateFormat = DateFormat(
            pynab=self.pynab, _json=self._json.get("date_format", {})
        )
        self.currency_format: CurrencyFormat = CurrencyFormat(
            pynab=self.pynab, _json=self._json.get("currency_format", {})
        )


class DateFormat:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initializes a new instance of the class.

        Args:
            pynab: An optional parameter representing pynab.
            _json: An optional parameter representing the JSON string.

        Attributes:
            format: A string representing the format, initialized with an empty string.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.format: str = self._json.get("format", "")


class CurrencyFormat:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initialize a new instance of the `ClassName` class.

        Args:
            pynab: An optional parameter representing the `pynab` object.
            _json: An optional parameter representing the JSON string.

        Attributes:
            iso_code (str): The ISO code.
            example_format (str): The example format.
            decimal_digits (int): The number of decimal digits.
            decimal_separator (str): The decimal separator.
            symbol_first (bool): Indicates if the currency symbol should be placed before the value.
            group_separator (str): The group separator.
            currency_symbol (str): The currency symbol.
            display_symbol (bool): Indicates if the currency symbol should be displayed.

        Returns:
            None
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = None

        self.iso_code: str = self._json.get("iso_code", "")
        self.example_format: str = self._json.get("example_format", "")
        self.decimal_digits: int = self._json.get("decimal_digits", 0)
        self.decimal_separator: str = self._json.get("decimal_separator", "")
        self.symbol_first: bool = self._json.get("symbol_first", False)
        self.group_separator: str = self._json.get("group_separator", "")
        self.currency_symbol: str = self._json.get("currency_symbol", "")
        self.display_symbol: bool = self._json.get("display_symbol", False)


class Account:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initializes a new instance of the `schemas` class.

        Args:
            pynab: An instance of the `pynab` class.
            _json: A JSON string.

        Attributes:
            id (str): The ID of the schema.
            name (str): The name of the schema.
            type (enums.AccountType): The type of the schema.
            on_budget (bool): Indicates if the schema is on budget.
            closed (bool): Indicates if the schema is closed.
            note (str): The note associated with the schema.
            balance (int): The balance of the schema.
            cleared_balance (int): The cleared balance of the schema.
            uncleared_balance (int): The uncleared balance of the schema.
            transfer_payee_id (str): The ID of the transfer payee.
            direct_import_linked (bool): Indicates if the schema is directly imported.
            direct_import_in_error (str): The error associated with direct import.
            last_reconciled_at (datetime): The last reconciled date of the schema.
            debt_original_balance (int): The original balance of the debt.
            debt_interest_rates (DebtInterestRates): The interest rates of the debt.
            debt_minimum_payments (DebtMinimumPayments): The minimum payments of the debt.
            debt_escrow_amounts (DebtEscrowAmounts): The escrow amounts of the debt.
            deleted (bool): Indicates if the schema is deleted.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.name: str = self._json.get("name", "")
        self.type: enums.AccountType = enums.AccountType(self._json.get("type", ""))
        self.on_budget: bool = self._json.get("on_budget", False)
        self.closed: bool = self._json.get("closed", False)
        self.note: str = self._json.get("note", "")
        self.balance: int = self._json.get("balance", 0)
        self.cleared_balance: int = self._json.get("cleared_balance", 0)
        self.uncleared_balance: int = self._json.get("uncleared_balance", 0)
        self.transfer_payee_id: str = self._json.get("transfer_payee_id", "")
        self.direct_import_linked: bool = self._json.get("direct_import_linked", False)
        self.direct_import_in_error: str = self._json.get("direct_import_in_error", "")
        self.last_reconciled_at: datetime = datetime.fromisoformat(
            self._json.get("last_reconciled_at", constants.EPOCH) or constants.EPOCH
        )
        self.debt_original_balance: int = self._json.get("debt_original_balance", 0)
        self.debt_interest_rates: DebtInterestRates = DebtInterestRates(
            pynab=self.pynab,
            budget=self.budget,
            account=self,
            _json=self._json.get("debt_interest_rates", {}),
        )
        self.debt_minimum_payments: DebtMinimumPayments = DebtMinimumPayments(
            pynab=self.pynab,
            budget=self.budget,
            account=self,
            _json=self._json.get("debt_minimum_payments", {}),
        )
        self.debt_escrow_amounts: DebtEscrowAmounts = DebtEscrowAmounts(
            pynab=self.pynab,
            budget=self.budget,
            account=self,
            _json=self._json.get("debt_escrow_amounts", {}),
        )
        self.deleted: bool = self._json.get("deleted", False)

    @property
    def transfer_payees(self):
        """
        Returns the payee associated with the transfer_payee_id.

        Returns:
            The payee object associated with the transfer_payee_id.
        """
        return self.budget.payees[self.transfer_payee_id]

    @property
    def payees(self):
        """
        Retrieve the payees associated with the budget.

        Returns:
            list: A list of payees associated with the budget.

        """
        return self.budget.payees.by(field="id", value=self.id, first=False)

    @property
    def payee_locations(self):
        """
        Retrieves the locations associated with each payee.

        Returns:
            A list of payee locations.
        """
        for payee in self.payees.values():
            return self.budget.payee_locations.by(
                field="payee_id", value=payee.id, first=False
            )

    @property
    def transactions(self):
        """
        Retrieve transactions associated with the account.

        Returns:
            list: A list of transactions associated with the account.
        """
        return self.budget.transactions.by(
            field="account_id", value=self.id, first=False
        )

    @property
    def scheduled_transactions(self):
        """
        Retrieves the scheduled transactions associated with the account.

        Returns:
            list: A list of scheduled transactions.
        """
        return self.budget.scheduled_transactions.by(
            field="account_id", value=self.id, first=False
        )


class DebtInterestRates:
    def __init__(
        self,
        pynab=None,
        budget: Budget = None,
        account: Account = None,
        _json: str = None,
    ):
        """
        Initializes a new instance of the class.

        Args:
            pynab: The pynab object.
            _json: The JSON string.

        Attributes:
            additionalProp1 (int): The value of additionalProp1 from the JSON, defaulting to 0 if not present.
            additionalProp2 (int): The value of additionalProp2 from the JSON, defaulting to 0 if not present.
            additionalProp3 (int): The value of additionalProp3 from the JSON, defaulting to 0 if not present.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget
        self.account = account

        self.additionalProp1: int = self._json.get("additionalProp1", 0)
        self.additionalProp2: int = self._json.get("additionalProp2", 0)
        self.additionalProp3: int = self._json.get("additionalProp3", 0)


class DebtMinimumPayments:
    def __init__(
        self,
        pynab=None,
        budget: Budget = None,
        account: Account = None,
        _json: str = None,
    ):
        """
        Initializes a new instance of the Schema class.

        Args:
            pynab: An instance of the Pynab class.
            _json: A JSON string.

        Attributes:
            additionalProp1: An integer representing additional property 1.
            additionalProp2: An integer representing additional property 2.
            additionalProp3: An integer representing additional property 3.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget
        self.account = account

        self.additionalProp1: int = self._json.get("additionalProp1", 0)
        self.additionalProp2: int = self._json.get("additionalProp2", 0)
        self.additionalProp3: int = self._json.get("additionalProp3", 0)


class DebtEscrowAmounts:
    def __init__(
        self,
        pynab=None,
        budget: Budget = None,
        account: Account = None,
        _json: str = None,
    ):
        """
        Initializes a new instance of the class.

        Args:
            pynab: The pynab object.
            _json: The JSON string.

        Attributes:
            additionalProp1: The value of additionalProp1, defaulting to 0 if not present in the JSON.
            additionalProp2: The value of additionalProp2, defaulting to 0 if not present in the JSON.
            additionalProp3: The value of additionalProp3, defaulting to 0 if not present in the JSON.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget
        self.account = account

        self.additionalProp1: int = self._json.get("additionalProp1", 0)
        self.additionalProp2: int = self._json.get("additionalProp2", 0)
        self.additionalProp3: int = self._json.get("additionalProp3", 0)


class Payee:
    def __init__(
        self,
        pynab=None,
        budget: Budget = None,
        _json: str = None,
    ):
        """
        Initializes a new instance of the `schemas` class.

        Args:
            pynab: An instance of the `pynab` class.
            _json: A JSON string.

        Attributes:
            id (str): The ID of the schema.
            name (str): The name of the schema.
            transfer_account_id (str): The ID of the transfer account.
            deleted (bool): Indicates if the schema is deleted or not.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.name: str = self._json.get("name", "")
        self.transfer_account_id: str = self._json.get("transfer_account_id", "")
        self.deleted: bool = self._json.get("deleted", False)

    @property
    def transfer_account(self):
        """
        Retrieves the account associated with the transfer_account_id.

        Returns:
            Account: The account associated with the transfer_account_id.
        """
        return self.budget.accounts[self.transfer_account_id]

    @property
    def transactions(self):
        """
        Retrieve transactions associated with the payee.

        Returns:
            list: A list of transactions associated with the payee.
        """
        return self.budget.transactions.by(field="payee_id", value=self.id, first=False)

    @property
    def payee_locations(self):
        """
        Retrieves the payee locations associated with the current payee.

        Returns:
            A list of payee locations.

        """
        return self.budget.payee_locations.by(
            field="payee_id", value=self.id, first=False
        )

    @property
    def scheduled_transactions(self):
        """
        Retrieve all scheduled transactions associated with the payee.

        Returns:
            list: A list of scheduled transactions.
        """
        return self.budget.scheduled_transactions.by(
            field="payee_id", value=self.id, first=False
        )

    def subtransactions(self):
        """
        Retrieves subtransactions associated with the current budget.

        Returns:
            list: A list of subtransactions matching the specified criteria.
        """
        return self.budget.subtransactions.by(
            field="payee_id", value=self.id, first=False
        )

    def scheduled_subtransactions(self):
        """
        Retrieves the scheduled subtransactions associated with the current payee.

        Returns:
            A list of scheduled subtransactions.

        """
        return self.budget.scheduled_subtransactions.by(
            field="payee_id", value=self.id, first=False
        )


class PayeeLocation:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initializes a new instance of the class.

        Args:
            pynab: An optional parameter representing the pynab object.
            _json: An optional parameter representing the JSON string.

        Attributes:
            id (str): The ID of the object.
            payee_id (str): The ID of the payee.
            latitude (str): The latitude value.
            longitude (str): The longitude value.
            deleted (bool): A flag indicating if the object is deleted.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.payee_id: str = self._json.get("payee_id", "")
        self.latitude: str = self._json.get("latitude", "")
        self.longitude: str = self._json.get("longitude", "")
        self.deleted: bool = self._json.get("deleted", False)

    @property
    def payee(self):
        """
        Returns the payee associated with the transaction.

        Returns:
            Payee: The payee object associated with the transaction.
        """
        return self.budget.payees[self.payee_id]


class CategoryGroup:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initializes a new instance of the Schema class.

        Args:
            pynab: An instance of the Pynab class.
            _json: A JSON string representing the schema.

        Attributes:
            id (str): The ID of the schema.
            name (str): The name of the schema.
            hidden (bool): Indicates if the schema is hidden.
            deleted (bool): Indicates if the schema is deleted.
            categories (dict): A dictionary of Category objects, where the keys are the category IDs.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.name: str = self._json.get("name", "")
        self.hidden: bool = self._json.get("hidden", False)
        self.deleted: bool = self._json.get("deleted", False)
        self.categories = utils._dict()
        for category_json in _json.get("categories", []):
            category = Category(pynab=self.pynab, _json=category_json)
            self.categories[category.id] = category


class Category:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initializes a new instance of the Schema class.

        Args:
            pynab: An instance of the Pynab class.
            _json: A JSON string representing the schema.

        Attributes:
            id (str): The ID of the schema.
            category_group_id (str): The ID of the category group.
            category_group_name (str): The name of the category group.
            name (str): The name of the schema.
            hidden (bool): Indicates if the schema is hidden.
            original_category_group_id (str): The ID of the original category group.
            note (str): The note associated with the schema.
            budgeted (int): The budgeted amount for the schema.
            activity (int): The activity amount for the schema.
            balance (int): The balance amount for the schema.
            goal_type (GoalType): The type of goal for the schema.
            goal_needs_whole_amount (bool): Indicates if the goal needs the whole amount.
            goal_day (int): The day of the goal.
            goal_cadence (int): The cadence of the goal.
            goal_cadence_frequency (int): The frequency of the goal cadence.
            goal_creation_month (date): The creation month of the goal.
            goal_target (int): The target amount of the goal.
            goal_target_month (date): The target month of the goal.
            goal_percentage_complete (int): The percentage complete of the goal.
            goal_months_to_budget (int): The number of months to budget for the goal.
            goal_under_funded (int): The under-funded amount of the goal.
            goal_overall_funded (int): The overall funded amount of the goal.
            goal_overall_left (int): The overall left amount of the goal.
            deleted (bool): Indicates if the schema is deleted.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.category_group_id: str = self._json.get("category_group_id", "")
        self.category_group_name: str = self._json.get("category_group_name", "")
        self.name: str = self._json.get("name", "")
        self.hidden: bool = self._json.get("hidden", False)
        self.original_category_group_id: str = self._json.get(
            "original_category_group_id", ""
        )
        self.note: str = self._json.get("note", "")
        self.budgeted: int = self._json.get("budgeted", 0)
        self.activity: int = self._json.get("activity", 0)
        self.balance: int = self._json.get("balance", 0)
        self.goal_type: enums.GoalType = enums.GoalType(
            self._json.get("goal_type", None)
        )
        self.goal_needs_whole_amount: bool = self._json.get(
            "goal_needs_whole_amount", False
        )
        self.goal_day: int = self._json.get("goal_day", 0)
        self.goal_cadence: int = self._json.get("goal_cadence", 0)
        self.goal_cadence_frequency: int = self._json.get("goal_cadence_frequency", 0)
        self.goal_creation_month: date = isoparse(
            self._json.get("goal_creation_month", constants.EPOCH) or constants.EPOCH
        ).date()
        self.goal_target: int = self._json.get("goal_target", 0)
        self.goal_target_month: date = isoparse(
            self._json.get("goal_target_month", constants.EPOCH) or constants.EPOCH
        ).date()
        self.goal_percentage_complete: int = self._json.get(
            "goal_percentage_complete", 0
        )
        self.goal_months_to_budget: int = self._json.get("goal_months_to_budget", 0)
        self.goal_under_funded: int = self._json.get("goal_under_funded", 0)
        self.goal_overall_funded: int = self._json.get("goal_overall_funded", 0)
        self.goal_overall_left: int = self._json.get("goal_overall_left", 0)
        self.deleted: bool = self._json.get("deleted", False)

    @property
    def category_group(self):
        """
        Returns the category group associated with the current budget category.

        Returns:
            CategoryGroup: The category group object associated with the current budget category.
        """
        return self.budget.category_groups[self.category_group_id]

    @property
    def original_category_group(self):
        """
        Returns the original category group associated with the transaction.

        Returns:
            CategoryGroup: The original category group object.
        """
        return self.budget.category_groups[self.original_category_group_id]

    @property
    def transactions(self):
        """
        Retrieve transactions associated with the category.

        Returns:
            list: A list of transactions associated with the category.
        """
        return self.budget.transactions.by(
            field="category_id", value=self.id, first=False
        )

    @property
    def subtransactions(self):
        """
        Retrieves the subtransactions associated with the current category.

        Returns:
            list: A list of subtransactions belonging to the category.
        """
        return self.budget.subtransactions.by(
            field="category_id", value=self.id, first=False
        )

    @property
    def scheduled_transactions(self):
        """
        Retrieves the scheduled transactions associated with the category.

        Returns:
            A list of scheduled transactions.
        """
        return self.budget.scheduled_transactions.by(
            field="category_id", value=self.id, first=False
        )

    @property
    def scheduled_subtransactions(self):
        """
        Retrieves the scheduled subtransactions associated with the category.

        Returns:
            list: A list of scheduled subtransactions.
        """
        return self.budget.scheduled_subtransactions.by(
            field="category_id", value=self.id, first=False
        )


class Month:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initializes a new instance of the Schema class.

        Args:
            pynab: An optional parameter representing the Pynab object.
            _json: An optional parameter representing the JSON string.

        Attributes:
            month (date): The month of the schema.
            note (str): The note associated with the schema.
            income (int): The income value of the schema.
            budgeted (int): The budgeted value of the schema.
            activity (int): The activity value of the schema.
            to_be_budgeted (int): The "to be budgeted" value of the schema.
            age_of_money (int): The age of money value of the schema.
            deleted (bool): A flag indicating whether the schema is deleted or not.
            categories (dict): A dictionary containing the categories associated with the schema.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.month: date = isoparse(
            self._json.get("month", constants.EPOCH) or constants.EPOCH
        ).date()
        self.note: str = self._json.get("note", "")
        self.income: int = self._json.get("income", 0)
        self.budgeted: int = self._json.get("budgeted", 0)
        self.activity: int = self._json.get("activity", 0)
        self.to_be_budgeted: int = self._json.get("to_be_budgeted", 0)
        self.age_of_money: int = self._json.get("age_of_money", 0)
        self.deleted: bool = self._json.get("deleted", False)
        self.categories = utils._dict()
        for category_json in _json.get("categories", []):
            category = Category(pynab=self.pynab, _json=category_json)
            self.categories[category.id] = category


class Transaction:
    def __init__(self, pynab=None, budget: Budget = None, _json: dict = None):
        """
        Initializes a new instance of the Transaction class.

        Args:
            pynab (Optional[Pynab]): The Pynab instance.
            _json (Optional[dict]): The JSON representation of the transaction.

        Attributes:
            id (str): The ID of the transaction.
            date (date): The date of the transaction.
            amount (int): The amount of the transaction.
            memo (str): The memo of the transaction.
            cleared (TransactionClearedStatus): The cleared status of the transaction.
            approved (bool): Indicates if the transaction is approved.
            flag_color (TransactionFlagColor): The flag color of the transaction.
            flag_name (str): The flag name of the transaction.
            account_id (str): The ID of the account associated with the transaction.
            payee_id (str): The ID of the payee associated with the transaction.
            category_id (str): The ID of the category associated with the transaction.
            transfer_account_id (str): The ID of the transfer account associated with the transaction.
            transfer_transaction_id (str): The ID of the transfer transaction associated with the transaction.
            matched_transaction_id (str): The ID of the matched transaction associated with the transaction.
            import_id (str): The import ID of the transaction.
            import_payee_name (str): The import payee name of the transaction.
            import_payee_name_original (str): The original import payee name of the transaction.
            debt_transaction_type (str): The debt transaction type of the transaction.
            deleted (bool): Indicates if the transaction is deleted.
            account_name (str): The name of the account associated with the transaction.
            payee_name (str): The name of the payee associated with the transaction.
            category_name (str): The name of the category associated with the transaction.
            subtransactions (dict): A dictionary of subtransactions associated with the transaction.
        """
        ...
        self.pynab = pynab
        self._json: dict = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.date: date = isoparse(
            self._json.get("date", constants.EPOCH) or constants.EPOCH
        ).date()
        self.amount: int = self._json.get("amount", 0)
        self.memo: str = self._json.get("memo", "")
        self.cleared: enums.TransactionClearedStatus = enums.TransactionClearedStatus(
            self._json.get("cleared", "")
        )
        self.approved: bool = self._json.get("approved", False)
        self.flag_color: enums.TransactionFlagColor = enums.TransactionFlagColor(
            self._json.get("flag_color", "")
        )
        self.flag_name: str = self._json.get("flag_name", "")
        self.account_id: str = self._json.get("account_id", "")
        self.payee_id: str = self._json
        self.category_id: str = self._json.get("category_id", "")
        self.transfer_account_id: str = self._json.get("transfer_account_id", "")
        self.transfer_transaction_id: str = self._json.get(
            "transfer_transaction_id", ""
        )
        self.matched_transaction_id: str = self._json.get("matched_transaction_id", "")
        self.import_id: str = self._json.get("import_id", "")
        self.import_payee_name: str = self._json.get("import_payee_name", "")
        self.import_payee_name_original: str = self._json.get(
            "import_payee_name_original", ""
        )
        self.debt_transaction_type: str = self._json.get("debt_transaction_type", "")
        self.deleted: bool = self._json.get("deleted", False)
        self.account_name: str = self._json.get("account_name", "")
        self.payee_name: str = self._json.get("payee_name", "")
        self.category_name: str = self._json.get("category_name", "")
        self.subtransactions = utils._dict()
        for subtransaction in self._json.get("subtransactions", []):
            self.subtransactions[subtransaction["id"]] = SubTransaction(
                pynab=self.pynab, _json=subtransaction
            )

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "amount": self.amount,
            "memo": self.memo,
            "cleared": self.cleared.value,
            "approved": self.approved,
            "flag_color": self.flag_color.value,
            "flag_name": self.flag_name,
            "account_id": self.account_id,
            "payee_id": self.payee_id,
            "category_id": self.category_id,
            "transfer_account_id": self.transfer_account_id,
            "transfer_transaction_id": self.transfer_transaction_id,
            "matched_transaction_id": self.matched_transaction_id,
            "import_id": self.import_id,
            "import_payee_name": self.import_payee_name,
            "import_payee_name_original": self.import_payee_name_original,
            "debt_transaction_type": self.debt_transaction_type,
            "deleted": self.deleted,
            "account_name": self.account_name,
            "payee_name": self.payee_name,
            "category_name": self.category_name,
            "subtransactions": [
                subtransaction.to_dict() for subtransaction in self.subtransactions
            ],
        }

    def to_json(self, indent: int = 4):
        """
        Convert the object to a JSON string representation.

        Args:
            indent (int, optional): The number of spaces to use for indentation. Defaults to 4.

        Returns:
            str: The JSON string representation of the object.
        """
        return json.dumps(self.to_dict(), cls=utils.CustomJsonEncoder, indent=indent)

    @property
    def account(self):
        """
        Returns the account associated with the current instance.
        """
        return self.budget.accounts[self.account_id]

    @property
    def payee(self):
        """
        Returns the payee associated with the transaction.

        Returns:
            Payee: The payee object associated with the transaction.
        """
        return self.budget.payees[self.payee_id]

    @property
    def categories(self):
        """
        Retrieve the categories associated with the budget.

        Returns:
            list: A list of categories associated with the budget.
        """
        return self.budget.categories.by(
            field="id", value=self.category_id, first=False
        )

    @property
    def transfer_account(self):
        """
        Returns the account associated with the transfer_account_id.

        Returns:
            Account: The account associated with the transfer_account_id.
        """
        return self.budget.accounts[self.transfer_account_id]

    @property
    def transfer_transaction(self):
        """
        Returns the transfer transaction associated with the current instance.

        Returns:
            Transaction: The transfer transaction object.
        """
        return self.budget.transactions[self.transfer_transaction_id]

    @property
    def matched_transaction(self):
        """
        Returns the matched transaction based on the `matched_transaction_id`.

        Returns:
            Transaction: The matched transaction object.
        """
        return self.budget.transactions[self.matched_transaction_id]


class SubTransaction:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initialize a new instance of the Schema class.

        Args:
            pynab (optional): The pynab object.
            _json (optional): The JSON string.

        Attributes:
            id (str): The ID of the schema.
            transaction_id (str): The ID of the transaction.
            amount (str): The amount of the transaction.
            memo (str): The memo of the transaction.
            payee_id (str): The ID of the payee.
            payee_name (str): The name of the payee.
            category_id (str): The ID of the category.
            category_name (str): The name of the category.
            transfer_account_id (str): The ID of the transfer account.
            transfer_transaction_id (str): The ID of the transfer transaction.
            deleted (str): Indicates if the schema is deleted.
        """
        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.transaction_id: str = self._json.get("transaction_id", "")
        self.amount: str = self._json.get("amount", 0)
        self.memo: str = self._json.get("memo", "")
        self.payee_id: str = self._json.get("payee_id", "")
        self.payee_name: str = self._json.get("payee_name", "")
        self.category_id: str = self._json.get("category_id", "")
        self.category_name: str = self._json.get("category_name", "")
        self.transfer_account_id: str = self._json.get("transfer_account_id", "")
        self.transfer_transaction_id: str = self._json.get(
            "transfer_transaction_id", ""
        )
        self.deleted: str = self._json.get("deleted", False)

    def transaction(self):
        """
        Returns the transaction associated with the current transaction_id.

        Returns:
            Transaction: The transaction object.
        """
        return self.budget.transactions[self.transaction_id]

    @property
    def payee(self):
        """
        Returns the payee associated with the transaction.

        Returns:
            Payee: The payee object associated with the transaction.
        """
        return self.budget.payees[self.payee_id]

    @property
    def category(self):
        """
        Returns the category associated with the current instance.

        Returns:
            Category: The category object associated with the current instance.
        """
        return self.budget.categories[self.category_id]

    @property
    def transfer_account(self):
        """
        Retrieves the account associated with the transfer_account_id.

        Returns:
            Account: The account associated with the transfer_account_id.
        """
        return self.budget.accounts[self.transfer_account_id]

    @property
    def transfer_transaction(self):
        """
        Retrieves the transfer transaction associated with the current instance.

        Returns:
            Transaction: The transfer transaction object.
        """
        return self.budget.transactions[self.transfer_transaction_id]


class ScheduledTransaction:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None):
        """
        Initializes a new instance of the class.

        Args:
            pynab: An optional parameter representing the pynab object.
            _json: An optional parameter representing the JSON string.

        Attributes:
            id (str): The ID of the object.
            date_first (date): The first date associated with the object.
            date_next (date): The next date associated with the object.
            frequency (enums.Frequency): The frequency of the object.
            amount (int): The amount of the object.
            memo (str): The memo of the object.
            flag_color (enums.TransactionFlagColor): The flag color of the object.
            flag_name (str): The flag name of the object.
            account_id (str): The account ID associated with the object.
            payee_id (str): The payee ID associated with the object.
            category_id (str): The category ID associated with the object.
            transfer_account_id (str): The transfer account ID associated with the object.
            scheduled_subtransactions (dict): A dictionary of scheduled subtransactions associated with the object.
            deleted (bool): A boolean value indicating whether the object is deleted or not.
        """

        self.pynab = pynab
        self._json: str = _json

        self.budget = budget

        self.id: str = self._json.get("id", "")
        self.date_first: date = isoparse(
            self._json.get("date_first", constants.EPOCH)
        ).date()
        self.date_next: date = isoparse(
            self._json.get("date_next", constants.EPOCH)
        ).date()
        self.frequency: enums.Frequency = enums.Frequency(
            self._json.get("frequency", "")
        )
        self.amount: int = self._json.get("amount", 0)
        self.memo: str = self._json.get("memo", "")
        self.flag_color: enums.TransactionFlagColor = enums.TransactionFlagColor(
            self._json.get("flag_color", "")
        )
        self.flag_name: str = self._json.get("flag_name", "")
        self.account_id: str = self._json.get("account_id", "")
        self.payee_id: str = self._json.get("payee_id", "")
        self.category_id: str = self._json.get("category_id", "")
        self.transfer_account_id: str = self._json.get("transfer_account_id", "")
        self.scheduled_subtransactions = utils._dict()
        for scheduled_subtransaction_json in _json.get("scheduled_subtransactions", []):
            scheduled_subtransaction = ScheduledSubTransaction(
                _json=scheduled_subtransaction_json
            )
            self.scheduled_subtransactions[scheduled_subtransaction.id] = (
                scheduled_subtransaction
            )
        self.deleted: bool = self._json.get("deleted", False)

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """
        return {
            "id": self.id,
            "date_first": self.date_first.isoformat(),
            "date_next": self.date_next.isoformat(),
            "date": self.date_next.isoformat(),
            "frequency": self.frequency.value,
            "amount": self.amount,
            "memo": self.memo,
            "flag_color": self.flag_color.value,
            "flag_name": self.flag_name,
            "account_id": self.account_id,
            "payee_id": self.payee_id,
            "payee_name": self.payee.name,
            "category_id": self.category_id,
            "transfer_account_id": self.transfer_account_id,
            "subtransactions": {
                k: v.to_dict() for k, v in self.scheduled_subtransactions.items()
            },
            "deleted": self.deleted,
        }

    def to_json(self, indent: int = 4):
        """
        Convert the object to a JSON string representation.

        Args:
            indent (int, optional): The number of spaces to use for indentation. Defaults to 4.

        Returns:
            str: The JSON string representation of the object.
        """
        return json.dumps(self.to_dict(), cls=utils.CustomJsonEncoder, indent=indent)

    @property
    def account(self):
        """
        Returns the account associated with the current instance.
        """
        return self.budget.accounts[self.account_id]

    @property
    def payee(self):
        """
        Returns the payee associated with the transaction.

        Returns:
            Payee: The payee object associated with the transaction.
        """
        return self.budget.payees[self.payee_id]

    @property
    def category(self):
        """
        Returns the category associated with the current instance.

        Returns:
            Category: The category object associated with the current instance.
        """
        return self.budget.categories[self.category_id]

    @property
    def transfer_account(self):
        """
        Returns the account associated with the transfer_account_id.

        Returns:
            Account: The account associated with the transfer_account_id.
        """
        return self.budget.accounts[self.transfer_account_id]


class ScheduledSubTransaction:
    def __init__(self, pynab=None, _json: str = None):
        """
        Initializes a new instance of the Schema class.

        Args:
            pynab: An instance of the Pynab class.
            _json: A JSON string representing the schema.

        Attributes:
            id (str): The ID of the schema.
            scheduled_transaction_id (str): The ID of the scheduled transaction.
            amount (int): The amount of the schema.
            memo (str): The memo of the schema.
            payee_id (str): The ID of the payee.
            category_id (str): The ID of the category.
            transfer_account_id (str): The ID of the transfer account.
            deleted (bool): Indicates if the schema is deleted.
        """
        self.pynab = pynab
        self._json: str = _json

        self.id: str = self._json.get("id", "")
        self.scheduled_transaction_id: str = (
            (self._json.get("scheduled_transaction_id", "")),
        )
        self.amount: int = self._json.get("amount", 0)
        self.memo: str = self._json.get("memo", "")
        self.payee_id: str = self._json.get("payee_id", "")
        self.category_id: str = self._json.get("category_id", "")
        self.transfer_account_id: str = self._json.get("transfer_account_id", "")
        self.deleted: bool = self._json.get("deleted", False)

    @property
    def scheduled_transaction(self):
        """
        Returns the scheduled transaction associated with the current instance.

        Returns:
            The scheduled transaction object.
        """
        return self.budget.scheduled_transactions[self.scheduled_transaction_id]

    @property
    def payee(self):
        """
        Returns the payee associated with the transaction.
        """
        return self.budget.payees[self.payee_id]

    @property
    def category(self):
        """
        Returns the category associated with the current instance.

        Returns:
            Category: The category object associated with the current instance.
        """
        return self.budget.categories[self.category_id]

    @property
    def transfer_account(self):
        """
        Returns the account associated with the transfer_account_id.

        Returns:
            Account: The account associated with the transfer_account_id.
        """
        return self.budget.accounts[self.transfer_account_id]
