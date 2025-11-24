from ynab_py import api
from ynab_py import schemas
from ynab_py import YnabPy
from ynab_py import enums
import pytest
import logging
from dotenv import dotenv_values


TEST_BUDGET_NAME = "test_budget"
TEST_ACCOUNT_NAME = "test_account"
TEST_CATEGORY_GROUP_NAME = "test_category_group"
TEST_CATEGORY_NAME = "test_category"
TEST_PAYEE_NAME = "test_payee"
TEST_PAYEE_LOCATION_NAME = "test_payee_location"
TEST_TRANSACTION_NAME = "test_transaction"
TEST_SCHEDULED_TRANSACTION_NAME = "test_scheduled_transaction"
TEST_PAYEE_CHANGED_NAME = "test_payee_changed"

# get API bearer token from .env
secrets = dotenv_values("testing/.env")
BEARER = secrets["API_KEY"]


@pytest.fixture(scope="module")
def test_ynab_py():
    """
    Test the initialization of the YnabPy class with a bearer token.

    This function creates an instance of the YnabPy class using a provided
    bearer token and returns the instance.

    Returns:
        YnabPy: An instance of the YnabPy class initialized with the bearer token.
    """
    test_ynab_py = YnabPy(bearer=BEARER)
    return test_ynab_py


def test_ynab_py_init(test_ynab_py):
    """
    Test the initialization of the YnabPy instance.

    Args:
        test_ynab_py: The YnabPy instance to be tested.

    Asserts:
        - The test_ynab_py instance is not None.
        - The test_ynab_py instance is not an instance of schemas.Error.
        - The test_ynab_py instance is an instance of YnabPy.
    """
    assert test_ynab_py is not None
    assert not isinstance(test_ynab_py, schemas.Error)
    assert isinstance(test_ynab_py, YnabPy)


@pytest.fixture(scope="module")
def user(test_ynab_py):
    """
    Fetches the user information from the API.

    Args:
        test_ynab_py: An instance of the test_ynab_py object which contains the API client.

    Returns:
        dict: A dictionary containing user information retrieved from the API.
    """
    user = test_ynab_py.api.get_user()
    return user


def test_user(user):
    """
    Test the user object.

    This test ensures that the user object is not None, is not an instance of the
    schemas.Error class, and is an instance of the schemas.User class.

    Args:
        user: The user object to be tested.

    Assertions:
        - The user object is not None.
        - The user object is not an instance of schemas.Error.
        - The user object is an instance of schemas.User.
    """
    assert user is not None
    assert not isinstance(user, schemas.Error)
    assert isinstance(user, schemas.User)


@pytest.fixture(scope="module")
def budgets(test_ynab_py):
    """
    Fetches the budgets from the API.

    Args:
        test_ynab_py: An instance of the test client for ynab_py.

    Returns:
        A list of budgets retrieved from the API with accounts excluded.
    """
    budgets = test_ynab_py.api.get_budgets(include_accounts=False)
    return budgets


