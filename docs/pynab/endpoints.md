# Endpoints



[Pynab Index](../README.md#pynab-index) / [Pynab](./index.md#pynab) / Endpoints

> Auto-generated documentation for [pynab.endpoints](../../pynab/endpoints.py) module.

- [Endpoints](#endpoints)
  - [Endpoints](#endpoints-1)
    - [Endpoints().request_create_account](#endpoints()request_create_account)
    - [Endpoints().request_create_scheduled_transaction](#endpoints()request_create_scheduled_transaction)
    - [Endpoints().request_create_transactions](#endpoints()request_create_transactions)
    - [Endpoints().request_delete_transaction](#endpoints()request_delete_transaction)
    - [Endpoints().request_get_account](#endpoints()request_get_account)
    - [Endpoints().request_get_account_transactions](#endpoints()request_get_account_transactions)
    - [Endpoints().request_get_accounts](#endpoints()request_get_accounts)
    - [Endpoints().request_get_all_payee_locations](#endpoints()request_get_all_payee_locations)
    - [Endpoints().request_get_budget](#endpoints()request_get_budget)
    - [Endpoints().request_get_budget_settings](#endpoints()request_get_budget_settings)
    - [Endpoints().request_get_budgets](#endpoints()request_get_budgets)
    - [Endpoints().request_get_categories](#endpoints()request_get_categories)
    - [Endpoints().request_get_category](#endpoints()request_get_category)
    - [Endpoints().request_get_category_for_month](#endpoints()request_get_category_for_month)
    - [Endpoints().request_get_category_transactions](#endpoints()request_get_category_transactions)
    - [Endpoints().request_get_month](#endpoints()request_get_month)
    - [Endpoints().request_get_month_transactions](#endpoints()request_get_month_transactions)
    - [Endpoints().request_get_months](#endpoints()request_get_months)
    - [Endpoints().request_get_payee](#endpoints()request_get_payee)
    - [Endpoints().request_get_payee_location](#endpoints()request_get_payee_location)
    - [Endpoints().request_get_payee_locations](#endpoints()request_get_payee_locations)
    - [Endpoints().request_get_payee_transactions](#endpoints()request_get_payee_transactions)
    - [Endpoints().request_get_payees](#endpoints()request_get_payees)
    - [Endpoints().request_get_scheduled_transaction](#endpoints()request_get_scheduled_transaction)
    - [Endpoints().request_get_scheduled_transactions](#endpoints()request_get_scheduled_transactions)
    - [Endpoints().request_get_transaction](#endpoints()request_get_transaction)
    - [Endpoints().request_get_transactions](#endpoints()request_get_transactions)
    - [Endpoints().request_get_user](#endpoints()request_get_user)
    - [Endpoints().request_import_transactions](#endpoints()request_import_transactions)
    - [Endpoints().request_update_category](#endpoints()request_update_category)
    - [Endpoints().request_update_category_for_month](#endpoints()request_update_category_for_month)
    - [Endpoints().request_update_payee](#endpoints()request_update_payee)
    - [Endpoints().request_update_transaction](#endpoints()request_update_transaction)
    - [Endpoints().request_update_transactions](#endpoints()request_update_transactions)

## Endpoints

[Show source in endpoints.py:5](../../pynab/endpoints.py#L5)

#### Signature

```python
class Endpoints:
    def __init__(self, pynab: pynab = None): ...
```

#### See also

- [Pynab](./pynab.md#pynab)

### Endpoints().request_create_account

[Show source in endpoints.py:109](../../pynab/endpoints.py#L109)

Creates a new account in the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget to create the account in. Defaults to "last-used".
- `request_body` *str, optional* - The JSON request body containing the account details. Defaults to None.

#### Returns

The response from the API call.

#### Signature

```python
def request_create_account(
    self, budget_id: str = "last-used", request_body: str = None
): ...
```

### Endpoints().request_create_scheduled_transaction

[Show source in endpoints.py:681](../../pynab/endpoints.py#L681)

Creates a new scheduled transaction for the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `request_body` *str, optional* - The request body containing the details of the scheduled transaction. Defaults to None.

#### Returns

The response from the API call.

#### Signature

```python
def request_create_scheduled_transaction(
    self, budget_id: str = "last-used", request_body: str = None
): ...
```

### Endpoints().request_create_transactions

[Show source in endpoints.py:431](../../pynab/endpoints.py#L431)

Sends a request to create transactions for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `request_body` *str, optional* - The JSON request body containing the transaction data. Defaults to None.

#### Returns

The response from the API call.

#### Signature

```python
def request_create_transactions(
    self, budget_id: str = "last-used", request_body: str = None
): ...
```

### Endpoints().request_delete_transaction

[Show source in endpoints.py:520](../../pynab/endpoints.py#L520)

Sends a request to delete a transaction.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transaction_id` *str, optional* - The ID of the transaction to be deleted.

#### Returns

The response from the HTTP request.

#### Signature

```python
def request_delete_transaction(
    self, budget_id: str = "last-used", transaction_id: str = None
): ...
```

### Endpoints().request_get_account

[Show source in endpoints.py:126](../../pynab/endpoints.py#L126)

Retrieves information about a specific account in a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `account_id` *str, optional* - The ID of the account. If not provided, information about all accounts will be returned.

#### Returns

- `dict` - A dictionary containing the account information.

#### Raises

- `HTTPException` - If the request fails or the account is not found.

#### Signature

```python
def request_get_account(self, budget_id: str = "last-used", account_id: str = None): ...
```

### Endpoints().request_get_account_transactions

[Show source in endpoints.py:537](../../pynab/endpoints.py#L537)

Retrieves the account transactions for a specific budget and account.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `account_id` *str, optional* - The ID of the account. Defaults to None.
- `since_date` *str, optional* - The date to retrieve transactions from. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The account transactions.

#### Signature

```python
def request_get_account_transactions(
    self,
    budget_id: str = "last-used",
    account_id: str = None,
    since_date: str = None,
    type: str = None,
    last_knowledge_of_server: int = 0,
): ...
```

### Endpoints().request_get_accounts

[Show source in endpoints.py:90](../../pynab/endpoints.py#L90)

Retrieves the accounts associated with a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The response from the HTTP GET request.

#### Signature

```python
def request_get_accounts(
    self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
): ...
```

### Endpoints().request_get_all_payee_locations

[Show source in endpoints.py:309](../../pynab/endpoints.py#L309)

Retrieves all payee locations for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `dict` - A dictionary containing the response data.

#### Raises

None

#### Signature

```python
def request_get_all_payee_locations(self, budget_id: str = "last-used"): ...
```

### Endpoints().request_get_budget

[Show source in endpoints.py:51](../../pynab/endpoints.py#L51)

Retrieves the budget information from the server.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget to retrieve. Defaults to "last-used".
- `last_knowledge_of_server` *int, optional* - The knowledge of the server to determine if the budget has been updated. Defaults to 0.

#### Returns

- `dict` - The budget information.

#### Raises

- `HTTPException` - If an error occurs during the HTTP request.

#### Signature

```python
def request_get_budget(
    self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
): ...
```

### Endpoints().request_get_budget_settings

[Show source in endpoints.py:73](../../pynab/endpoints.py#L73)

Retrieves the budget settings for the specified budget ID.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".

#### Returns

- `dict` - The budget settings.

#### Raises

- `HTTPError` - If an HTTP error occurs.

#### Signature

```python
def request_get_budget_settings(self, budget_id: str = "last-used"): ...
```

### Endpoints().request_get_budgets

[Show source in endpoints.py:32](../../pynab/endpoints.py#L32)

Sends a GET request to retrieve budgets.

#### Arguments

- `include_accounts` *bool, optional* - Whether to include accounts in the response. Defaults to False.

#### Returns

- `dict` - The response from the API.

#### Raises

None

#### Signature

```python
def request_get_budgets(self, include_accounts: bool = False): ...
```

### Endpoints().request_get_categories

[Show source in endpoints.py:144](../../pynab/endpoints.py#L144)

Retrieves the categories for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The response from the HTTP GET request.

#### Signature

```python
def request_get_categories(
    self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
): ...
```

### Endpoints().request_get_category

[Show source in endpoints.py:163](../../pynab/endpoints.py#L163)

Retrieves a specific category from a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `category_id` *str, optional* - The ID of the category. If not provided, retrieves all categories.

#### Returns

- `dict` - The category information.

#### Raises

- `HTTPError` - If the request fails.

#### Signature

```python
def request_get_category(
    self, budget_id: str = "last-used", category_id: str = None
): ...
```

### Endpoints().request_get_category_for_month

[Show source in endpoints.py:207](../../pynab/endpoints.py#L207)

Retrieves the category for a specific month in a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month` *str, optional* - The month to retrieve the category for. Defaults to "current".
- `category_id` *str, optional* - The ID of the category. Defaults to None.

#### Returns

The response from the API call.

#### Signature

```python
def request_get_category_for_month(
    self, budget_id: str = "last-used", month: str = "current", category_id: str = None
): ...
```

### Endpoints().request_get_category_transactions

[Show source in endpoints.py:569](../../pynab/endpoints.py#L569)

Retrieves transactions for a specific category.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `category_id` *str, optional* - The ID of the category. Defaults to None.
- `since_date` *str, optional* - The starting date to retrieve transactions from. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.
- `last_knowledge_of_server` *int, optional* - The knowledge of the server to retrieve transactions from. Defaults to 0.

#### Returns

- `dict` - The response containing the retrieved transactions.

#### Signature

```python
def request_get_category_transactions(
    self,
    budget_id: str = "last-used",
    category_id: str = None,
    since_date: str = None,
    type: str = None,
    last_knowledge_of_server: int = 0,
): ...
```

### Endpoints().request_get_month

[Show source in endpoints.py:382](../../pynab/endpoints.py#L382)

Retrieves the details of a specific month in a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month_id` *str, optional* - The ID of the month. Defaults to "current".

#### Returns

- `dict` - The details of the requested month.

#### Raises

- `HTTPError` - If the request fails.

#### Signature

```python
def request_get_month(self, budget_id: str = "last-used", month_id: str = "current"): ...
```

### Endpoints().request_get_month_transactions

[Show source in endpoints.py:631](../../pynab/endpoints.py#L631)

Retrieves the transactions for a specific month in a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month` *str, optional* - The month to retrieve transactions for. Defaults to "current".
- `since_date` *str, optional* - The starting date for the transactions. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The response from the API containing the transactions for the specified month.

#### Signature

```python
def request_get_month_transactions(
    self,
    budget_id: str = "last-used",
    month: str = "current",
    since_date: str = None,
    type: str = None,
    last_knowledge_of_server: int = 0,
): ...
```

### Endpoints().request_get_months

[Show source in endpoints.py:363](../../pynab/endpoints.py#L363)

Retrieves the months for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The response from the server.

#### Signature

```python
def request_get_months(
    self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
): ...
```

### Endpoints().request_get_payee

[Show source in endpoints.py:270](../../pynab/endpoints.py#L270)

Retrieves a specific payee from the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee_id` *str, optional* - The ID of the payee. If not provided, all payees will be returned.

#### Returns

- `dict` - The payee information.

#### Raises

- `HTTPError` - If the request fails.

#### Signature

```python
def request_get_payee(self, budget_id: str = "last-used", payee_id: str = None): ...
```

### Endpoints().request_get_payee_location

[Show source in endpoints.py:326](../../pynab/endpoints.py#L326)

Retrieves a specific payee location from the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee_location_id` *str, optional* - The ID of the payee location. Defaults to None.

#### Returns

- `dict` - The payee location information.

#### Raises

- `HTTPError` - If the request fails.

#### Signature

```python
def request_get_payee_location(
    self, budget_id: str = "last-used", payee_location_id: str = None
): ...
```

### Endpoints().request_get_payee_locations

[Show source in endpoints.py:346](../../pynab/endpoints.py#L346)

Retrieves the payee locations for a specific payee in a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee_id` *str, optional* - The ID of the payee. Defaults to None.

#### Returns

- `dict` - The payee locations for the specified payee in the budget.

#### Signature

```python
def request_get_payee_locations(
    self, budget_id: str = "last-used", payee_id: str = None
): ...
```

### Endpoints().request_get_payee_transactions

[Show source in endpoints.py:600](../../pynab/endpoints.py#L600)

Retrieves transactions for a specific payee.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee_id` *str, optional* - The ID of the payee. Defaults to None.
- `since_date` *str, optional* - The date to retrieve transactions since. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The response from the API containing the payee transactions.

#### Signature

```python
def request_get_payee_transactions(
    self,
    budget_id: str = "last-used",
    payee_id: str = None,
    since_date: str = None,
    type: str = None,
    last_knowledge_of_server: int = 0,
): ...
```

### Endpoints().request_get_payees

[Show source in endpoints.py:251](../../pynab/endpoints.py#L251)

Retrieves the payees for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The response from the HTTP GET request.

#### Signature

```python
def request_get_payees(
    self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
): ...
```

### Endpoints().request_get_scheduled_transaction

[Show source in endpoints.py:698](../../pynab/endpoints.py#L698)

Retrieves a scheduled transaction from the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `scheduled_transaction_id` *str, optional* - The ID of the scheduled transaction.

#### Returns

- `dict` - The scheduled transaction information.

#### Raises

- `HTTPException` - If the request fails.

#### Signature

```python
def request_get_scheduled_transaction(
    self, budget_id: str = "last-used", scheduled_transaction_id: str = None
): ...
```

### Endpoints().request_get_scheduled_transactions

[Show source in endpoints.py:662](../../pynab/endpoints.py#L662)

Retrieves the scheduled transactions for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `last_knowledge_of_server` *int, optional* - The knowledge of the server. Defaults to 0.

#### Returns

The response from the server containing the scheduled transactions.

#### Signature

```python
def request_get_scheduled_transactions(
    self, budget_id: str = "last-used", last_knowledge_of_server: int = 0
): ...
```

### Endpoints().request_get_transaction

[Show source in endpoints.py:479](../../pynab/endpoints.py#L479)

Retrieves a specific transaction from a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transaction_id` *str, optional* - The ID of the transaction. If not provided, all transactions will be returned.

#### Returns

- `dict` - The retrieved transaction information.

#### Raises

- `HTTPError` - If the request fails or the transaction is not found.

#### Signature

```python
def request_get_transaction(
    self, budget_id: str = "last-used", transaction_id: str = None
): ...
```

### Endpoints().request_get_transactions

[Show source in endpoints.py:402](../../pynab/endpoints.py#L402)

Sends a GET request to retrieve transactions from the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget to retrieve transactions from. Defaults to "last-used".
- `since_date` *str, optional* - The date to retrieve transactions since. Defaults to None.
- `type` *str, optional* - The type of transactions to retrieve. Defaults to None.
- `last_knowledge_of_server` *int, optional* - The knowledge of the server to retrieve transactions from. Defaults to 0.

#### Returns

- `dict` - The response from the server containing the retrieved transactions.

#### Signature

```python
def request_get_transactions(
    self,
    budget_id: str = "last-used",
    since_date: str = None,
    type: str = None,
    last_knowledge_of_server: int = 0,
): ...
```

### Endpoints().request_get_user

[Show source in endpoints.py:21](../../pynab/endpoints.py#L21)

Sends a GET request to retrieve user information.

#### Returns

The response from the GET request.

#### Signature

```python
def request_get_user(self): ...
```

### Endpoints().request_import_transactions

[Show source in endpoints.py:465](../../pynab/endpoints.py#L465)

Sends a request to import transactions for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget to import transactions for. Defaults to "last-used".

#### Returns

The response from the HTTP POST request.

#### Signature

```python
def request_import_transactions(self, budget_id: str = "last-used"): ...
```

### Endpoints().request_update_category

[Show source in endpoints.py:183](../../pynab/endpoints.py#L183)

Sends a PATCH request to update a category in the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `category_id` *str, optional* - The ID of the category to update.
- `request_body` *str, optional* - The JSON request body containing the updated category data.

#### Returns

The response from the PATCH request.

#### Raises

None.

#### Signature

```python
def request_update_category(
    self, budget_id: str = "last-used", category_id: str = None, request_body: str = None
): ...
```

### Endpoints().request_update_category_for_month

[Show source in endpoints.py:228](../../pynab/endpoints.py#L228)

Sends a PATCH request to update a category for a specific month in a budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `month_id` *str, optional* - The ID of the month. Defaults to "current".
- `category_id` *str, optional* - The ID of the category to update.
- `request_body` *str, optional* - The JSON request body.

#### Returns

The response from the PATCH request.

#### Signature

```python
def request_update_category_for_month(
    self,
    budget_id: str = "last-used",
    month_id: str = "current",
    category_id: str = None,
    request_body: str = None,
): ...
```

### Endpoints().request_update_payee

[Show source in endpoints.py:288](../../pynab/endpoints.py#L288)

Sends a PATCH request to update a payee.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `payee_id` *str, optional* - The ID of the payee to update.
- `request_body` *str, optional* - The JSON request body.

#### Returns

The response from the PATCH request.

#### Signature

```python
def request_update_payee(
    self, budget_id: str = "last-used", payee_id: str = None, request_body: str = None
): ...
```

### Endpoints().request_update_transaction

[Show source in endpoints.py:499](../../pynab/endpoints.py#L499)

Updates a transaction in the specified budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `transaction_id` *str, optional* - The ID of the transaction to update.
- `request_body` *str, optional* - The JSON request body containing the updated transaction data.

#### Returns

The response from the API call.

#### Signature

```python
def request_update_transaction(
    self,
    budget_id: str = "last-used",
    transaction_id: str = None,
    request_body: str = None,
): ...
```

### Endpoints().request_update_transactions

[Show source in endpoints.py:448](../../pynab/endpoints.py#L448)

Sends a PATCH request to update transactions for a specific budget.

#### Arguments

- `budget_id` *str, optional* - The ID of the budget. Defaults to "last-used".
- `request_body` *str, optional* - The JSON request body. Defaults to None.

#### Returns

The response from the PATCH request.

#### Signature

```python
def request_update_transactions(
    self, budget_id: str = "last-used", request_body: str = None
): ...
```