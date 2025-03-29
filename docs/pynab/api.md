# Api



[Pynab Index](../README.md#pynab-index) / [Pynab](./index.md#pynab) / Api

> Auto-generated documentation for [pynab.api](../../pynab/api.py) module.

- [Api](#api)
  - [Api](#api-1)
    - [Api().create_account](#api()create_account)
    - [Api().create_scheduled_transaction](#api()create_scheduled_transaction)
    - [Api().create_transactions](#api()create_transactions)
    - [Api().delete_transaction](#api()delete_transaction)
    - [Api().get_account](#api()get_account)
    - [Api().get_account_transactions](#api()get_account_transactions)
    - [Api().get_accounts](#api()get_accounts)
    - [Api().get_budget](#api()get_budget)
    - [Api().get_budget_payee_locations](#api()get_budget_payee_locations)
    - [Api().get_budget_settings](#api()get_budget_settings)
    - [Api().get_budgets](#api()get_budgets)
    - [Api().get_categories](#api()get_categories)
    - [Api().get_category](#api()get_category)
    - [Api().get_category_for_month](#api()get_category_for_month)
    - [Api().get_category_transactions](#api()get_category_transactions)
    - [Api().get_month](#api()get_month)
    - [Api().get_month_transactions](#api()get_month_transactions)
    - [Api().get_months](#api()get_months)
    - [Api().get_payee](#api()get_payee)
    - [Api().get_payee_location](#api()get_payee_location)
    - [Api().get_payee_locations](#api()get_payee_locations)
    - [Api().get_payee_transactions](#api()get_payee_transactions)
    - [Api().get_payees](#api()get_payees)
    - [Api().get_scheduled_transaction](#api()get_scheduled_transaction)
    - [Api().get_scheduled_transactions](#api()get_scheduled_transactions)
    - [Api().get_transaction](#api()get_transaction)
    - [Api().get_transactions](#api()get_transactions)
    - [Api().get_user](#api()get_user)
    - [Api().import_transactions](#api()import_transactions)
    - [Api().update_category](#api()update_category)
    - [Api().update_category_for_month](#api()update_category_for_month)
    - [Api().update_payee](#api()update_payee)
    - [Api().update_transaction](#api()update_transaction)
    - [Api().update_transactions](#api()update_transactions)

## Api

[Show source in api.py:8](../../pynab/api.py#L8)

#### Signature

```python
class Api:
    def __init__(self, pynab=None): ...
```

### Api().create_account

[Show source in api.py:189](../../pynab/api.py#L189)

Creates a new account.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget to associate the account with. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget to associate the account with. Defaults to "last-used".
- `account_name` *str, optional* - The name of the account. Defaults to None.
- `account_type` *enums.AccountType, optional* - The type of the account. Defaults to None.
- `account_balance` *int, optional* - The initial balance of the account. Defaults to 0.

#### Returns

- `schemas.Account` - The created account.

#### Raises

- `Exception` - If there is an error creating the account.

#### Signature

```python
def create_account(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    account_name: str = None,
    account_type: enums.AccountType = None,
    account_balance: int = 0,
): ...
```

### Api().create_scheduled_transaction

[Show source in api.py:1475](../../pynab/api.py#L1475)

Creates a scheduled transaction.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The budget ID. Defaults to "last-used".
- `scheduled_transaction` *schemas.ScheduledTransaction, optional* - The scheduled transaction object. Defaults to None.

#### Returns

- `Union[schemas.ScheduledTransaction,` *schemas.Error]* - The created scheduled transaction object or an error object.

#### Signature

```python
def create_scheduled_transaction(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    scheduled_transaction: schemas.ScheduledTransaction = None,
): ...
```

### Api().create_transactions

[Show source in api.py:900](../../pynab/api.py#L900)

Create transactions in the specified budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transactions` *list, optional* - The list of transactions to create. Defaults to None.

#### Returns

Union[List[schemas.Transaction], Dict[str, Any]]: If a single transaction is created, returns the created transaction as a dictionary. If multiple transactions are created, returns a list of created transactions.

#### Raises

- `Exception` - If there is an error creating the transactions.

#### Signature

```python
def create_transactions(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    transactions: list = None,
): ...
```

### Api().delete_transaction

[Show source in api.py:1165](../../pynab/api.py#L1165)

Deletes a transaction from the specified budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transaction` *schemas.Transaction, optional* - The transaction object. Defaults to None.
- `transaction_id` *str, optional* - The ID of the transaction. Defaults to None.

#### Returns

- `schemas.Transaction` - The deleted transaction.

#### Raises

- `Exception` - If the deletion fails, an exception is raised with the error details.

#### Signature

```python
def delete_transaction(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    transaction: schemas.Transaction = None,
    transaction_id: str = None,
): ...
```

### Api().get_account

[Show source in api.py:240](../../pynab/api.py#L240)

Retrieves an account from the specified budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `account` *schemas.Account, optional* - The account object. Defaults to None.
- `account_id` *str, optional* - The ID of the account. Defaults to None.

#### Returns

- `schemas.Account` - The retrieved account.

#### Raises

- `Exception` - If there is an error retrieving the account.

#### Signature

```python
def get_account(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    account: schemas.Account = None,
    account_id: str = None,
): ...
```

### Api().get_account_transactions

[Show source in api.py:1204](../../pynab/api.py#L1204)

Retrieves account transactions from the API.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The budget ID. Defaults to "last-used".
- `account` *schemas.Account, optional* - The account object. Defaults to None.
- `account_id` *str, optional* - The account ID. Defaults to None.
- `since_date` *str, optional* - The date to retrieve transactions since. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.

#### Returns

- `dict` - A dictionary of transactions, where the transaction ID is the key and the transaction object is the value.

#### Raises

- `Exception` - If there is an error retrieving the transactions.

#### Signature

```python
def get_account_transactions(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    account: schemas.Account = None,
    account_id: str = None,
    since_date: str = None,
    type: str = None,
): ...
```

### Api().get_accounts

[Show source in api.py:147](../../pynab/api.py#L147)

Retrieves the accounts associated with the specified budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `dict` - A dictionary containing the retrieved accounts, where the keys are the account IDs and the values are the account objects.

#### Raises

- `Exception` - If the response status code is not 200, an exception is raised with the error details.

#### Signature

```python
def get_accounts(self, budget: schemas.Budget = None, budget_id: str = "last-used"): ...
```

### Api().get_budget

[Show source in api.py:82](../../pynab/api.py#L82)

Retrieves a budget from the server.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object to retrieve. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget to retrieve. Defaults to "last-used".

#### Returns

- `schemas.Budget` - The retrieved budget object.

#### Raises

- `Exception` - If there is an error retrieving the budget.

#### Signature

```python
def get_budget(self, budget: schemas.Budget = None, budget_id: str = "last-used"): ...
```

### Api().get_budget_payee_locations

[Show source in api.py:644](../../pynab/api.py#L644)

Retrieves the payee locations for a given budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `dict` - A dictionary containing the payee locations, where the keys are the payee location IDs and the values are the payee location objects.

#### Raises

- `Exception` - If there is an error retrieving the payee locations.

#### Signature

```python
def get_budget_payee_locations(
    self, budget: schemas.Budget = None, budget_id: str = "last-used"
): ...
```

### Api().get_budget_settings

[Show source in api.py:118](../../pynab/api.py#L118)

Retrieves the budget settings for a given budget or the last-used budget.

#### Arguments

- budget (schemas.Budget, optional): The budget object for which to retrieve the settings. If not provided, the last-used budget will be used.
- budget_id (str, optional): The ID of the budget for which to retrieve the settings. Defaults to "last-used" if not provided.

#### Returns

- `-` *schemas.BudgetSettings* - The budget settings object.

#### Raises

- `-` *Exception* - If the API request fails or returns an error.

#### Signature

```python
def get_budget_settings(
    self, budget: schemas.Budget = None, budget_id: str = "last-used"
): ...
```

### Api().get_budgets

[Show source in api.py:42](../../pynab/api.py#L42)

Retrieves budgets from the API.

#### Arguments

- `include_accounts` *bool, optional* - Whether to include accounts in the response. Defaults to False.

#### Returns

- `dict` - A dictionary containing the budgets retrieved from the API. The keys are the budget IDs and the values are instances of the `Budget` class.

#### Raises

- `Exception` - If an error occurs while retrieving the budgets.

#### Signature

```python
def get_budgets(self, include_accounts: bool = False): ...
```

### Api().get_categories

[Show source in api.py:277](../../pynab/api.py#L277)

Retrieves the categories for a given budget or the last-used budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `dict` - A dictionary containing the category groups, where the keys are the category group IDs and the values are the category group objects.

#### Raises

- `Exception` - If there is an error in the API response.

#### Signature

```python
def get_categories(
    self, budget: schemas.Budget = None, budget_id: str = "last-used"
): ...
```

### Api().get_category

[Show source in api.py:321](../../pynab/api.py#L321)

Retrieves a category from the API.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `category` *schemas.Category, optional* - The category object. Defaults to None.
- `category_id` *str, optional* - The ID of the category. Defaults to None.

#### Returns

- `schemas.Category` - The retrieved category.

#### Raises

- `Exception` - If the API request fails.

#### Signature

```python
def get_category(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    category: schemas.Category = None,
    category_id: str = None,
): ...
```

### Api().get_category_for_month

[Show source in api.py:421](../../pynab/api.py#L421)

Retrieves the category for a specific month in a budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month` *str, optional* - The month to retrieve the category for. Defaults to "current".
- `category` *schemas.Category, optional* - The category object. Defaults to None.
- `category_id` *str, optional* - The ID of the category. Defaults to None.

#### Returns

- `schemas.Category` - The category object for the specified month.

#### Raises

- `Exception` - If there is an error retrieving the category.

#### Signature

```python
def get_category_for_month(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    month: str = "current",
    category: schemas.Category = None,
    category_id: str = None,
): ...
```

### Api().get_category_transactions

[Show source in api.py:1261](../../pynab/api.py#L1261)

Retrieves transactions for a specific category.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The budget ID. Defaults to "last-used".
- `category` *schemas.Category, optional* - The category object. Defaults to None.
- `category_id` *str, optional* - The category ID. Defaults to None.
- `since_date` *str, optional* - The starting date for the transactions. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.

#### Returns

- `dict` - A dictionary of transactions, where the keys are the transaction IDs and the values are the transaction objects.

#### Raises

- `Exception` - If there is an error retrieving the transactions.

#### Signature

```python
def get_category_transactions(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    category: schemas.Category = None,
    category_id: str = None,
    since_date: str = None,
    type: str = None,
): ...
```

### Api().get_month

[Show source in api.py:810](../../pynab/api.py#L810)

Retrieves a specific month from the budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month` *schemas.Month, optional* - The month object. Defaults to None.
- `month_id` *str, optional* - The ID of the month. Defaults to "current".

#### Returns

- `schemas.Month` - The retrieved month object.

#### Raises

- `Exception` - If there is an error retrieving the month.

#### Signature

```python
def get_month(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    month: schemas.Month = None,
    month_id: str = "current",
): ...
```

### Api().get_month_transactions

[Show source in api.py:1373](../../pynab/api.py#L1373)

Retrieves the transactions for a specific month in a budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month` *schemas.Month, optional* - The month object. Defaults to None.
- `month_id` *str, optional* - The ID of the month. Defaults to "current".
- `since_date` *str, optional* - The starting date for the transactions. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.

#### Returns

- `dict` - A dictionary of transactions, where the keys are the transaction IDs and the values are the transaction objects.

#### Raises

- `Exception` - If there is an error retrieving the transactions.

#### Signature

```python
def get_month_transactions(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    month: schemas.Month = None,
    month_id: str = "current",
    since_date: str = None,
    type: str = None,
): ...
```

### Api().get_months

[Show source in api.py:766](../../pynab/api.py#L766)

Retrieves the months for a given budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `dict` - A dictionary containing the months as keys and their corresponding Month objects as values.

#### Raises

- `Exception` - If there is an error retrieving the months.

#### Signature

```python
def get_months(self, budget: schemas.Budget = None, budget_id: str = "last-used"): ...
```

### Api().get_payee

[Show source in api.py:558](../../pynab/api.py#L558)

Retrieves a payee from the specified budget or the last-used budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee` *schemas.Payee, optional* - The payee object. Defaults to None.
- `payee_id` *str, optional* - The ID of the payee. Defaults to None.

#### Returns

- `schemas.Payee` - The retrieved payee object.

#### Raises

- `Exception` - If the API response status code is not 200, an exception is raised with the error details.

#### Signature

```python
def get_payee(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    payee: schemas.Payee = None,
    payee_id: str = None,
): ...
```

### Api().get_payee_location

[Show source in api.py:679](../../pynab/api.py#L679)

Retrieves a payee location from the API.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The budget ID. Defaults to "last-used".
- `payee_location` *schemas.PayeeLocation, optional* - The payee location object. Defaults to None.
- `payee_location_id` *str, optional* - The payee location ID. Defaults to None.

#### Returns

- `schemas.PayeeLocation` - The retrieved payee location.

#### Raises

- `Exception` - If the API request fails.

#### Signature

```python
def get_payee_location(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    payee_location: schemas.PayeeLocation = None,
    payee_location_id: str = None,
): ...
```

### Api().get_payee_locations

[Show source in api.py:722](../../pynab/api.py#L722)

Retrieves the payee locations for a given budget and payee.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee` *schemas.Payee, optional* - The payee object. Defaults to None.
- `payee_id` *str, optional* - The ID of the payee. Defaults to None.

#### Returns

- `dict` - A dictionary of payee locations, where the keys are the payee location IDs and the values are the payee location objects.

#### Raises

- `Exception` - If the API response status code is not 200, an exception is raised with the error details.

#### Signature

```python
def get_payee_locations(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    payee: schemas.Payee = None,
    payee_id: str = None,
): ...
```

### Api().get_payee_transactions

[Show source in api.py:1317](../../pynab/api.py#L1317)

Retrieves transactions associated with a specific payee.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee` *schemas.Payee, optional* - The payee object. Defaults to None.
- `payee_id` *str, optional* - The ID of the payee. Defaults to None.
- `since_date` *str, optional* - The starting date for the transactions. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.

#### Returns

- `dict` - A dictionary of transactions, where the transaction ID is the key and the transaction object is the value.

#### Raises

- `Exception` - If there is an error retrieving the transactions.

#### Signature

```python
def get_payee_transactions(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    payee: schemas.Payee = None,
    payee_id: str = None,
    since_date: str = None,
    type: str = None,
): ...
```

### Api().get_payees

[Show source in api.py:521](../../pynab/api.py#L521)

Retrieves the payees associated with a budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `dict` - A dictionary containing the payees, where the key is the payee ID and the value is the payee object.

If the request is successful, the dictionary will contain the payees associated with the budget.
If the request fails, an error object will be returned.

#### Signature

```python
def get_payees(self, budget: schemas.Budget = None, budget_id: str = "last-used"): ...
```

### Api().get_scheduled_transaction

[Show source in api.py:1528](../../pynab/api.py#L1528)

Retrieves a scheduled transaction from the API.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The budget ID. Defaults to "last-used".
- `schedule_transaction` *schemas.ScheduledTransaction, optional* - The scheduled transaction object. Defaults to None.
- `scheduled_transaction_id` *str, optional* - The scheduled transaction ID. Defaults to None.

#### Returns

- `schemas.ScheduledTransaction` - The retrieved scheduled transaction.

#### Raises

- `Exception` - If the API request fails.

#### Signature

```python
def get_scheduled_transaction(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    schedule_transaction: schemas.ScheduledTransaction = None,
    scheduled_transaction_id: str = None,
): ...
```

### Api().get_scheduled_transactions

[Show source in api.py:1429](../../pynab/api.py#L1429)

Retrieves the scheduled transactions from the specified budget or the last-used budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object to retrieve scheduled transactions from. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget to retrieve scheduled transactions from. Defaults to "last-used".

#### Returns

- `dict` - A dictionary of scheduled transactions, where the keys are the transaction IDs and the values are the corresponding ScheduledTransaction objects.

#### Raises

- `Exception` - If there is an error retrieving the scheduled transactions.

#### Signature

```python
def get_scheduled_transactions(
    self, budget: schemas.Budget = None, budget_id: str = "last-used"
): ...
```

### Api().get_transaction

[Show source in api.py:1081](../../pynab/api.py#L1081)

Retrieves a transaction from the specified budget or the last-used budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transaction` *schemas.Transaction, optional* - The transaction object. Defaults to None.
- `transaction_id` *str, optional* - The ID of the transaction. Defaults to None.

#### Returns

- `schemas.Transaction` - The retrieved transaction.

#### Raises

- `Exception` - If there is an error retrieving the transaction.

#### Signature

```python
def get_transaction(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    transaction: schemas.Transaction = None,
    transaction_id: str = None,
): ...
```

### Api().get_transactions

[Show source in api.py:851](../../pynab/api.py#L851)

Retrieves transactions from the specified budget or the last-used budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object to retrieve transactions from. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget to retrieve transactions from. Defaults to "last-used".
- `since_date` *str, optional* - The date to retrieve transactions from. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.

#### Returns

- `dict` - A dictionary of transactions, where the keys are the transaction IDs and the values are the transaction objects.

#### Raises

- `Exception` - If there is an error retrieving the transactions.

#### Signature

```python
def get_transactions(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    since_date: str = None,
    type: str = None,
): ...
```

### Api().get_user

[Show source in api.py:22](../../pynab/api.py#L22)

Retrieves the user information from the API.

#### Returns

- `User` - An instance of the User class representing the user information.

#### Raises

- `Exception` - If the API response status code is not 200, an exception is raised with the error information.

#### Signature

```python
def get_user(self): ...
```

### Api().import_transactions

[Show source in api.py:1058](../../pynab/api.py#L1058)

Imports transactions into the budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `list` - A list of transaction IDs if the import is successful.
- `schemas.Error` - An error object if the import fails.

#### Signature

```python
def import_transactions(
    self, budget: schemas.Budget = None, budget_id: str = "last-used"
): ...
```

### Api().update_category

[Show source in api.py:362](../../pynab/api.py#L362)

Update a category in the budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `category_group` *schemas.CategoryGroup, optional* - The category group object. Defaults to None.
- `category_group_id` *str, optional* - The ID of the category group. Defaults to None.
- `category` *schemas.Category, optional* - The category object. Defaults to None.
- `category_id` *str, optional* - The ID of the category. Defaults to None.
- `name` *any, optional* - The name of the category. Defaults to None.
- `note` *str, optional* - The note for the category. Defaults to None.

#### Returns

- `schemas.Category` - The updated category object.

#### Raises

- `Exception` - If there is an error updating the category.

#### Signature

```python
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
): ...
```

### Api().update_category_for_month

[Show source in api.py:464](../../pynab/api.py#L464)

Update the budgeted amount for a category in a specific month.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month` *schemas.Month, optional* - The month object. Defaults to None.
- `month_id` *str, optional* - The ID of the month. Defaults to "current".
- `category` *schemas.Category, optional* - The category object. Defaults to None.
- `category_id` *str, optional* - The ID of the category. Defaults to None.
- `budgeted` *int, optional* - The new value for the amount assigned to this category

#### Returns

- `schemas.Category` - The updated category object.

#### Raises

- `Exception` - If the response status code is not 200, an exception is raised with the error details.

#### Signature

```python
def update_category_for_month(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    month: schemas.Month = None,
    month_id: str = "current",
    category: schemas.Category = None,
    category_id: str = None,
    budgeted: int = 0,
): ...
```

### Api().update_payee

[Show source in api.py:598](../../pynab/api.py#L598)

Update a payee with the given information.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee` *schemas.Payee, optional* - The payee object. Defaults to None.
- `payee_id` *str, optional* - The ID of the payee. Defaults to None.
- `name` *str, optional* - The new name for the payee. Defaults to None.

#### Returns

- `schemas.Payee` - The updated payee object.

#### Raises

- `Exception` - If the API request fails.

#### Signature

```python
def update_payee(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    payee: schemas.Payee = None,
    payee_id: str = None,
    name: str = None,
): ...
```

### Api().update_transaction

[Show source in api.py:1121](../../pynab/api.py#L1121)

Update a transaction in the budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transaction` *schemas.Transaction, optional* - The transaction object. Defaults to None.
- `transaction_id` *str, optional* - The ID of the transaction. Defaults to None.
- `request_body` *str, optional* - The request body. Defaults to None.

#### Returns

- `schemas.Transaction` - The updated transaction object.

#### Raises

- `Exception` - If there is an error updating the transaction.

#### Signature

```python
def update_transaction(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    transaction: schemas.Transaction = None,
    transaction_id: str = None,
    request_body: str = None,
): ...
```

### Api().update_transactions

[Show source in api.py:999](../../pynab/api.py#L999)

Update transactions in the budget.

#### Arguments

- `budget` *schemas.Budget, optional* - The budget object. Defaults to None.
- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transactions` *list, optional* - List of transactions to update. Defaults to None.

#### Returns

- `dict` - A dictionary containing the updated transaction information.

#### Raises

- `Exception` - If there is an error in the update process.

#### Signature

```python
def update_transactions(
    self,
    budget: schemas.Budget = None,
    budget_id: str = "last-used",
    transactions: list = None,
): ...
```