def test_budgets(budgets):
    """
    Test the budgets data structure.

    This test ensures that the `budgets` object is not None and is not an instance of `schemas.Error`.
    It also verifies that each item in the `budgets` dictionary is an instance of `schemas.Budget`.

    Args:
        budgets (dict): A dictionary where keys are budget IDs and values are budget objects.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    assert budgets is not None
    assert not isinstance(budgets, schemas.Error)
    for budget_id, budget in budgets.items():
        assert isinstance(budget, schemas.Budget)


@pytest.fixture(scope="module")
def budget(test_ynab_py, budgets):
    """
    Retrieve a specific budget from the provided budgets.

    This function iterates through the given budgets and identifies the budget
    whose name contains the predefined `TEST_BUDGET_NAME`. It then fetches and
    returns the budget details using the `test_pynab` API.

    Args:
        test_pynab (object): An instance of the ynab_py test API.
        budgets (dict): A dictionary of budget objects, where keys are budget IDs
                        and values are budget instances.

    Returns:
        object: The budget instance that matches the `TEST_BUDGET_NAME`.
    """
    for budget_id, budget in budgets.items():
        if TEST_BUDGET_NAME in budget.name:
            test_budget_id = budget_id

    test_budget = test_ynab_py.api.get_budget(budget_id=test_budget_id)
    return test_budget


def test_budget(budget):
    """
    Test the budget object.

    This test ensures that the budget object is not None, is not an instance of
    schemas.Error, and is an instance of schemas.Budget.

    Args:
        budget: The budget object to be tested.
    """
    assert budget is not None
    assert not isinstance(budget, schemas.Error)
    assert isinstance(budget, schemas.Budget)


@pytest.fixture(scope="module")
def budget_settings(test_ynab_py, budget):
    """
    Retrieve the budget settings for a given budget.

    Args:
        test_pynab (object): An instance of the test_pynab class, which provides access to the API.
        budget (str): The identifier of the budget for which settings are to be retrieved.

    Returns:
        dict: A dictionary containing the budget settings.
    """
    budget_settings = test_ynab_py.api.get_budget_settings(budget=budget)
    return budget_settings


def test_budget_settings(budget_settings):
    """
    Test the budget_settings function.

    This test ensures that the budget_settings object is not None, is not an instance of schemas.Error,
    and is an instance of schemas.BudgetSettings.

    Args:
        budget_settings: The budget settings object to be tested.

    Asserts:
        - budget_settings is not None.
        - budget_settings is not an instance of schemas.Error.
        - budget_settings is an instance of schemas.BudgetSettings.
    """
    assert budget_settings is not None
    assert not isinstance(budget_settings, schemas.Error)
    assert isinstance(budget_settings, schemas.BudgetSettings)


@pytest.fixture(scope="module")
def accounts(test_ynab_py, budget):
    """
    Fetches the accounts for a given budget.

    Args:
        test_ynab_py: An instance of the test_ynab_py object which provides access to the API.
        budget: The budget identifier for which accounts are to be fetched.

    Returns:
        A list of accounts associated with the specified budget.
    """
    accounts = test_ynab_py.api.get_accounts(budget=budget)
    return accounts


def test_accounts(accounts):
    """
    Test the accounts data structure.

    Args:
        accounts (dict): A dictionary of account data where keys are account IDs and values are account objects.

    Assertions:
        - The accounts object is not None.
        - The accounts object is not an instance of schemas.Error.
        - Each item in the accounts dictionary is an instance of schemas.Account.
    """
    assert accounts is not None
    assert not isinstance(accounts, schemas.Error)
    for account_id, account in accounts.items():
        assert isinstance(account, schemas.Account)


@pytest.fixture(scope="module")
def account(test_ynab_py, budget, accounts):
    """
    Retrieve a specific account from the provided accounts dictionary.

    This function iterates through the given accounts and finds the account
    whose name contains the predefined `TEST_ACCOUNT_NAME`. It then fetches
    the account details using the `test_pynab` API.

    Args:
        test_pynab (object): An instance of the ynab_py test API.
        budget (str): The budget identifier.
        accounts (dict): A dictionary of account objects, where keys are account IDs
                         and values are account instances.

    Returns:
        object: The account object corresponding to the found account ID.
    """
    for account_id, account in accounts.items():
        if TEST_ACCOUNT_NAME in account.name:
            test_account_id = account_id
    test_account = test_ynab_py.api.get_account(
        budget=budget,
        account_id=test_account_id,
    )
    return test_account


def test_account(account):
    """
    Test the account object.

    This test ensures that the provided account object is valid and correctly
    typed. It performs the following checks:
    1. The account object is not None.
    2. The account object is not an instance of the Error schema.
    3. The account object is an instance of the Account schema.

    Args:
        account: The account object to be tested.
    """
    assert account is not None
    assert not isinstance(account, schemas.Error)
    assert isinstance(account, schemas.Account)


@pytest.fixture(scope="module")
def category_groups(test_ynab_py, budget):
    """
    Retrieve category groups for a given budget.

    Args:
        test_pynab (object): An instance of the test_pynab class, which provides access to the API.
        budget (str): The budget identifier for which to retrieve category groups.

    Returns:
        list: A list of category groups associated with the specified budget.
    """
    category_groups = test_ynab_py.api.get_categories(budget=budget)
    return category_groups


def test_category_groups(category_groups):
    """
    Test the category_groups function.

    This test ensures that the category_groups object is not None and is not an instance of schemas.Error.
    It also verifies that each item in the category_groups dictionary is an instance of schemas.CategoryGroup.

    Args:
        category_groups (dict): A dictionary where keys are category group IDs and values are category group objects.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    assert category_groups is not None
    assert not isinstance(category_groups, schemas.Error)
    for category_group_id, category_group in category_groups.items():
        assert isinstance(category_group, schemas.CategoryGroup)


@pytest.fixture(scope="module")
def category_group(test_ynab_py, budget, category_groups):
    """
    Retrieves a category group from the provided category groups dictionary that matches a specific name.

    Args:
        test_ynab_py: An instance of the test ynab_py object.
        budget: The budget object associated with the category groups.
        category_groups (dict): A dictionary where the keys are category group IDs and the values are category group objects.

    Returns:
        The category group object that matches the specified name, or None if no match is found.
    """
    for category_group_id, category_group in category_groups.items():
        if TEST_CATEGORY_GROUP_NAME in category_group.name:
            return category_group
    return None


@pytest.fixture(scope="module")
def category(test_ynab_py, category_group, budget):
    """
    Retrieve a specific category from a category group in a budget.

    This function iterates through the categories in the provided category group,
    identifies the category with a name matching the predefined `TEST_CATEGORY_NAME`,
    and retrieves its details using the `test_pynab` API.

    Args:
        test_pynab (object): An instance of the test_ynab_py API client.
        category_group (object): The category group containing the categories.
        budget (object): The budget object to which the category belongs.

    Returns:
        object: The category object retrieved from the API.
    """
    for category_id, category in category_group.categories.items():
        if TEST_CATEGORY_NAME in category.name:
            test_category_id = category_id
    test_category = test_ynab_py.api.get_category(
        budget=budget,
        category_id=test_category_id,
    )
    return test_category


def test_category(category):
    """
    Test the validity of a category object.

    Args:
        category (schemas.Category): The category object to be tested.

    Asserts:
        - The category is not None.
        - The category is not an instance of schemas.Error.
        - The category is an instance of schemas.Category.
    """
    assert category is not None
    assert not isinstance(category, schemas.Error)
    assert isinstance(category, schemas.Category)


