# Test Live Api



[Pynab Index](../README.md#pynab-index) / [Testing](./index.md#testing) / Test Live Api

> Auto-generated documentation for [testing.test_live_api](../../testing/test_live_api.py) module.

#### Attributes

- `secrets` - get API bearer token from .env: dotenv_values('testing/.env')


- [Test Live Api](#test-live-api)
  - [account](#account)
  - [account_transactions](#account_transactions)
  - [accounts](#accounts)
  - [budget](#budget)
  - [budget_settings](#budget_settings)
  - [budgets](#budgets)
  - [category](#category)
  - [category_for_month](#category_for_month)
  - [category_group](#category_group)
  - [category_groups](#category_groups)
  - [category_transactions](#category_transactions)
  - [create_account](#create_account)
  - [create_scheduled_transaction](#create_scheduled_transaction)
  - [create_transactions](#create_transactions)
  - [delete_transaction](#delete_transaction)
  - [get_payee_locations](#get_payee_locations)
  - [import_transactions](#import_transactions)
  - [month](#month)
  - [month_transactions](#month_transactions)
  - [months](#months)
  - [payee](#payee)
  - [payee_locations](#payee_locations)
  - [payee_transactions](#payee_transactions)
  - [payees](#payees)
  - [scheduled_transaction](#scheduled_transaction)
  - [scheduled_transactions](#scheduled_transactions)
  - [test_account](#test_account)
  - [test_account_transactions](#test_account_transactions)
  - [test_accounts](#test_accounts)
  - [test_budget](#test_budget)
  - [test_budget_settings](#test_budget_settings)
  - [test_budgets](#test_budgets)
  - [test_category](#test_category)
  - [test_category_for_month](#test_category_for_month)
  - [test_category_groups](#test_category_groups)
  - [test_category_transactions](#test_category_transactions)
  - [test_create_account](#test_create_account)
  - [test_create_scheduled_transaction](#test_create_scheduled_transaction)
  - [test_create_transactions](#test_create_transactions)
  - [test_delete_transaction](#test_delete_transaction)
  - [test_get_payee_locations](#test_get_payee_locations)
  - [test_import_transactions](#test_import_transactions)
  - [test_month](#test_month)
  - [test_month_transactions](#test_month_transactions)
  - [test_months](#test_months)
  - [test_payee](#test_payee)
  - [test_payee_location](#test_payee_location)
  - [test_payee_locations](#test_payee_locations)
  - [test_payee_transactions](#test_payee_transactions)
  - [test_payees](#test_payees)
  - [test_pynab](#test_pynab)
  - [test_pynab_init](#test_pynab_init)
  - [test_scheduled_transaction](#test_scheduled_transaction)
  - [test_scheduled_transactions](#test_scheduled_transactions)
  - [test_transaction](#test_transaction)
  - [test_transactions](#test_transactions)
  - [test_update_category](#test_update_category)
  - [test_update_category_for_month](#test_update_category_for_month)
  - [test_update_payee](#test_update_payee)
  - [test_update_transactions](#test_update_transactions)
  - [test_update_transactions](#test_update_transactions-1)
  - [test_user](#test_user)
  - [transaction](#transaction)
  - [transactions](#transactions)
  - [update_category](#update_category)
  - [update_category_for_month](#update_category_for_month)
  - [update_payee](#update_payee)
  - [update_transactions](#update_transactions)
  - [update_transactions](#update_transactions-1)
  - [user](#user)

## account

[Show source in test_live_api.py:236](../../testing/test_live_api.py#L236)

Retrieve a specific account from the provided accounts dictionary.

This function iterates through the given accounts and finds the account
whose name contains the predefined [TEST_ACCOUNT_NAME](#test-live-api). It then fetches
the account details using the [test_pynab](#test_pynab) API.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the pynab test API.
- [budget](#budget) *str* - The budget identifier.
- [accounts](#accounts) *dict* - A dictionary of account objects, where keys are account IDs
                 and values are account instances.

#### Returns

- `object` - The account object corresponding to the found account ID.

#### Signature

```python
@pytest.fixture(scope="module")
def account(test_pynab, budget, accounts): ...
```



## account_transactions

[Show source in test_live_api.py:784](../../testing/test_live_api.py#L784)

Retrieve transactions for a specific account within a budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) *str* - The ID or name of the budget to retrieve transactions from.
- [account](#account) *str* - The ID or name of the account to retrieve transactions for.

#### Returns

- `list` - A list of transactions for the specified account within the given budget.

#### Signature

```python
@pytest.fixture(scope="module")
def account_transactions(test_pynab, budget, account): ...
```



## accounts

[Show source in test_live_api.py:202](../../testing/test_live_api.py#L202)

Fetches the accounts for a given budget.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the test_pynab object which provides access to the API.
- [budget](#budget) - The budget identifier for which accounts are to be fetched.

#### Returns

A list of accounts associated with the specified budget.

#### Signature

```python
@pytest.fixture(scope="module")
def accounts(test_pynab, budget): ...
```



## budget

[Show source in test_live_api.py:126](../../testing/test_live_api.py#L126)

Retrieve a specific budget from the provided budgets.

This function iterates through the given budgets and identifies the budget
whose name contains the predefined [TEST_BUDGET_NAME](#test-live-api). It then fetches and
returns the budget details using the [test_pynab](#test_pynab) API.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the pynab test API.
- [budgets](#budgets) *dict* - A dictionary of budget objects, where keys are budget IDs
                and values are budget instances.

#### Returns

- `object` - The budget instance that matches the [TEST_BUDGET_NAME](#test-live-api).

#### Signature

```python
@pytest.fixture(scope="module")
def budget(test_pynab, budgets): ...
```



## budget_settings

[Show source in test_live_api.py:166](../../testing/test_live_api.py#L166)

Retrieve the budget settings for a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) *str* - The identifier of the budget for which settings are to be retrieved.

#### Returns

- `dict` - A dictionary containing the budget settings.

#### Signature

```python
@pytest.fixture(scope="module")
def budget_settings(test_pynab, budget): ...
```



## budgets

[Show source in test_live_api.py:92](../../testing/test_live_api.py#L92)

Fetches the budgets from the API.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the test client for pynab.

#### Returns

A list of budgets retrieved from the API with accounts excluded.

#### Signature

```python
@pytest.fixture(scope="module")
def budgets(test_pynab): ...
```



## category

[Show source in test_live_api.py:336](../../testing/test_live_api.py#L336)

Retrieve a specific category from a category group in a budget.

This function iterates through the categories in the provided category group,
identifies the category with a name matching the predefined [TEST_CATEGORY_NAME](#test-live-api),
and retrieves its details using the [test_pynab](#test_pynab) API.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab API client.
- [category_group](#category_group) *object* - The category group containing the categories.
- [budget](#budget) *object* - The budget object to which the category belongs.

#### Returns

- `object` - The category object retrieved from the API.

#### Signature

```python
@pytest.fixture(scope="module")
def category(test_pynab, category_group, budget): ...
```



## category_for_month

[Show source in test_live_api.py:380](../../testing/test_live_api.py#L380)

Retrieve the category details for the current month from the budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab object which provides access to the API.
- [budget](#budget) *str* - The budget identifier from which to retrieve the category details.
- [category](#category) *str* - The category identifier for which details are to be retrieved.

#### Returns

- `dict` - A dictionary containing the details of the specified category for the current month.

#### Signature

```python
@pytest.fixture(scope="module")
def category_for_month(test_pynab, budget, category): ...
```



## category_group

[Show source in test_live_api.py:317](../../testing/test_live_api.py#L317)

Retrieves a category group from the provided category groups dictionary that matches a specific name.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the test pynab object.
- [budget](#budget) - The budget object associated with the category groups.
- [category_groups](#category_groups) *dict* - A dictionary where the keys are category group IDs and the values are category group objects.

#### Returns

The category group object that matches the specified name, or None if no match is found.

#### Signature

```python
@pytest.fixture(scope="module")
def category_group(test_pynab, budget, category_groups): ...
```



## category_groups

[Show source in test_live_api.py:282](../../testing/test_live_api.py#L282)

Retrieve category groups for a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) *str* - The budget identifier for which to retrieve category groups.

#### Returns

- `list` - A list of category groups associated with the specified budget.

#### Signature

```python
@pytest.fixture(scope="module")
def category_groups(test_pynab, budget): ...
```



## category_transactions

[Show source in test_live_api.py:829](../../testing/test_live_api.py#L829)

Retrieve transactions for a specific category within a budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - The test instance of the pynab API.
- [budget](#budget) *str* - The budget identifier.
- [category](#category) *str* - The category identifier.

#### Returns

- `list` - A list of transactions for the specified category.

#### Signature

```python
@pytest.fixture(scope="module")
def category_transactions(test_pynab, budget, category): ...
```



## create_account

[Show source in test_live_api.py:1051](../../testing/test_live_api.py#L1051)

Creates a new account in the specified budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab object which provides access to the API.
- [budget](#budget) *str* - The budget ID where the account will be created.

#### Returns

- `object` - The created account object.

#### Signature

```python
@pytest.fixture(scope="module")
def create_account(test_pynab, budget): ...
```



## create_scheduled_transaction

[Show source in test_live_api.py:1420](../../testing/test_live_api.py#L1420)

Create a scheduled transaction using the provided test_pynab instance.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) - The budget object within which the scheduled transaction will be created.
- [scheduled_transaction](#scheduled_transaction) - The scheduled transaction object to be created.

#### Returns

The created scheduled transaction object.

#### Signature

```python
@pytest.fixture(scope="module")
def create_scheduled_transaction(test_pynab, budget, scheduled_transaction): ...
```



## create_transactions

[Show source in test_live_api.py:1215](../../testing/test_live_api.py#L1215)

Create multiple transactions in the specified budget using the test_pynab API.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the test_pynab API client.
- [budget](#budget) - The budget in which to create the transactions.
- [transaction](#transaction) - A single transaction object to be duplicated and created.

#### Returns

A list of created transaction objects.

#### Signature

```python
@pytest.fixture(scope="module")
def create_transactions(test_pynab, budget, transaction): ...
```



## delete_transaction

[Show source in test_live_api.py:1370](../../testing/test_live_api.py#L1370)

Deletes a transaction from the given budget if it matches a specific memo.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the Pynab API client.
- [budget](#budget) - The budget from which the transaction should be deleted.
- [transactions](#transactions) - A dictionary of transactions where the key is the transaction ID and the value is the transaction object.

#### Returns

The deleted transaction object if a matching transaction is found and deleted, otherwise None.

#### Signature

```python
@pytest.fixture(scope="module")
def delete_transaction(test_pynab, budget, transactions): ...
```



## get_payee_locations

[Show source in test_live_api.py:568](../../testing/test_live_api.py#L568)

Retrieve the locations associated with a specific payee within a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab object which provides access to the API.
- [budget](#budget) *str* - The budget identifier for which the payee locations are to be retrieved.
- [payee](#payee) *str* - The payee identifier for which the locations are to be retrieved.

#### Returns

- `list` - A list of payee locations associated with the specified budget and payee.

#### Signature

```python
@pytest.fixture(scope="module")
def get_payee_locations(test_pynab, budget, payee): ...
```



## import_transactions

[Show source in test_live_api.py:706](../../testing/test_live_api.py#L706)

Imports transactions for a given budget using the test_pynab API.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) *str* - The budget identifier for which transactions are to be imported.

#### Returns

- `list` - A list of imported transactions.

#### Signature

```python
@pytest.fixture(scope="module")
def import_transactions(test_pynab, budget): ...
```



## month

[Show source in test_live_api.py:638](../../testing/test_live_api.py#L638)

Retrieve the current month's budget data from the API.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the Pynab API client.
- [budget](#budget) *str* - The budget ID for which to retrieve the month data.

#### Returns

- `dict` - The current month's budget data as returned by the API.

#### Signature

```python
@pytest.fixture(scope="module")
def month(test_pynab, budget): ...
```



## month_transactions

[Show source in test_live_api.py:917](../../testing/test_live_api.py#L917)

Retrieve transactions for a specific month from the API.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test Pynab API client.
- [budget](#budget) *str* - The budget ID to retrieve transactions for.
- [month](#month) *str* - The month to retrieve transactions for in 'YYYY-MM' format.

#### Returns

- `list` - A list of transactions for the specified month.

#### Signature

```python
@pytest.fixture(scope="module")
def month_transactions(test_pynab, budget, month): ...
```



## months

[Show source in test_live_api.py:604](../../testing/test_live_api.py#L604)

Fetches the months data from the API for a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class which contains the API client.
- [budget](#budget) *str* - The budget identifier for which to fetch the months data.

#### Returns

- `list` - A list of months data retrieved from the API.

#### Signature

```python
@pytest.fixture(scope="module")
def months(test_pynab, budget): ...
```



## payee

[Show source in test_live_api.py:454](../../testing/test_live_api.py#L454)

Retrieves a specific payee from the provided payees dictionary and fetches its details using the test_pynab API.

#### Arguments

- [budget](#budget) *str* - The budget identifier.
- [test_pynab](#test_pynab) *object* - An instance of the test_pynab API client.
- [payees](#payees) *dict* - A dictionary of payee IDs to payee objects.

#### Returns

- `object` - The payee object retrieved from the test_pynab API.

#### Raises

- `AssertionError` - If any item in the payees dictionary is not an instance of schemas.Payee.

#### Signature

```python
@pytest.fixture(scope="module")
def payee(budget, test_pynab, payees): ...
```



## payee_locations

[Show source in test_live_api.py:498](../../testing/test_live_api.py#L498)

Retrieve payee locations for a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test pynab API client.
- [budget](#budget) *str* - The budget identifier.

#### Returns

- `list` - A list of payee locations associated with the specified budget.

#### Signature

```python
@pytest.fixture(scope="module")
def payee_locations(test_pynab, budget): ...
```



## payee_transactions

[Show source in test_live_api.py:874](../../testing/test_live_api.py#L874)

Retrieve transactions for a specific payee within a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab object which provides access to the API.
- [budget](#budget) *str* - The budget ID or name to retrieve transactions from.
- [payee](#payee) *str* - The payee ID or name to filter transactions by.

#### Returns

- `list` - A list of transactions associated with the specified payee within the given budget.

#### Signature

```python
@pytest.fixture(scope="module")
def payee_transactions(test_pynab, budget, payee): ...
```



## payees

[Show source in test_live_api.py:423](../../testing/test_live_api.py#L423)

Retrieve the list of payees for a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) *str* - The budget identifier for which to retrieve the payees.

#### Returns

- `list` - A list of payees associated with the specified budget.

#### Signature

```python
@pytest.fixture(scope="module")
def payees(test_pynab, budget): ...
```



## scheduled_transaction

[Show source in test_live_api.py:999](../../testing/test_live_api.py#L999)

Retrieve a specific scheduled transaction from a budget.

This function iterates through a dictionary of scheduled transactions,
identifies the one that matches a predefined name, and retrieves its details
using the provided API client.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the API client used to interact with the budget.
- [budget](#budget) *str* - The identifier of the budget from which to retrieve the scheduled transaction.
- [scheduled_transactions](#scheduled_transactions) *dict* - A dictionary of scheduled transactions where keys are transaction IDs
                               and values are `schemas.ScheduledTransaction` instances.

#### Returns

- `object` - The scheduled transaction object retrieved from the API.

#### Signature

```python
@pytest.fixture(scope="module")
def scheduled_transaction(test_pynab, budget, scheduled_transactions): ...
```



## scheduled_transactions

[Show source in test_live_api.py:957](../../testing/test_live_api.py#L957)

Retrieve scheduled transactions for a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) *str* - The budget identifier for which to retrieve scheduled transactions.

#### Returns

- `list` - A list of scheduled transactions for the specified budget.

#### Signature

```python
@pytest.fixture(scope="module")
def scheduled_transactions(test_pynab, budget): ...
```



## test_account

[Show source in test_live_api.py:264](../../testing/test_live_api.py#L264)

Test the account object.

This test ensures that the provided account object is valid and correctly
typed. It performs the following checks:
1. The account object is not None.
2. The account object is not an instance of the Error schema.
3. The account object is an instance of the Account schema.

#### Arguments

- [account](#account) - The account object to be tested.

#### Signature

```python
def test_account(account): ...
```



## test_account_transactions

[Show source in test_live_api.py:806](../../testing/test_live_api.py#L806)

Test the account_transactions function.

This test ensures that the account_transactions object is not None,
is not an instance of schemas.Error, and that each item in the
account_transactions dictionary is an instance of schemas.Transaction.

#### Arguments

- [account_transactions](#account_transactions) *dict* - A dictionary where keys are transaction IDs
and values are transaction objects.

Assertions:
    - account_transactions is not None.
    - account_transactions is not an instance of schemas.Error.
    - Each value in account_transactions is an instance of schemas.Transaction.

#### Signature

```python
def test_account_transactions(account_transactions): ...
```



## test_accounts

[Show source in test_live_api.py:218](../../testing/test_live_api.py#L218)

Test the accounts data structure.

#### Arguments

- [accounts](#accounts) *dict* - A dictionary of account data where keys are account IDs and values are account objects.

Assertions:
    - The accounts object is not None.
    - The accounts object is not an instance of schemas.Error.
    - Each item in the accounts dictionary is an instance of schemas.Account.

#### Signature

```python
def test_accounts(accounts): ...
```



## test_budget

[Show source in test_live_api.py:151](../../testing/test_live_api.py#L151)

Test the budget object.

This test ensures that the budget object is not None, is not an instance of
schemas.Error, and is an instance of schemas.Budget.

#### Arguments

- [budget](#budget) - The budget object to be tested.

#### Signature

```python
def test_budget(budget): ...
```



## test_budget_settings

[Show source in test_live_api.py:182](../../testing/test_live_api.py#L182)

Test the budget_settings function.

This test ensures that the budget_settings object is not None, is not an instance of schemas.Error,
and is an instance of schemas.BudgetSettings.

#### Arguments

- [budget_settings](#budget_settings) - The budget settings object to be tested.

Asserts:
    - budget_settings is not None.
    - budget_settings is not an instance of schemas.Error.
    - budget_settings is an instance of schemas.BudgetSettings.

#### Signature

```python
def test_budget_settings(budget_settings): ...
```



## test_budgets

[Show source in test_live_api.py:107](../../testing/test_live_api.py#L107)

Test the budgets data structure.

This test ensures that the [budgets](#budgets) object is not None and is not an instance of `schemas.Error`.
It also verifies that each item in the [budgets](#budgets) dictionary is an instance of `schemas.Budget`.

#### Arguments

- [budgets](#budgets) *dict* - A dictionary where keys are budget IDs and values are budget objects.

#### Raises

- `AssertionError` - If any of the assertions fail.

#### Signature

```python
def test_budgets(budgets): ...
```



## test_category

[Show source in test_live_api.py:363](../../testing/test_live_api.py#L363)

Test the validity of a category object.

#### Arguments

- [category](#category) *schemas.Category* - The category object to be tested.

Asserts:
    - The category is not None.
    - The category is not an instance of schemas.Error.
    - The category is an instance of schemas.Category.

#### Signature

```python
def test_category(category): ...
```



## test_category_for_month

[Show source in test_live_api.py:402](../../testing/test_live_api.py#L402)

Test the [category_for_month](#category_for_month) function.

This test ensures that the [category_for_month](#category_for_month) function returns a valid
category object for a given month. The test performs the following checks:
1. Asserts that the [category_for_month](#category_for_month) is not None.
2. Asserts that the [category_for_month](#category_for_month) is not an instance of `schemas.Error`.
3. Asserts that the [category_for_month](#category_for_month) is an instance of `schemas.Category`.

#### Arguments

- [category_for_month](#category_for_month) - The category object for a specific month to be tested.

#### Raises

- `AssertionError` - If any of the assertions fail.

#### Signature

```python
def test_category_for_month(category_for_month): ...
```



## test_category_groups

[Show source in test_live_api.py:298](../../testing/test_live_api.py#L298)

Test the category_groups function.

This test ensures that the category_groups object is not None and is not an instance of schemas.Error.
It also verifies that each item in the category_groups dictionary is an instance of schemas.CategoryGroup.

#### Arguments

- [category_groups](#category_groups) *dict* - A dictionary where keys are category group IDs and values are category group objects.

#### Raises

- `AssertionError` - If any of the assertions fail.

#### Signature

```python
def test_category_groups(category_groups): ...
```



## test_category_transactions

[Show source in test_live_api.py:851](../../testing/test_live_api.py#L851)

Test the category_transactions function.

This test ensures that the category_transactions object is not None,
is not an instance of schemas.Error, and that each item in the
category_transactions dictionary is an instance of schemas.Transaction.

#### Arguments

- [category_transactions](#category_transactions) *dict* - A dictionary where keys are transaction IDs
                              and values are transaction objects.

Asserts:
    - category_transactions is not None.
    - category_transactions is not an instance of schemas.Error.
    - Each value in category_transactions is an instance of schemas.Transaction.

#### Signature

```python
def test_category_transactions(category_transactions): ...
```



## test_create_account

[Show source in test_live_api.py:1072](../../testing/test_live_api.py#L1072)

Test the creation of an account.

This test ensures that the account creation process returns a valid account object and not an error.

#### Arguments

- [create_account](#create_account) - A fixture or function that attempts to create an account.

Asserts:
    - The account creation result is not None.
    - The result is not an instance of schemas.Error.
    - The result is an instance of schemas.Account.

#### Signature

```python
def test_create_account(create_account): ...
```



## test_create_scheduled_transaction

[Show source in test_live_api.py:1439](../../testing/test_live_api.py#L1439)

Test the creation of a scheduled transaction.

This test ensures that the scheduled transaction is created successfully
and is of the correct type.

#### Arguments

- [scheduled_transaction](#scheduled_transaction) - The scheduled transaction object to be tested.

Asserts:
    - The scheduled transaction is not None.
    - The scheduled transaction is not an instance of schemas.Error.
    - The scheduled transaction is an instance of schemas.ScheduledTransaction.

#### Signature

```python
def test_create_scheduled_transaction(scheduled_transaction): ...
```



## test_create_transactions

[Show source in test_live_api.py:1240](../../testing/test_live_api.py#L1240)

Test the creation of transactions.

This test verifies that the [create_transactions](#create_transactions) function returns a valid
transaction or a list of valid transactions. It ensures that the returned
value is not None and is not an instance of `schemas.Error`. Depending on
the type of the returned value, it checks if it is an instance of
`schemas.Transaction` or if it is a list of `schemas.Transaction` instances.

#### Arguments

- [create_transactions](#create_transactions) - The result of the [create_transactions](#create_transactions) function,
                     which can be a single transaction or a list of
                     transactions.

Asserts:
    - [create_transactions](#create_transactions) is not None.
    - [create_transactions](#create_transactions) is not an instance of `schemas.Error`.
    - If [create_transactions](#create_transactions) is a single transaction, it is an instance
      of `schemas.Transaction`.
    - If [create_transactions](#create_transactions) is a list, each item in the list is an
      instance of `schemas.Transaction`.

#### Signature

```python
def test_create_transactions(create_transactions): ...
```



## test_delete_transaction

[Show source in test_live_api.py:1399](../../testing/test_live_api.py#L1399)

Test the deletion of a transaction.

This test ensures that the [delete_transaction](#delete_transaction) function correctly deletes a transaction.
It verifies that the returned value is not None, is not an instance of `schemas.Error`,
and is an instance of `schemas.Transaction`.

#### Arguments

- [delete_transaction](#delete_transaction) - The transaction to be deleted.

Asserts:
    - The transaction is not None.
    - The transaction is not an instance of `schemas.Error`.
    - The transaction is an instance of `schemas.Transaction`.

#### Signature

```python
def test_delete_transaction(delete_transaction): ...
```



## test_get_payee_locations

[Show source in test_live_api.py:585](../../testing/test_live_api.py#L585)

Test the retrieval of payee locations.

This test checks the following:
1. The [get_payee_locations](#get_payee_locations) fixture is not None.
2. The [get_payee_locations](#get_payee_locations) fixture is not an instance of `schemas.Error`.
3. Each item in the [get_payee_locations](#get_payee_locations) dictionary is an instance of `schemas.PayeeLocation`.

#### Arguments

- [get_payee_locations](#get_payee_locations) *dict* - A dictionary of payee locations where the key is the payee location ID and the value is an instance of `schemas.PayeeLocation`.

#### Signature

```python
def test_get_payee_locations(get_payee_locations): ...
```



## test_import_transactions

[Show source in test_live_api.py:722](../../testing/test_live_api.py#L722)

Test the import_transactions function.

This test ensures that the import_transactions function returns a non-None value
and that the returned value is not an instance of schemas.Error.

#### Arguments

- [import_transactions](#import_transactions) - The result of the import_transactions function to be tested.

Assertions:
    - The import_transactions result is not None.
    - The import_transactions result is not an instance of schemas.Error.

#### Signature

```python
def test_import_transactions(import_transactions): ...
```



## test_month

[Show source in test_live_api.py:654](../../testing/test_live_api.py#L654)

Test the [month](#month) object.

#### Arguments

- [month](#month) *schemas.Month* - The month object to be tested.

Asserts:
    - The month object is not None.
    - The month object is not an instance of `schemas.Error`.
    - The month object is an instance of `schemas.Month`.

#### Signature

```python
def test_month(month): ...
```



## test_month_transactions

[Show source in test_live_api.py:939](../../testing/test_live_api.py#L939)

Test the validity of month transactions.

#### Arguments

- [month_transactions](#month_transactions) *dict* - A dictionary of transactions for the month.

Asserts:
    - The month_transactions is not None.
    - The month_transactions is not an instance of schemas.Error.
    - Each transaction in month_transactions is an instance of schemas.Transaction.

#### Signature

```python
def test_month_transactions(month_transactions): ...
```



## test_months

[Show source in test_live_api.py:620](../../testing/test_live_api.py#L620)

Test function to validate the 'months' data structure.

#### Arguments

- [months](#months) *dict* - A dictionary where keys are month IDs and values are instances of schemas.Month.

Asserts:
    - The 'months' parameter is not None.
    - The 'months' parameter is not an instance of schemas.Error.
    - Each value in the 'months' dictionary is an instance of schemas.Month.

#### Signature

```python
def test_months(months): ...
```



## test_payee

[Show source in test_live_api.py:478](../../testing/test_live_api.py#L478)

Test the payee object.

This test ensures that the payee object is not None, is not an instance of
schemas.Error, and is an instance of schemas.Payee.

#### Arguments

- [payee](#payee) - The payee object to be tested.

Assertions:
    - payee is not None.
    - payee is not an instance of schemas.Error.
    - payee is an instance of schemas.Payee.

#### Signature

```python
def test_payee(payee): ...
```



## test_payee_location

[Show source in test_live_api.py:532](../../testing/test_live_api.py#L532)

Test the retrieval of a specific payee location from the API.

This test function iterates through a dictionary of payee locations,
checks if each location is an instance of `schemas.PayeeLocation`,
and identifies a payee location by name. If a matching payee location
is found, it retrieves the payee location from the API and performs
several assertions to ensure the retrieved data is valid.

#### Arguments

- [test_pynab](#test_pynab) - The test fixture providing access to the pynab API.
- [budget](#budget) - The budget object to be used in the API call.
- [payee_locations](#payee_locations) - A dictionary of payee locations to search through.

Assertions:
    - Each payee location in the dictionary is an instance of `schemas.PayeeLocation`.
    - The retrieved payee location is not None.
    - The retrieved payee location is not an instance of `schemas.Error`.
    - The retrieved payee location is an instance of `schemas.PayeeLocation`.

#### Signature

```python
def test_payee_location(test_pynab, budget, payee_locations): ...
```



## test_payee_locations

[Show source in test_live_api.py:516](../../testing/test_live_api.py#L516)

Test the payee_locations function.

#### Arguments

- [payee_locations](#payee_locations) *object* - The payee locations object to be tested.

Asserts:
    - payee_locations is not None.
    - payee_locations is not an instance of schemas.Error.

#### Signature

```python
def test_payee_locations(payee_locations): ...
```



## test_payee_transactions

[Show source in test_live_api.py:896](../../testing/test_live_api.py#L896)

Test the payee_transactions function.

This test ensures that the payee_transactions object is not None,
is not an instance of schemas.Error, and that each item in the
payee_transactions dictionary is an instance of schemas.Transaction.

#### Arguments

- [payee_transactions](#payee_transactions) *dict* - A dictionary where keys are transaction IDs
                           and values are transaction objects.

#### Raises

- `AssertionError` - If any of the assertions fail.

#### Signature

```python
def test_payee_transactions(payee_transactions): ...
```



## test_payees

[Show source in test_live_api.py:439](../../testing/test_live_api.py#L439)

Test the payees function.

#### Arguments

- [payees](#payees) - The payees object to be tested.

Asserts:
    - payees is not None.
    - payees is not an instance of schemas.Error.

#### Signature

```python
def test_payees(payees): ...
```



## test_pynab

[Show source in test_live_api.py:25](../../testing/test_live_api.py#L25)

Test the initialization of the Pynab class with a bearer token.

This function creates an instance of the Pynab class using a provided
bearer token and returns the instance.

#### Returns

- `Pynab` - An instance of the Pynab class initialized with the bearer token.

#### Signature

```python
@pytest.fixture(scope="module")
def test_pynab(): ...
```



## test_pynab_init

[Show source in test_live_api.py:40](../../testing/test_live_api.py#L40)

Test the initialization of the Pynab instance.

#### Arguments

- [test_pynab](#test_pynab) - The Pynab instance to be tested.

Asserts:
    - The test_pynab instance is not None.
    - The test_pynab instance is not an instance of schemas.Error.
    - The test_pynab instance is an instance of Pynab.

#### Signature

```python
def test_pynab_init(test_pynab): ...
```



## test_scheduled_transaction

[Show source in test_live_api.py:1031](../../testing/test_live_api.py#L1031)

Test the scheduled_transaction function.

This test ensures that the scheduled_transaction object is not None,
is not an instance of schemas.Error, and is an instance of schemas.ScheduledTransaction.

#### Arguments

- [scheduled_transaction](#scheduled_transaction) - The scheduled transaction object to be tested.

Asserts:
    - scheduled_transaction is not None.
    - scheduled_transaction is not an instance of schemas.Error.
    - scheduled_transaction is an instance of schemas.ScheduledTransaction.

#### Signature

```python
def test_scheduled_transaction(scheduled_transaction): ...
```



## test_scheduled_transactions

[Show source in test_live_api.py:975](../../testing/test_live_api.py#L975)

Test the scheduled transactions.

This test verifies that the [scheduled_transactions](#scheduled_transactions) object is not None and is not an instance of `schemas.Error`.
It also checks that each item in the [scheduled_transactions](#scheduled_transactions) dictionary is an instance of `schemas.ScheduledTransaction`.

#### Arguments

- [scheduled_transactions](#scheduled_transactions) *dict* - A dictionary of scheduled transactions where the key is the transaction ID and the value is the `ScheduledTransaction` object.

Assertions:
    - [scheduled_transactions](#scheduled_transactions) is not None.
    - [scheduled_transactions](#scheduled_transactions) is not an instance of `schemas.Error`.
    - Each value in [scheduled_transactions](#scheduled_transactions) is an instance of `schemas.ScheduledTransaction`.

#### Signature

```python
def test_scheduled_transactions(scheduled_transactions): ...
```



## test_transaction

[Show source in test_live_api.py:769](../../testing/test_live_api.py#L769)

Test the transaction object.

This test ensures that the transaction object is not None, is not an instance of schemas.Error,
and is an instance of schemas.Transaction.

#### Arguments

- [transaction](#transaction) - The transaction object to be tested.

#### Signature

```python
def test_transaction(transaction): ...
```



## test_transactions

[Show source in test_live_api.py:691](../../testing/test_live_api.py#L691)

Test the transactions function.

#### Arguments

- [transactions](#transactions) - The transactions data to be tested.

Asserts:
    - transactions is not None.
    - transactions is not an instance of schemas.Error.

#### Signature

```python
def test_transactions(transactions): ...
```



## test_update_category

[Show source in test_live_api.py:1115](../../testing/test_live_api.py#L1115)

Test the update_category function.

This test ensures that the update_category function returns a valid category object.
It verifies that the returned object is not None, is not an instance of schemas.Error,
and is an instance of schemas.Category.

#### Arguments

- [update_category](#update_category) - The category object returned by the update_category function.

Assertions:
    - update_category is not None.
    - update_category is not an instance of schemas.Error.
    - update_category is an instance of schemas.Category.

#### Signature

```python
def test_update_category(update_category): ...
```



## test_update_category_for_month

[Show source in test_live_api.py:1157](../../testing/test_live_api.py#L1157)

Test the update_category_for_month function.

This test ensures that the update_category_for_month function:
1. Does not return None.
2. Does not return an instance of schemas.Error.
3. Returns an instance of schemas.Category.

#### Arguments

- [update_category_for_month](#update_category_for_month) - The function or result to be tested.

#### Signature

```python
def test_update_category_for_month(update_category_for_month): ...
```



## test_update_payee

[Show source in test_live_api.py:1195](../../testing/test_live_api.py#L1195)

Test the update_payee function.

This test ensures that the update_payee function returns a valid Payee object
and does not return an Error object.

#### Arguments

update_payee (schemas.Payee or schemas.Error): The result of the update_payee function.

Asserts:
    - update_payee is not None.
    - update_payee is not an instance of schemas.Error.
    - update_payee is an instance of schemas.Payee.

#### Signature

```python
def test_update_payee(update_payee): ...
```



## test_update_transactions

[Show source in test_live_api.py:1302](../../testing/test_live_api.py#L1302)

Test the update_transactions function.

This test ensures that the update_transactions function returns a valid response.
It checks the following:
- The response is not None.
- The response is not an instance of schemas.Error.
- Each transaction in the response is an instance of schemas.Transaction.

#### Arguments

- [update_transactions](#update_transactions) - The function or data to be tested.

#### Signature

```python
def test_update_transactions(update_transactions): ...
```



## test_update_transactions

[Show source in test_live_api.py:1348](../../testing/test_live_api.py#L1348)

Test the update_transactions function.

This test ensures that the update_transactions function returns a non-None value,
does not return an instance of schemas.Error, and that each item in the returned
value is an instance of schemas.Transaction.

#### Arguments

- [update_transactions](#update_transactions) - The result of the update_transactions function to be tested.

Assertions:
    - update_transactions is not None.
    - update_transactions is not an instance of schemas.Error.
    - Each item in update_transactions is an instance of schemas.Transaction.

#### Signature

```python
def test_update_transactions(update_transactions): ...
```



## test_user

[Show source in test_live_api.py:72](../../testing/test_live_api.py#L72)

Test the user object.

This test ensures that the user object is not None, is not an instance of the
schemas.Error class, and is an instance of the schemas.User class.

#### Arguments

- [user](#user) - The user object to be tested.

Assertions:
    - The user object is not None.
    - The user object is not an instance of schemas.Error.
    - The user object is an instance of schemas.User.

#### Signature

```python
def test_user(user): ...
```



## transaction

[Show source in test_live_api.py:740](../../testing/test_live_api.py#L740)

Retrieve a specific transaction from a budget.

This function iterates over a dictionary of transactions, checks if each
transaction is an instance of `schemas.Transaction`, and identifies the
transaction with a memo matching [TEST_TRANSACTION_NAME](#test-live-api). It then retrieves
this transaction using the [test_pynab](#test_pynab) API.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the pynab test client.
- [budget](#budget) - The budget from which to retrieve the transaction.
- [transactions](#transactions) - A dictionary of transactions where the key is the
              transaction ID and the value is the transaction object.

#### Returns

The transaction object that matches the specified memo.

#### Signature

```python
@pytest.fixture(scope="module")
def transaction(test_pynab, budget, transactions): ...
```



## transactions

[Show source in test_live_api.py:671](../../testing/test_live_api.py#L671)

Retrieve transactions from the API for a given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab class, which provides access to the API.
- [budget](#budget) *str* - The budget identifier for which transactions are to be retrieved.

#### Returns

- `list` - A list of transactions retrieved from the API.

#### Signature

```python
@pytest.fixture(scope="module")
def transactions(test_pynab, budget): ...
```



## update_category

[Show source in test_live_api.py:1091](../../testing/test_live_api.py#L1091)

Update a category in the specified budget and category group.

#### Arguments

- [test_pynab](#test_pynab) *object* - The test instance of the pynab API.
- [budget](#budget) *str* - The budget identifier.
- [category_group](#category_group) *str* - The category group identifier.
- [category](#category) *str* - The category identifier.

#### Returns

- `object` - The updated category object.

#### Signature

```python
@pytest.fixture(scope="module")
def update_category(test_pynab, budget, category_group, category): ...
```



## update_category_for_month

[Show source in test_live_api.py:1136](../../testing/test_live_api.py#L1136)

Update the category for the current month in the given budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab object which provides access to the API.
- [budget](#budget) *str* - The budget identifier where the category update will be applied.
- [category](#category) *str* - The category identifier that needs to be updated.

#### Returns

- `dict` - The response from the API after updating the category for the current month.

#### Signature

```python
@pytest.fixture(scope="module")
def update_category_for_month(test_pynab, budget, category): ...
```



## update_payee

[Show source in test_live_api.py:1174](../../testing/test_live_api.py#L1174)

Update the name of a payee in the specified budget.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test pynab API client.
- [budget](#budget) *str* - The ID or name of the budget to update the payee in.
- [payee](#payee) *str* - The ID or name of the payee to update.

#### Returns

- `object` - The response from the API after updating the payee.

#### Signature

```python
@pytest.fixture(scope="module")
def update_payee(test_pynab, budget, payee): ...
```



## update_transactions

[Show source in test_live_api.py:1273](../../testing/test_live_api.py#L1273)

Update transactions in the given budget using the test_pynab API.

This function iterates over the provided transactions and updates them
in the specified budget using the test_pynab API. It identifies a specific
transaction based on a predefined memo name and updates the transactions.

#### Arguments

- [test_pynab](#test_pynab) *object* - An instance of the test_pynab API client.
- [budget](#budget) *str* - The budget ID or name where the transactions will be updated.
- [create_transactions](#create_transactions) *dict* - A dictionary of transactions to be updated,
                            where keys are transaction IDs and values are
                            transaction objects.

#### Returns

- `list` - A list of updated transactions.

#### Signature

```python
@pytest.fixture(scope="module")
def update_transactions(test_pynab, budget, create_transactions): ...
```



## update_transactions

[Show source in test_live_api.py:1321](../../testing/test_live_api.py#L1321)

Update transactions in the given budget using the test_pynab API.

This function iterates over the provided transactions and updates those
that contain a specific memo. The updated transactions are then returned.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the test_pynab API client.
- [budget](#budget) - The budget object where the transactions will be updated.
- [create_transactions](#create_transactions) - A list of transaction objects to be checked and updated.

#### Returns

A list of updated transaction objects.

#### Signature

```python
@pytest.fixture(scope="module")
def update_transactions(test_pynab, budget, create_transactions): ...
```



## user

[Show source in test_live_api.py:57](../../testing/test_live_api.py#L57)

Fetches the user information from the API.

#### Arguments

- [test_pynab](#test_pynab) - An instance of the test_pynab object which contains the API client.

#### Returns

- `dict` - A dictionary containing user information retrieved from the API.

#### Signature

```python
@pytest.fixture(scope="module")
def user(test_pynab): ...
```