@pytest.fixture(scope="module")
def category_for_month(test_ynab_py, budget, category):
    """
    Retrieve the category details for the current month from the budget.

    Args:
        test_pynab (object): An instance of the test_ynab_py object which provides access to the API.
        budget (str): The budget identifier from which to retrieve the category details.
        category (str): The category identifier for which details are to be retrieved.

    Returns:
        dict: A dictionary containing the details of the specified category for the current month.
    """
    # Test get_category_for_month
    test_category_for_month = test_ynab_py.api.get_category_for_month(
        budget=budget,
        month="current",
        category=category,
    )
    return test_category_for_month


def test_category_for_month(category_for_month):
    """
    Test the `category_for_month` function.

    This test ensures that the `category_for_month` function returns a valid
    category object for a given month. The test performs the following checks:
    1. Asserts that the `category_for_month` is not None.
    2. Asserts that the `category_for_month` is not an instance of `schemas.Error`.
    3. Asserts that the `category_for_month` is an instance of `schemas.Category`.

    Args:
        category_for_month: The category object for a specific month to be tested.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    assert category_for_month is not None
    assert not isinstance(category_for_month, schemas.Error)
    assert isinstance(category_for_month, schemas.Category)


@pytest.fixture(scope="module")
def payees(test_ynab_py, budget):
    """
    Retrieve the list of payees for a given budget.

    Args:
        test_pynab (object): An instance of the test_pynab class, which provides access to the API.
        budget (str): The budget identifier for which to retrieve the payees.

    Returns:
        list: A list of payees associated with the specified budget.
    """
    payees = test_ynab_py.api.get_payees(budget=budget)
    return payees


def test_payees(payees):
    """
    Test the payees function.

    Args:
        payees: The payees object to be tested.

    Asserts:
        - payees is not None.
        - payees is not an instance of schemas.Error.
    """
    assert payees is not None
    assert not isinstance(payees, schemas.Error)


@pytest.fixture(scope="module")
def payee(budget, test_ynab_py, payees):
    """
    Retrieves a specific payee from the provided payees dictionary and fetches its details using the test_ynab_py API.

    Args:
        budget (str): The budget identifier.
        test_pynab (object): An instance of the test_ynab_py API client.
        payees (dict): A dictionary of payee IDs to payee objects.

    Returns:
        object: The payee object retrieved from the test_ynab_py API.

    Raises:
        AssertionError: If any item in the payees dictionary is not an instance of schemas.Payee.
    """
    for payee_id, payee in payees.items():
        assert isinstance(payee, schemas.Payee)
        if TEST_PAYEE_NAME in payee.name:
            test_payee_id = payee_id
    payee = test_ynab_py.api.get_payee(budget=budget, payee_id=test_payee_id)
    return payee


def test_payee(payee):
    """
    Test the payee object.

    This test ensures that the payee object is not None, is not an instance of
    schemas.Error, and is an instance of schemas.Payee.

    Args:
        payee: The payee object to be tested.

    Assertions:
        - payee is not None.
        - payee is not an instance of schemas.Error.
        - payee is an instance of schemas.Payee.
    """
    assert payee is not None
    assert not isinstance(payee, schemas.Error)
    assert isinstance(payee, schemas.Payee)


@pytest.fixture(scope="module")
def payee_locations(test_ynab_py, budget):
    """
    Retrieve payee locations for a given budget.

    Args:
        test_pynab (object): An instance of the test ynab_py API client.
        budget (str): The budget identifier.

    Returns:
        list: A list of payee locations associated with the specified budget.
    """
    test_budget_payee_locations = test_ynab_py.api.get_budget_payee_locations(
        budget=budget
    )
    return test_budget_payee_locations


def test_payee_locations(payee_locations):
    """
    Test the payee_locations function.

    Args:
        payee_locations (object): The payee locations object to be tested.

    Asserts:
        - payee_locations is not None.
        - payee_locations is not an instance of schemas.Error.
    """
    if payee_locations:
        assert payee_locations is not None
        assert not isinstance(payee_locations, schemas.Error)


def test_payee_location(test_ynab_py, budget, payee_locations):
    """
    Test the retrieval of a specific payee location from the API.

    This test function iterates through a dictionary of payee locations,
    checks if each location is an instance of `schemas.PayeeLocation`,
    and identifies a payee location by name. If a matching payee location
    is found, it retrieves the payee location from the API and performs
    several assertions to ensure the retrieved data is valid.

    Args:
        test_ynab_py: The test fixture providing access to the ynab_py API.
        budget: The budget object to be used in the API call.
        payee_locations: A dictionary of payee locations to search through.

    Assertions:
        - Each payee location in the dictionary is an instance of `schemas.PayeeLocation`.
        - The retrieved payee location is not None.
        - The retrieved payee location is not an instance of `schemas.Error`.
        - The retrieved payee location is an instance of `schemas.PayeeLocation`.
    """
    test_payee_location_id = None
    for payee_location_id, test_payee_location in payee_locations.items():
        assert isinstance(test_payee_location, schemas.PayeeLocation)
        if TEST_PAYEE_LOCATION_NAME in test_payee_location.name:
            test_payee_location_id = payee_location_id
    if test_payee_location_id is not None:
        test_payee_location = test_ynab_py.api.get_payee_location(
            budget=budget,
            payee_location_id=test_payee_location_id,
        )
        assert test_payee_location is not None
        assert not isinstance(test_payee_location, schemas.Error)
        assert isinstance(test_payee_location, schemas.PayeeLocation)


@pytest.fixture(scope="module")
def get_payee_locations(test_ynab_py, budget, payee):
    """
    Retrieve the locations associated with a specific payee within a given budget.

    Args:
        test_pynab (object): An instance of the test_ynab_py object which provides access to the API.
        budget (str): The budget identifier for which the payee locations are to be retrieved.
        payee (str): The payee identifier for which the locations are to be retrieved.

    Returns:
        list: A list of payee locations associated with the specified budget and payee.
    """
    payee_locations = test_ynab_py.api.get_payee_locations(budget=budget, payee=payee)
    return payee_locations


def test_get_payee_locations(get_payee_locations):
    """
    Test the retrieval of payee locations.

    This test checks the following:
    1. The `get_payee_locations` fixture is not None.
    2. The `get_payee_locations` fixture is not an instance of `schemas.Error`.
    3. Each item in the `get_payee_locations` dictionary is an instance of `schemas.PayeeLocation`.

    Args:
        get_payee_locations (dict): A dictionary of payee locations where the key is the payee location ID and the value is an instance of `schemas.PayeeLocation`.
    """
    if get_payee_locations:
        assert get_payee_locations is not None
        assert not isinstance(get_payee_locations, schemas.Error)
        for payee_location_id, payee_location in get_payee_locations.items():
            assert isinstance(payee_location, schemas.PayeeLocation)


@pytest.fixture(scope="module")
def months(test_ynab_py, budget):
    """
    Fetches the months data from the API for a given budget.

    Args:
        test_pynab (object): An instance of the test_pynab class which contains the API client.
        budget (str): The budget identifier for which to fetch the months data.

    Returns:
        list: A list of months data retrieved from the API.
    """
    months = test_ynab_py.api.get_months(budget=budget)
    return months


def test_months(months):
    """
    Test function to validate the 'months' data structure.

    Args:
        months (dict): A dictionary where keys are month IDs and values are instances of schemas.Month.

    Asserts:
        - The 'months' parameter is not None.
        - The 'months' parameter is not an instance of schemas.Error.
        - Each value in the 'months' dictionary is an instance of schemas.Month.
    """
    assert months is not None
    assert not isinstance(months, schemas.Error)
    for month_id, test_month in months.items():
        assert isinstance(test_month, schemas.Month)


@pytest.fixture(scope="module")
def month(test_ynab_py, budget):
    """
    Retrieve the current month's budget data from the API.

    Args:
        test_pynab (object): An instance of the Pynab API client.
        budget (str): The budget ID for which to retrieve the month data.

    Returns:
        dict: The current month's budget data as returned by the API.
    """
    test_month = test_ynab_py.api.get_month(budget=budget, month_id="current")
    return test_month


def test_month(month):
    """
    Test the `month` object.

    Args:
        month (schemas.Month): The month object to be tested.

    Asserts:
        - The month object is not None.
        - The month object is not an instance of `schemas.Error`.
        - The month object is an instance of `schemas.Month`.
    """
    assert month is not None
    assert not isinstance(month, schemas.Error)
    assert isinstance(month, schemas.Month)


@pytest.fixture(scope="module")
def transactions(test_ynab_py, budget):
    """
    Retrieve transactions from the API for a given budget.

    Args:
        test_pynab (object): An instance of the test_pynab class, which provides access to the API.
        budget (str): The budget identifier for which transactions are to be retrieved.

    Returns:
        list: A list of transactions retrieved from the API.
    """
    transactions = test_ynab_py.api.get_transactions(
        budget=budget,
        since_date=None,
        type=None,
    )
    return transactions


def test_transactions(transactions):
    """
    Test the transactions function.

    Args:
        transactions: The transactions data to be tested.

    Asserts:
        - transactions is not None.
        - transactions is not an instance of schemas.Error.
    """
    assert transactions is not None
    assert not isinstance(transactions, schemas.Error)


@pytest.fixture(scope="module")
def import_transactions(test_ynab_py, budget):
    """
    Imports transactions for a given budget using the test_ynab_py API.

    Args:
        test_pynab (object): An instance of the test_pynab class, which provides access to the API.
        budget (str): The budget identifier for which transactions are to be imported.

    Returns:
        list: A list of imported transactions.
    """
    imported_transactions = test_ynab_py.api.import_transactions(budget=budget)
    return imported_transactions


def test_import_transactions(import_transactions):
    """
    Test the import_transactions function.

    This test ensures that the import_transactions function returns a non-None value
    and that the returned value is not an instance of schemas.Error.

    Args:
        import_transactions: The result of the import_transactions function to be tested.

    Assertions:
        - The import_transactions result is not None.
        - The import_transactions result is not an instance of schemas.Error.
    """
    assert import_transactions is not None
    assert not isinstance(import_transactions, schemas.Error)


@pytest.fixture(scope="module")
def transaction(test_ynab_py, budget, transactions):
    """
    Retrieve a specific transaction from a budget.

    This function iterates over a dictionary of transactions, checks if each
    transaction is an instance of `schemas.Transaction`, and identifies the
    transaction with a memo matching `TEST_TRANSACTION_NAME`. It then retrieves
    this transaction using the `test_pynab` API.

    Args:
        test_ynab_py: An instance of the ynab_py test client.
        budget: The budget from which to retrieve the transaction.
        transactions: A dictionary of transactions where the key is the
                      transaction ID and the value is the transaction object.

    Returns:
        The transaction object that matches the specified memo.
    """
    for transaction_id, transaction in transactions.items():
        assert isinstance(transaction, schemas.Transaction)
        if transaction.memo == TEST_TRANSACTION_NAME:
            test_transaction_id = transaction_id
    test_transaction = test_ynab_py.api.get_transaction(
        budget=budget, transaction_id=test_transaction_id
    )
    return test_transaction


def test_transaction(transaction):
    """
    Test the transaction object.

    This test ensures that the transaction object is not None, is not an instance of schemas.Error,
    and is an instance of schemas.Transaction.

    Args:
        transaction: The transaction object to be tested.
    """
    assert transaction is not None
    assert not isinstance(transaction, schemas.Error)
    assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def account_transactions(test_ynab_py, budget, account):
    """
    Retrieve transactions for a specific account within a budget.

    Args:
        test_pynab (object): An instance of the test_pynab class, which provides access to the API.
        budget (str): The ID or name of the budget to retrieve transactions from.
        account (str): The ID or name of the account to retrieve transactions for.

    Returns:
        list: A list of transactions for the specified account within the given budget.
    """
    account_transactions = test_ynab_py.api.get_account_transactions(
        budget=budget,
        account=account,
        since_date=None,
        type=None,
    )
    return account_transactions


def test_account_transactions(account_transactions):
    """
    Test the account_transactions function.

    This test ensures that the account_transactions object is not None,
    is not an instance of schemas.Error, and that each item in the
    account_transactions dictionary is an instance of schemas.Transaction.

    Args:
        account_transactions (dict): A dictionary where keys are transaction IDs
        and values are transaction objects.

    Assertions:
        - account_transactions is not None.
        - account_transactions is not an instance of schemas.Error.
        - Each value in account_transactions is an instance of schemas.Transaction.
    """
    assert account_transactions is not None
    assert not isinstance(account_transactions, schemas.Error)
    for transaction_id, transaction in account_transactions.items():
        assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def category_transactions(test_ynab_py, budget, category):
    """
    Retrieve transactions for a specific category within a budget.

    Args:
        test_pynab (object): The test instance of the ynab_py API.
        budget (str): The budget identifier.
        category (str): The category identifier.

    Returns:
        list: A list of transactions for the specified category.
    """
    category_transactions = test_ynab_py.api.get_category_transactions(
        budget=budget,
        category=category,
        since_date=None,
        type=None,
    )
    return category_transactions


def test_category_transactions(category_transactions):
    """
    Test the category_transactions function.

    This test ensures that the category_transactions object is not None,
    is not an instance of schemas.Error, and that each item in the
    category_transactions dictionary is an instance of schemas.Transaction.

    Args:
        category_transactions (dict): A dictionary where keys are transaction IDs
                                      and values are transaction objects.

    Asserts:
        - category_transactions is not None.
        - category_transactions is not an instance of schemas.Error.
        - Each value in category_transactions is an instance of schemas.Transaction.
    """
    assert category_transactions is not None
    assert not isinstance(category_transactions, schemas.Error)
    for transaction_id, transaction in category_transactions.items():
        assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def payee_transactions(test_ynab_py, budget, payee):
    """
    Retrieve transactions for a specific payee within a given budget.

    Args:
        test_pynab (object): An instance of the test_ynab_py object which provides access to the API.
        budget (str): The budget ID or name to retrieve transactions from.
        payee (str): The payee ID or name to filter transactions by.

    Returns:
        list: A list of transactions associated with the specified payee within the given budget.
    """
    payee_transactions = test_ynab_py.api.get_payee_transactions(
        budget=budget,
        payee=payee,
        since_date=None,
        type=None,
    )
    return payee_transactions


def test_payee_transactions(payee_transactions):
    """
    Test the payee_transactions function.

    This test ensures that the payee_transactions object is not None,
    is not an instance of schemas.Error, and that each item in the
    payee_transactions dictionary is an instance of schemas.Transaction.

    Args:
        payee_transactions (dict): A dictionary where keys are transaction IDs
                                   and values are transaction objects.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    assert payee_transactions is not None
    assert not isinstance(payee_transactions, schemas.Error)
    for transaction_id, transaction in payee_transactions.items():
        assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def month_transactions(test_ynab_py, budget, month):
    """
    Retrieve transactions for a specific month from the API.

    Args:
        test_pynab (object): An instance of the test Pynab API client.
        budget (str): The budget ID to retrieve transactions for.
        month (str): The month to retrieve transactions for in 'YYYY-MM' format.

    Returns:
        list: A list of transactions for the specified month.
    """
    month_transactions = test_ynab_py.api.get_month_transactions(
        budget=budget,
        month=month,
        since_date=None,
        type=None,
    )
    return month_transactions


def test_month_transactions(month_transactions):
    """
    Test the validity of month transactions.

    Args:
        month_transactions (dict): A dictionary of transactions for the month.

    Asserts:
        - The month_transactions is not None.
        - The month_transactions is not an instance of schemas.Error.
        - Each transaction in month_transactions is an instance of schemas.Transaction.
    """
    assert month_transactions is not None
    assert not isinstance(month_transactions, schemas.Error)
    for transaction_id, transaction in month_transactions.items():
        assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def scheduled_transactions(test_ynab_py, budget):
    """
    Retrieve scheduled transactions for a given budget.

    Args:
        test_pynab (object): An instance of the test_pynab class, which provides access to the API.
        budget (str): The budget identifier for which to retrieve scheduled transactions.

    Returns:
        list: A list of scheduled transactions for the specified budget.
    """
    scheduled_transactions = test_ynab_py.api.get_scheduled_transactions(
        budget=budget,
    )
    return scheduled_transactions


def test_scheduled_transactions(scheduled_transactions):
    """
    Test the scheduled transactions.

    This test verifies that the `scheduled_transactions` object is not None and is not an instance of `schemas.Error`.
    It also checks that each item in the `scheduled_transactions` dictionary is an instance of `schemas.ScheduledTransaction`.

    Args:
        scheduled_transactions (dict): A dictionary of scheduled transactions where the key is the transaction ID and the value is the `ScheduledTransaction` object.

    Assertions:
        - `scheduled_transactions` is not None.
        - `scheduled_transactions` is not an instance of `schemas.Error`.
        - Each value in `scheduled_transactions` is an instance of `schemas.ScheduledTransaction`.
    """
    assert scheduled_transactions is not None
    assert not isinstance(scheduled_transactions, schemas.Error)
    for (
        scheduled_transaction_id,
        scheduled_transaction,
    ) in scheduled_transactions.items():
        assert isinstance(scheduled_transaction, schemas.ScheduledTransaction)


@pytest.fixture(scope="module")
def scheduled_transaction(test_ynab_py, budget, scheduled_transactions):
    """
    Retrieve a specific scheduled transaction from a budget.

    This function iterates through a dictionary of scheduled transactions,
    identifies the one that matches a predefined name, and retrieves its details
    using the provided API client.

    Args:
        test_pynab (object): An instance of the API client used to interact with the budget.
        budget (str): The identifier of the budget from which to retrieve the scheduled transaction.
        scheduled_transactions (dict): A dictionary of scheduled transactions where keys are transaction IDs
                                       and values are `schemas.ScheduledTransaction` instances.

    Returns:
        object: The scheduled transaction object retrieved from the API.
    """
    for (
        scheduled_transaction_id,
        scheduled_transaction,
    ) in scheduled_transactions.items():
        assert isinstance(scheduled_transaction, schemas.ScheduledTransaction)
        if TEST_SCHEDULED_TRANSACTION_NAME in scheduled_transaction.memo:
            test_scheduled_transaction_id = scheduled_transaction_id
    scheduled_transaction = test_ynab_py.api.get_scheduled_transaction(
        budget=budget,
        scheduled_transaction_id=test_scheduled_transaction_id,
    )
    return scheduled_transaction


def test_scheduled_transaction(scheduled_transaction):
    """
    Test the scheduled_transaction function.

    This test ensures that the scheduled_transaction object is not None,
    is not an instance of schemas.Error, and is an instance of schemas.ScheduledTransaction.

    Args:
        scheduled_transaction: The scheduled transaction object to be tested.

    Asserts:
        - scheduled_transaction is not None.
        - scheduled_transaction is not an instance of schemas.Error.
        - scheduled_transaction is an instance of schemas.ScheduledTransaction.
    """
    assert scheduled_transaction is not None
    assert not isinstance(scheduled_transaction, schemas.Error)
    assert isinstance(scheduled_transaction, schemas.ScheduledTransaction)


@pytest.fixture(scope="module")
def create_account(test_ynab_py, budget):
    """
    Creates a new account in the specified budget.

    Args:
        test_pynab (object): An instance of the test_ynab_py object which provides access to the API.
        budget (str): The budget ID where the account will be created.

    Returns:
        object: The created account object.
    """
    create_account = test_ynab_py.api.create_account(
        budget=budget,
        account_name=TEST_ACCOUNT_NAME,
        account_type=enums.AccountType.CHECKING,
        account_balance=0,
    )
    return create_account


def test_create_account(create_account):
    """
    Test the creation of an account.

    This test ensures that the account creation process returns a valid account object and not an error.

    Args:
        create_account: A fixture or function that attempts to create an account.

    Asserts:
        - The account creation result is not None.
        - The result is not an instance of schemas.Error.
        - The result is an instance of schemas.Account.
    """
    assert create_account is not None
    assert not isinstance(create_account, schemas.Error)
    assert isinstance(create_account, schemas.Account)


@pytest.fixture(scope="module")
def update_category(test_ynab_py, budget, category_group, category):
    """
    Update a category in the specified budget and category group.

    Args:
        test_pynab (object): The test instance of the ynab_py API.
        budget (str): The budget identifier.
        category_group (str): The category group identifier.
        category (str): The category identifier.

    Returns:
        object: The updated category object.
    """
    update_category = test_ynab_py.api.update_category(
        budget=budget,
        category_group=category_group,
        category=category,
        name=TEST_CATEGORY_GROUP_NAME,
        note=None,
    )
    return update_category


def test_update_category(update_category):
    """
    Test the update_category function.

    This test ensures that the update_category function returns a valid category object.
    It verifies that the returned object is not None, is not an instance of schemas.Error,
    and is an instance of schemas.Category.

    Args:
        update_category: The category object returned by the update_category function.

    Assertions:
        - update_category is not None.
        - update_category is not an instance of schemas.Error.
        - update_category is an instance of schemas.Category.
    """
    assert update_category is not None
    assert not isinstance(update_category, schemas.Error)
    assert isinstance(update_category, schemas.Category)


@pytest.fixture(scope="module")
def update_category_for_month(test_ynab_py, budget, category):
    """
    Update the category for the current month in the given budget.

    Args:
        test_pynab (object): An instance of the test_ynab_py object which provides access to the API.
        budget (str): The budget identifier where the category update will be applied.
        category (str): The category identifier that needs to be updated.

    Returns:
        dict: The response from the API after updating the category for the current month.
    """
    update_category_for_month = test_ynab_py.api.update_category_for_month(
        budget=budget,
        month_id="current",
        category=category,
    )
    return update_category_for_month


def test_update_category_for_month(update_category_for_month):
    """
    Test the update_category_for_month function.

    This test ensures that the update_category_for_month function:
    1. Does not return None.
    2. Does not return an instance of schemas.Error.
    3. Returns an instance of schemas.Category.

    Args:
        update_category_for_month: The function or result to be tested.
    """
    assert update_category_for_month is not None
    assert not isinstance(update_category_for_month, schemas.Error)
    assert isinstance(update_category_for_month, schemas.Category)


@pytest.fixture(scope="module")
def update_payee(test_ynab_py, budget, payee):
    """
    Update the name of a payee in the specified budget.

    Args:
        test_pynab (object): An instance of the test ynab_py API client.
        budget (str): The ID or name of the budget to update the payee in.
        payee (str): The ID or name of the payee to update.

    Returns:
        object: The response from the API after updating the payee.
    """
    update_payee = test_ynab_py.api.update_payee(
        budget=budget,
        payee=payee,
        name=TEST_PAYEE_CHANGED_NAME,
    )
    return update_payee


def test_update_payee(update_payee):
    """
    Test the update_payee function.

    This test ensures that the update_payee function returns a valid Payee object
    and does not return an Error object.

    Args:
        update_payee (schemas.Payee or schemas.Error): The result of the update_payee function.

    Asserts:
        - update_payee is not None.
        - update_payee is not an instance of schemas.Error.
        - update_payee is an instance of schemas.Payee.
    """
    assert update_payee is not None
    assert not isinstance(update_payee, schemas.Error)
    assert isinstance(update_payee, schemas.Payee)


@pytest.fixture(scope="module")
def create_transactions(test_ynab_py, budget, transaction):
    """
    Create multiple transactions in the specified budget using the test_ynab_py API.

    Args:
        test_ynab_py: An instance of the test_ynab_py API client.
        budget: The budget in which to create the transactions.
        transaction: A single transaction object to be duplicated and created.

    Returns:
        A list of created transaction objects.
    """
    transactions = [
        transaction,
        transaction,
        transaction,
    ]

    transactions = test_ynab_py.api.create_transactions(
        budget=budget, transactions=transactions
    )
    return transactions


def test_create_transactions(create_transactions):
    """
    Test the creation of transactions.

    This test verifies that the `create_transactions` function returns a valid
    transaction or a list of valid transactions. It ensures that the returned
    value is not None and is not an instance of `schemas.Error`. Depending on
    the type of the returned value, it checks if it is an instance of
    `schemas.Transaction` or if it is a list of `schemas.Transaction` instances.

    Args:
        create_transactions: The result of the `create_transactions` function,
                             which can be a single transaction or a list of
                             transactions.

    Asserts:
        - `create_transactions` is not None.
        - `create_transactions` is not an instance of `schemas.Error`.
        - If `create_transactions` is a single transaction, it is an instance
          of `schemas.Transaction`.
        - If `create_transactions` is a list, each item in the list is an
          instance of `schemas.Transaction`.
    """
    assert create_transactions is not None
    assert not isinstance(create_transactions, schemas.Error)

    if isinstance(create_transactions, schemas.Transaction):
        assert isinstance(create_transactions, schemas.Transaction)
    else:
        for transaction in create_transactions:
            assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def update_transactions(test_ynab_py, budget, create_transactions):
    """
    Update transactions in the given budget using the test_ynab_py API.

    This function iterates over the provided transactions and updates them
    in the specified budget using the test_ynab_py API. It identifies a specific
    transaction based on a predefined memo name and updates the transactions.

    Args:
        test_pynab (object): An instance of the test_ynab_py API client.
        budget (str): The budget ID or name where the transactions will be updated.
        create_transactions (dict): A dictionary of transactions to be updated,
                                    where keys are transaction IDs and values are
                                    transaction objects.

    Returns:
        list: A list of updated transactions.
    """
    for transaction_id, transaction in create_transactions.items():
        if TEST_TRANSACTION_NAME in transaction.memo:
            test_transaction_id = transaction_id

    transactions = test_ynab_py.api.update_transactions(
        budget=budget, transactions=transactions
    )
    return transactions


def test_update_transactions(update_transactions):
    """
    Test the update_transactions function.

    This test ensures that the update_transactions function returns a valid response.
    It checks the following:
    - The response is not None.
    - The response is not an instance of schemas.Error.
    - Each transaction in the response is an instance of schemas.Transaction.

    Args:
        update_transactions: The function or data to be tested.
    """
    assert update_transactions is not None
    assert not isinstance(update_transactions, schemas.Error)
    for transaction_id, transaction in transactions.items():
        assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def update_transactions(test_ynab_py, budget, create_transactions):
    """
    Update transactions in the given budget using the test_ynab_py API.

    This function iterates over the provided transactions and updates those
    that contain a specific memo. The updated transactions are then returned.

    Args:
        test_ynab_py: An instance of the test_ynab_py API client.
        budget: The budget object where the transactions will be updated.
        create_transactions: A list of transaction objects to be checked and updated.

    Returns:
        A list of updated transaction objects.
    """
    logging.debug(create_transactions)
    updated_transactions = []
    for transaction in create_transactions:
        if transaction.memo and TEST_TRANSACTION_NAME in transaction.memo:
            updated_transaction = test_ynab_py.api.update_transaction(
                budget=budget, transaction=transaction
            )
            updated_transactions.append(updated_transaction)
    return updated_transactions


def test_update_transactions(update_transactions):
    """
    Test the update_transactions function.

    This test ensures that the update_transactions function returns a non-None value,
    does not return an instance of schemas.Error, and that each item in the returned
    value is an instance of schemas.Transaction.

    Args:
        update_transactions: The result of the update_transactions function to be tested.

    Assertions:
        - update_transactions is not None.
        - update_transactions is not an instance of schemas.Error.
        - Each item in update_transactions is an instance of schemas.Transaction.
    """
    assert update_transactions is not None
    assert not isinstance(update_transactions, schemas.Error)
    for transaction in update_transactions:
        assert isinstance(transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def delete_transaction(test_ynab_py, budget, transactions):
    """
    Deletes a transaction from the given budget if it matches a specific memo.

    Args:
        test_ynab_py: An instance of the Pynab API client.
        budget: The budget from which the transaction should be deleted.
        transactions: A dictionary of transactions where the key is the transaction ID and the value is the transaction object.

    Returns:
        The deleted transaction object if a matching transaction is found and deleted, otherwise None.
    """
    logging.debug(transactions)
    test_transaction_id = None
    for transaction_id, transaction in transactions.items():
        if transaction.memo and TEST_TRANSACTION_NAME in transaction.memo:
            test_transaction_id = transaction_id
            break
    if test_transaction_id:
        transaction = test_ynab_py.api.delete_transaction(
            budget=budget,
            transaction=transactions[test_transaction_id],
        )
        return transaction
    else:
        return None


def test_delete_transaction(delete_transaction):
    """
    Test the deletion of a transaction.

    This test ensures that the `delete_transaction` function correctly deletes a transaction.
    It verifies that the returned value is not None, is not an instance of `schemas.Error`,
    and is an instance of `schemas.Transaction`.

    Args:
        delete_transaction: The transaction to be deleted.

    Asserts:
        - The transaction is not None.
        - The transaction is not an instance of `schemas.Error`.
        - The transaction is an instance of `schemas.Transaction`.
    """
    assert delete_transaction is not None
    assert not isinstance(delete_transaction, schemas.Error)
    assert isinstance(delete_transaction, schemas.Transaction)


@pytest.fixture(scope="module")
def create_scheduled_transaction(test_ynab_py, budget, scheduled_transaction):
    """
    Create a scheduled transaction using the provided test_pynab instance.

    Args:
        test_ynab_py: An instance of the test_pynab class, which provides access to the API.
        budget: The budget object within which the scheduled transaction will be created.
        scheduled_transaction: The scheduled transaction object to be created.

    Returns:
        The created scheduled transaction object.
    """
    scheduled_transaction = test_ynab_py.api.create_scheduled_transaction(
        budget=budget, scheduled_transaction=scheduled_transaction
    )
    return scheduled_transaction


def test_create_scheduled_transaction(scheduled_transaction):
    """
    Test the creation of a scheduled transaction.

    This test ensures that the scheduled transaction is created successfully
    and is of the correct type.

    Args:
        scheduled_transaction: The scheduled transaction object to be tested.

    Asserts:
        - The scheduled transaction is not None.
        - The scheduled transaction is not an instance of schemas.Error.
        - The scheduled transaction is an instance of schemas.ScheduledTransaction.
    """
    assert scheduled_transaction is not None
    assert not isinstance(scheduled_transaction, schemas.Error)
    assert isinstance(scheduled_transaction, schemas.ScheduledTransaction)
