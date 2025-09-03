# Schemas



[Pynab Index](../README.md#pynab-index) / [Pynab](./index.md#pynab) / Schemas

> Auto-generated documentation for [pynab.schemas](../../pynab/schemas.py) module.

- [Schemas](#schemas)
  - [Account](#account)
    - [Account().payee_locations](#account()payee_locations)
    - [Account().payees](#account()payees)
    - [Account().scheduled_transactions](#account()scheduled_transactions)
    - [Account().transactions](#account()transactions)
    - [Account().transfer_payees](#account()transfer_payees)
  - [Budget](#budget)
    - [Budget().accounts](#budget()accounts)
    - [Budget().accounts](#budget()accounts-1)
    - [Budget().accounts](#budget()accounts-2)
    - [Budget().categories](#budget()categories)
    - [Budget().categories](#budget()categories-1)
    - [Budget().categories](#budget()categories-2)
    - [Budget().category_groups](#budget()category_groups)
    - [Budget().category_groups](#budget()category_groups-1)
    - [Budget().category_groups](#budget()category_groups-2)
    - [Budget().detail](#budget()detail)
    - [Budget().months](#budget()months)
    - [Budget().months](#budget()months-1)
    - [Budget().months](#budget()months-2)
    - [Budget().payee_locations](#budget()payee_locations)
    - [Budget().payee_locations](#budget()payee_locations-1)
    - [Budget().payee_locations](#budget()payee_locations-2)
    - [Budget().payees](#budget()payees)
    - [Budget().payees](#budget()payees-1)
    - [Budget().payees](#budget()payees-2)
    - [Budget().scheduled_subtransactions](#budget()scheduled_subtransactions)
    - [Budget().scheduled_subtransactions](#budget()scheduled_subtransactions-1)
    - [Budget().scheduled_subtransactions](#budget()scheduled_subtransactions-2)
    - [Budget().scheduled_transactions](#budget()scheduled_transactions)
    - [Budget().scheduled_transactions](#budget()scheduled_transactions-1)
    - [Budget().scheduled_transactions](#budget()scheduled_transactions-2)
    - [Budget().settings](#budget()settings)
    - [Budget().subtransactions](#budget()subtransactions)
    - [Budget().subtransactions](#budget()subtransactions-1)
    - [Budget().subtransactions](#budget()subtransactions-2)
    - [Budget().transactions](#budget()transactions)
    - [Budget().transactions](#budget()transactions-1)
    - [Budget().transactions](#budget()transactions-2)
  - [BudgetSettings](#budgetsettings)
  - [Category](#category)
    - [Category().category_group](#category()category_group)
    - [Category().original_category_group](#category()original_category_group)
    - [Category().scheduled_subtransactions](#category()scheduled_subtransactions)
    - [Category().scheduled_transactions](#category()scheduled_transactions)
    - [Category().subtransactions](#category()subtransactions)
    - [Category().transactions](#category()transactions)
  - [CategoryGroup](#categorygroup)
  - [CurrencyFormat](#currencyformat)
  - [DateFormat](#dateformat)
  - [DebtEscrowAmounts](#debtescrowamounts)
  - [DebtInterestRates](#debtinterestrates)
  - [DebtMinimumPayments](#debtminimumpayments)
  - [Error](#error)
    - [Error().__str__](#error()__str__)
  - [Month](#month)
  - [Payee](#payee)
    - [Payee().payee_locations](#payee()payee_locations)
    - [Payee().scheduled_subtransactions](#payee()scheduled_subtransactions)
    - [Payee().scheduled_transactions](#payee()scheduled_transactions)
    - [Payee().subtransactions](#payee()subtransactions)
    - [Payee().transactions](#payee()transactions)
    - [Payee().transfer_account](#payee()transfer_account)
  - [PayeeLocation](#payeelocation)
    - [PayeeLocation().payee](#payeelocation()payee)
  - [ScheduledSubTransaction](#scheduledsubtransaction)
    - [ScheduledSubTransaction().category](#scheduledsubtransaction()category)
    - [ScheduledSubTransaction().payee](#scheduledsubtransaction()payee)
    - [ScheduledSubTransaction().scheduled_transaction](#scheduledsubtransaction()scheduled_transaction)
    - [ScheduledSubTransaction().transfer_account](#scheduledsubtransaction()transfer_account)
  - [ScheduledTransaction](#scheduledtransaction)
    - [ScheduledTransaction().account](#scheduledtransaction()account)
    - [ScheduledTransaction().category](#scheduledtransaction()category)
    - [ScheduledTransaction().payee](#scheduledtransaction()payee)
    - [ScheduledTransaction().to_dict](#scheduledtransaction()to_dict)
    - [ScheduledTransaction().to_json](#scheduledtransaction()to_json)
    - [ScheduledTransaction().transfer_account](#scheduledtransaction()transfer_account)
  - [SubTransaction](#subtransaction)
    - [SubTransaction().category](#subtransaction()category)
    - [SubTransaction().payee](#subtransaction()payee)
    - [SubTransaction().transaction](#subtransaction()transaction)
    - [SubTransaction().transfer_account](#subtransaction()transfer_account)
    - [SubTransaction().transfer_transaction](#subtransaction()transfer_transaction)
  - [Transaction](#transaction)
    - [Transaction().account](#transaction()account)
    - [Transaction().categories](#transaction()categories)
    - [Transaction().matched_transaction](#transaction()matched_transaction)
    - [Transaction().payee](#transaction()payee)
    - [Transaction().to_dict](#transaction()to_dict)
    - [Transaction().to_json](#transaction()to_json)
    - [Transaction().transfer_account](#transaction()transfer_account)
    - [Transaction().transfer_transaction](#transaction()transfer_transaction)
  - [User](#user)
    - [User().to_dict](#user()to_dict)
    - [User().to_json](#user()to_json)

## Account

[Show source in schemas.py:706](../../pynab/schemas.py#L706)

#### Signature

```python
class Account:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)

### Account().payee_locations

[Show source in schemas.py:797](../../pynab/schemas.py#L797)

Retrieves the locations associated with each payee.

#### Returns

A list of payee locations.

#### Signature

```python
@property
def payee_locations(self): ...
```

### Account().payees

[Show source in schemas.py:786](../../pynab/schemas.py#L786)

Retrieve the payees associated with the budget.

#### Returns

- `list` - A list of payees associated with the budget.

#### Signature

```python
@property
def payees(self): ...
```

### Account().scheduled_transactions

[Show source in schemas.py:822](../../pynab/schemas.py#L822)

Retrieves the scheduled transactions associated with the account.

#### Returns

- `list` - A list of scheduled transactions.

#### Signature

```python
@property
def scheduled_transactions(self): ...
```

### Account().transactions

[Show source in schemas.py:810](../../pynab/schemas.py#L810)

Retrieve transactions associated with the account.

#### Returns

- `list` - A list of transactions associated with the account.

#### Signature

```python
@property
def transactions(self): ...
```

### Account().transfer_payees

[Show source in schemas.py:776](../../pynab/schemas.py#L776)

Returns the payee associated with the transfer_payee_id.

#### Returns

The payee object associated with the transfer_payee_id.

#### Signature

```python
@property
def transfer_payees(self): ...
```



## Budget

[Show source in schemas.py:91](../../pynab/schemas.py#L91)

#### Signature

```python
class Budget:
    def __init__(self, pynab=None, _json: str = None): ...
```

### Budget().accounts

[Show source in schemas.py:184](../../pynab/schemas.py#L184)

Returns the accounts associated with the object.

#### Returns

- `list` - A list of accounts.

#### Signature

```python
@property
def accounts(self): ...
```

### Budget().accounts

[Show source in schemas.py:194](../../pynab/schemas.py#L194)

Process the given JSON string and create Account objects for each account.

#### Arguments

- `_json` *str* - The JSON string containing account information.

#### Returns

None

#### Signature

```python
@accounts.setter
def accounts(self, _json: str = ""): ...
```

### Budget().accounts

[Show source in schemas.py:209](../../pynab/schemas.py#L209)

Retrieve the accounts associated with the budget.

#### Returns

- `dict` - A dictionary containing the accounts associated with the budget.

#### Signature

```python
@accounts.getter
def accounts(self): ...
```

### Budget().categories

[Show source in schemas.py:344](../../pynab/schemas.py#L344)

Returns the categories associated with the object.

#### Returns

The categories associated with the object.

#### Signature

```python
@property
def categories(self): ...
```

### Budget().categories

[Show source in schemas.py:354](../../pynab/schemas.py#L354)

Process the given JSON string and create Category objects for each category.

#### Arguments

- `_json` *str* - The JSON string containing the categories.

#### Returns

None

#### Signature

```python
@categories.setter
def categories(self, _json: str = ""): ...
```

### Budget().categories

[Show source in schemas.py:369](../../pynab/schemas.py#L369)

Retrieves the categories associated with the budget.

If the categories have not been fetched yet, it makes a request to the Pynab API
to retrieve the budget's categories. The fetched categories are then stored in
the `_categories` attribute for future use.

#### Returns

- `dict` - A dictionary containing the budget's categories.

#### Signature

```python
@categories.getter
def categories(self): ...
```

### Budget().category_groups

[Show source in schemas.py:305](../../pynab/schemas.py#L305)

Returns the category groups associated with the object.

#### Returns

The category groups.

#### Signature

```python
@property
def category_groups(self): ...
```

### Budget().category_groups

[Show source in schemas.py:314](../../pynab/schemas.py#L314)

Parses the given JSON string and creates CategoryGroup objects for each category group.

#### Arguments

- `_json` *str* - The JSON string containing the category groups.

#### Returns

None

#### Signature

```python
@category_groups.setter
def category_groups(self, _json: str = ""): ...
```

### Budget().category_groups

[Show source in schemas.py:329](../../pynab/schemas.py#L329)

Retrieves the category groups for the budget.

If the category groups have not been fetched yet, it calls the `get_categories` method of the [Api](./api.md#api) object
passing the current budget as an argument and assigns the result to the `_category_groups` attribute.

#### Returns

- `dict` - A dictionary containing the category groups for the budget.

#### Signature

```python
@category_groups.getter
def category_groups(self): ...
```

### Budget().detail

[Show source in schemas.py:595](../../pynab/schemas.py#L595)

Retrieves detailed information about the budget.

#### Returns

The budget object with additional details.

#### Signature

```python
@property
def detail(self): ...
```

### Budget().months

[Show source in schemas.py:387](../../pynab/schemas.py#L387)

Returns the months attribute.

#### Returns

The months attribute.

#### Signature

```python
@property
def months(self): ...
```

### Budget().months

[Show source in schemas.py:396](../../pynab/schemas.py#L396)

Process the given JSON string and create Month objects for each month in the JSON.

#### Arguments

- `_json` *str* - The JSON string containing the months data.

#### Returns

None

#### Signature

```python
@months.setter
def months(self, _json: str = ""): ...
```

### Budget().months

[Show source in schemas.py:411](../../pynab/schemas.py#L411)

Returns the months associated with the budget.

If the `_months` attribute is empty, it retrieves the months using the `get_months` method from the [Api](./api.md#api) module.

#### Returns

- `dict` - A dictionary containing the months associated with the budget.

#### Signature

```python
@months.getter
def months(self): ...
```

### Budget().payee_locations

[Show source in schemas.py:262](../../pynab/schemas.py#L262)

Returns the payee locations associated with the object.

#### Returns

The payee locations.

#### Signature

```python
@property
def payee_locations(self): ...
```

### Budget().payee_locations

[Show source in schemas.py:273](../../pynab/schemas.py#L273)

Adds payee locations to the schema.

#### Arguments

- _json (str): A string representing the JSON data for payee locations.

#### Returns

None

#### Signature

```python
@payee_locations.setter
def payee_locations(self, _json: str = ""): ...
```

### Budget().payee_locations

[Show source in schemas.py:288](../../pynab/schemas.py#L288)

Retrieves and returns the payee locations associated with the budget.

If the payee locations have not been fetched yet, it calls the `get_payee_locations` method
from the [Api](./api.md#api) module to retrieve the payee locations and stores them in the `_payee_locations`
attribute. Subsequent calls to this method will return the cached payee locations.

#### Returns

- `dict` - A dictionary containing the payee locations associated with the budget.

#### Signature

```python
@payee_locations.getter
def payee_locations(self): ...
```

### Budget().payees

[Show source in schemas.py:221](../../pynab/schemas.py#L221)

Returns the payees associated with the object.

#### Returns

The payees associated with the object.

#### Signature

```python
@property
def payees(self): ...
```

### Budget().payees

[Show source in schemas.py:231](../../pynab/schemas.py#L231)

Adds payees to the schema.

#### Arguments

- `_json` *str* - A JSON string containing payee information.

#### Returns

None

#### Signature

```python
@payees.setter
def payees(self, _json: str = ""): ...
```

### Budget().payees

[Show source in schemas.py:246](../../pynab/schemas.py#L246)

Retrieves the payees associated with the budget.

If the payees have not been fetched yet, it calls the `get_payees` method from the [Api](./api.md#api) module
and stores the result in the `_payees` attribute.

#### Returns

- `dict` - A dictionary containing the payees associated with the budget.

#### Signature

```python
@payees.getter
def payees(self): ...
```

### Budget().scheduled_subtransactions

[Show source in schemas.py:551](../../pynab/schemas.py#L551)

Returns the scheduled subtransactions.

#### Returns

The scheduled subtransactions.

#### Signature

```python
@property
def scheduled_subtransactions(self): ...
```

### Budget().scheduled_subtransactions

[Show source in schemas.py:560](../../pynab/schemas.py#L560)

Process the scheduled subtransactions from the given JSON string and store them in the `_scheduled_subtransactions` dictionary.

#### Arguments

- _json (str): The JSON string containing the scheduled subtransactions.

#### Returns

- None

#### Signature

```python
@scheduled_subtransactions.setter
def scheduled_subtransactions(self, _json: str = ""): ...
```

### Budget().scheduled_subtransactions

[Show source in schemas.py:579](../../pynab/schemas.py#L579)

Retrieves the scheduled subtransactions for the budget.

If the scheduled subtransactions have not been fetched yet, it fetches them from the API
and stores them in the `_scheduled_subtransactions` attribute.

#### Returns

- `dict` - A dictionary containing the scheduled subtransactions.

#### Signature

```python
@scheduled_subtransactions.getter
def scheduled_subtransactions(self): ...
```

### Budget().scheduled_transactions

[Show source in schemas.py:506](../../pynab/schemas.py#L506)

Returns the scheduled transactions.

#### Returns

The scheduled transactions.

#### Signature

```python
@property
def scheduled_transactions(self): ...
```

### Budget().scheduled_transactions

[Show source in schemas.py:515](../../pynab/schemas.py#L515)

Adds scheduled transactions to the schema.

#### Arguments

- `_json` *str* - A JSON string representing the scheduled transactions.

#### Returns

None

#### Signature

```python
@scheduled_transactions.setter
def scheduled_transactions(self, _json: str = ""): ...
```

### Budget().scheduled_transactions

[Show source in schemas.py:534](../../pynab/schemas.py#L534)

Retrieves the scheduled transactions for the budget.

If the scheduled transactions have not been fetched yet, it calls the `get_scheduled_transactions` method
from the [Api](./api.md#api) module to fetch them and stores them in the `_scheduled_transactions` attribute.

#### Returns

- `dict` - A dictionary containing the scheduled transactions for the budget.

#### Signature

```python
@scheduled_transactions.getter
def scheduled_transactions(self): ...
```

### Budget().settings

[Show source in schemas.py:606](../../pynab/schemas.py#L606)

Retrieves the budget settings from the Pynab API.

If the settings have already been retrieved, it returns the cached settings.
Otherwise, it makes a request to the Pynab API to fetch the settings.

#### Returns

The budget settings.

#### Signature

```python
@property
def settings(self): ...
```

### Budget().subtransactions

[Show source in schemas.py:467](../../pynab/schemas.py#L467)

Returns the subtransactions of the object.

#### Returns

The subtransactions.

#### Signature

```python
@property
def subtransactions(self): ...
```

### Budget().subtransactions

[Show source in schemas.py:476](../../pynab/schemas.py#L476)

Process the subtransactions from the given JSON string and store them in the `_subtransactions` dictionary.

#### Arguments

- `_json` *str* - The JSON string containing the subtransactions.

#### Returns

None

#### Signature

```python
@subtransactions.setter
def subtransactions(self, _json: str = ""): ...
```

### Budget().subtransactions

[Show source in schemas.py:491](../../pynab/schemas.py#L491)

Retrieves the subtransactions associated with the budget.

If the subtransactions have not been fetched yet, it fetches them from the API and stores them in the `_subtransactions` attribute.

#### Returns

- `dict` - A dictionary containing the subtransactions associated with the budget.

#### Signature

```python
@subtransactions.getter
def subtransactions(self): ...
```

### Budget().transactions

[Show source in schemas.py:425](../../pynab/schemas.py#L425)

Returns the transactions associated with the object.

#### Returns

The transactions associated with the object.

#### Signature

```python
@property
def transactions(self): ...
```

### Budget().transactions

[Show source in schemas.py:434](../../pynab/schemas.py#L434)

Process the given transactions and store them in the `_transactions` dictionary.

#### Arguments

- _json (str): A string containing the transactions in JSON format.

#### Returns

- None

#### Signature

```python
@transactions.setter
def transactions(self, _json: str = ""): ...
```

### Budget().transactions

[Show source in schemas.py:450](../../pynab/schemas.py#L450)

Retrieves the transactions associated with the budget.

If the transactions have not been fetched yet, it calls the `get_transactions` method of the [Api](./api.md#api) object
passing the current budget as a parameter. The fetched transactions are then stored in the `_transactions`
attribute of the budget object.

#### Returns

- `dict` - A dictionary containing the fetched transactions.

#### Signature

```python
@transactions.getter
def transactions(self): ...
```



## BudgetSettings

[Show source in schemas.py:623](../../pynab/schemas.py#L623)

#### Signature

```python
class BudgetSettings:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)



## Category

[Show source in schemas.py:1096](../../pynab/schemas.py#L1096)

#### Signature

```python
class Category:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)

### Category().category_group

[Show source in schemas.py:1173](../../pynab/schemas.py#L1173)

Returns the category group associated with the current budget category.

#### Returns

- [CategoryGroup](#categorygroup) - The category group object associated with the current budget category.

#### Signature

```python
@property
def category_group(self): ...
```

### Category().original_category_group

[Show source in schemas.py:1183](../../pynab/schemas.py#L1183)

Returns the original category group associated with the transaction.

#### Returns

- [CategoryGroup](#categorygroup) - The original category group object.

#### Signature

```python
@property
def original_category_group(self): ...
```

### Category().scheduled_subtransactions

[Show source in schemas.py:1229](../../pynab/schemas.py#L1229)

Retrieves the scheduled subtransactions associated with the category.

#### Returns

- `list` - A list of scheduled subtransactions.

#### Signature

```python
@property
def scheduled_subtransactions(self): ...
```

### Category().scheduled_transactions

[Show source in schemas.py:1217](../../pynab/schemas.py#L1217)

Retrieves the scheduled transactions associated with the category.

#### Returns

A list of scheduled transactions.

#### Signature

```python
@property
def scheduled_transactions(self): ...
```

### Category().subtransactions

[Show source in schemas.py:1205](../../pynab/schemas.py#L1205)

Retrieves the subtransactions associated with the current category.

#### Returns

- `list` - A list of subtransactions belonging to the category.

#### Signature

```python
@property
def subtransactions(self): ...
```

### Category().transactions

[Show source in schemas.py:1193](../../pynab/schemas.py#L1193)

Retrieve transactions associated with the category.

#### Returns

- `list` - A list of transactions associated with the category.

#### Signature

```python
@property
def transactions(self): ...
```



## CategoryGroup

[Show source in schemas.py:1065](../../pynab/schemas.py#L1065)

#### Signature

```python
class CategoryGroup:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)



## CurrencyFormat

[Show source in schemas.py:669](../../pynab/schemas.py#L669)

#### Signature

```python
class CurrencyFormat:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)



## DateFormat

[Show source in schemas.py:649](../../pynab/schemas.py#L649)

#### Signature

```python
class DateFormat:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)



## DebtEscrowAmounts

[Show source in schemas.py:897](../../pynab/schemas.py#L897)

#### Signature

```python
class DebtEscrowAmounts:
    def __init__(
        self,
        pynab=None,
        budget: Budget = None,
        account: Account = None,
        _json: str = None,
    ): ...
```

#### See also

- [Account](#account)
- [Budget](#budget)



## DebtInterestRates

[Show source in schemas.py:835](../../pynab/schemas.py#L835)

#### Signature

```python
class DebtInterestRates:
    def __init__(
        self,
        pynab=None,
        budget: Budget = None,
        account: Account = None,
        _json: str = None,
    ): ...
```

#### See also

- [Account](#account)
- [Budget](#budget)



## DebtMinimumPayments

[Show source in schemas.py:866](../../pynab/schemas.py#L866)

#### Signature

```python
class DebtMinimumPayments:
    def __init__(
        self,
        pynab=None,
        budget: Budget = None,
        account: Account = None,
        _json: str = None,
    ): ...
```

#### See also

- [Account](#account)
- [Budget](#budget)



## Error

[Show source in schemas.py:52](../../pynab/schemas.py#L52)

#### Signature

```python
class Error:
    def __init__(self, pynab=None, _json: str = None): ...
```

### Error().__str__

[Show source in schemas.py:81](../../pynab/schemas.py#L81)

Returns a string representation of the object.

#### Returns

- `str` - A string representation of the object, formatted as "api error: {id} - {name} - {detail}".

#### Signature

```python
def __str__(self): ...
```



## Month

[Show source in schemas.py:1242](../../pynab/schemas.py#L1242)

#### Signature

```python
class Month:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)



## Payee

[Show source in schemas.py:928](../../pynab/schemas.py#L928)

#### Signature

```python
class Payee:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)

### Payee().payee_locations

[Show source in schemas.py:978](../../pynab/schemas.py#L978)

Retrieves the payee locations associated with the current payee.

#### Returns

A list of payee locations.

#### Signature

```python
@property
def payee_locations(self): ...
```

### Payee().scheduled_subtransactions

[Show source in schemas.py:1014](../../pynab/schemas.py#L1014)

Retrieves the scheduled subtransactions associated with the current payee.

#### Returns

A list of scheduled subtransactions.

#### Signature

```python
def scheduled_subtransactions(self): ...
```

### Payee().scheduled_transactions

[Show source in schemas.py:991](../../pynab/schemas.py#L991)

Retrieve all scheduled transactions associated with the payee.

#### Returns

- `list` - A list of scheduled transactions.

#### Signature

```python
@property
def scheduled_transactions(self): ...
```

### Payee().subtransactions

[Show source in schemas.py:1003](../../pynab/schemas.py#L1003)

Retrieves subtransactions associated with the current budget.

#### Returns

- `list` - A list of subtransactions matching the specified criteria.

#### Signature

```python
def subtransactions(self): ...
```

### Payee().transactions

[Show source in schemas.py:968](../../pynab/schemas.py#L968)

Retrieve transactions associated with the payee.

#### Returns

- `list` - A list of transactions associated with the payee.

#### Signature

```python
@property
def transactions(self): ...
```

### Payee().transfer_account

[Show source in schemas.py:958](../../pynab/schemas.py#L958)

Retrieves the account associated with the transfer_account_id.

#### Returns

- [Account](#account) - The account associated with the transfer_account_id.

#### Signature

```python
@property
def transfer_account(self): ...
```



## PayeeLocation

[Show source in schemas.py:1027](../../pynab/schemas.py#L1027)

#### Signature

```python
class PayeeLocation:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)

### PayeeLocation().payee

[Show source in schemas.py:1054](../../pynab/schemas.py#L1054)

Returns the payee associated with the transaction.

#### Returns

- [Payee](#payee) - The payee object associated with the transaction.

#### Signature

```python
@property
def payee(self): ...
```



## ScheduledSubTransaction

[Show source in schemas.py:1698](../../pynab/schemas.py#L1698)

#### Signature

```python
class ScheduledSubTransaction:
    def __init__(self, pynab=None, _json: str = None): ...
```

### ScheduledSubTransaction().category

[Show source in schemas.py:1748](../../pynab/schemas.py#L1748)

Returns the category associated with the current instance.

#### Returns

- [Category](#category) - The category object associated with the current instance.

#### Signature

```python
@property
def category(self): ...
```

### ScheduledSubTransaction().payee

[Show source in schemas.py:1741](../../pynab/schemas.py#L1741)

Returns the payee associated with the transaction.

#### Signature

```python
@property
def payee(self): ...
```

### ScheduledSubTransaction().scheduled_transaction

[Show source in schemas.py:1731](../../pynab/schemas.py#L1731)

Returns the scheduled transaction associated with the current instance.

#### Returns

The scheduled transaction object.

#### Signature

```python
@property
def scheduled_transaction(self): ...
```

### ScheduledSubTransaction().transfer_account

[Show source in schemas.py:1758](../../pynab/schemas.py#L1758)

Returns the account associated with the transfer_account_id.

#### Returns

- [Account](#account) - The account associated with the transfer_account_id.

#### Signature

```python
@property
def transfer_account(self): ...
```



## ScheduledTransaction

[Show source in schemas.py:1559](../../pynab/schemas.py#L1559)

#### Signature

```python
class ScheduledTransaction:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)

### ScheduledTransaction().account

[Show source in schemas.py:1660](../../pynab/schemas.py#L1660)

Returns the account associated with the current instance.

#### Signature

```python
@property
def account(self): ...
```

### ScheduledTransaction().category

[Show source in schemas.py:1677](../../pynab/schemas.py#L1677)

Returns the category associated with the current instance.

#### Returns

- [Category](#category) - The category object associated with the current instance.

#### Signature

```python
@property
def category(self): ...
```

### ScheduledTransaction().payee

[Show source in schemas.py:1667](../../pynab/schemas.py#L1667)

Returns the payee associated with the transaction.

#### Returns

- [Payee](#payee) - The payee object associated with the transaction.

#### Signature

```python
@property
def payee(self): ...
```

### ScheduledTransaction().to_dict

[Show source in schemas.py:1620](../../pynab/schemas.py#L1620)

Converts the object to a dictionary representation.

#### Returns

- `dict` - A dictionary representation of the object.

#### Signature

```python
def to_dict(self): ...
```

### ScheduledTransaction().to_json

[Show source in schemas.py:1648](../../pynab/schemas.py#L1648)

Convert the object to a JSON string representation.

#### Arguments

- `indent` *int, optional* - The number of spaces to use for indentation. Defaults to 4.

#### Returns

- `str` - The JSON string representation of the object.

#### Signature

```python
def to_json(self, indent: int = 4): ...
```

### ScheduledTransaction().transfer_account

[Show source in schemas.py:1687](../../pynab/schemas.py#L1687)

Returns the account associated with the transfer_account_id.

#### Returns

- [Account](#account) - The account associated with the transfer_account_id.

#### Signature

```python
@property
def transfer_account(self): ...
```



## SubTransaction

[Show source in schemas.py:1468](../../pynab/schemas.py#L1468)

#### Signature

```python
class SubTransaction:
    def __init__(self, pynab=None, budget: Budget = None, _json: str = None): ...
```

#### See also

- [Budget](#budget)

### SubTransaction().category

[Show source in schemas.py:1528](../../pynab/schemas.py#L1528)

Returns the category associated with the current instance.

#### Returns

- [Category](#category) - The category object associated with the current instance.

#### Signature

```python
@property
def category(self): ...
```

### SubTransaction().payee

[Show source in schemas.py:1518](../../pynab/schemas.py#L1518)

Returns the payee associated with the transaction.

#### Returns

- [Payee](#payee) - The payee object associated with the transaction.

#### Signature

```python
@property
def payee(self): ...
```

### SubTransaction().transaction

[Show source in schemas.py:1509](../../pynab/schemas.py#L1509)

Returns the transaction associated with the current transaction_id.

#### Returns

- [Transaction](#transaction) - The transaction object.

#### Signature

```python
def transaction(self): ...
```

### SubTransaction().transfer_account

[Show source in schemas.py:1538](../../pynab/schemas.py#L1538)

Retrieves the account associated with the transfer_account_id.

#### Returns

- [Account](#account) - The account associated with the transfer_account_id.

#### Signature

```python
@property
def transfer_account(self): ...
```

### SubTransaction().transfer_transaction

[Show source in schemas.py:1548](../../pynab/schemas.py#L1548)

Retrieves the transfer transaction associated with the current instance.

#### Returns

- [Transaction](#transaction) - The transfer transaction object.

#### Signature

```python
@property
def transfer_transaction(self): ...
```



## Transaction

[Show source in schemas.py:1283](../../pynab/schemas.py#L1283)

#### Signature

```python
class Transaction:
    def __init__(self, pynab=None, budget: Budget = None, _json: dict = None): ...
```

#### See also

- [Budget](#budget)

### Transaction().account

[Show source in schemas.py:1408](../../pynab/schemas.py#L1408)

Returns the account associated with the current instance.

#### Signature

```python
@property
def account(self): ...
```

### Transaction().categories

[Show source in schemas.py:1425](../../pynab/schemas.py#L1425)

Retrieve the categories associated with the budget.

#### Returns

- `list` - A list of categories associated with the budget.

#### Signature

```python
@property
def categories(self): ...
```

### Transaction().matched_transaction

[Show source in schemas.py:1457](../../pynab/schemas.py#L1457)

Returns the matched transaction based on the `matched_transaction_id`.

#### Returns

- [Transaction](#transaction) - The matched transaction object.

#### Signature

```python
@property
def matched_transaction(self): ...
```

### Transaction().payee

[Show source in schemas.py:1415](../../pynab/schemas.py#L1415)

Returns the payee associated with the transaction.

#### Returns

- [Payee](#payee) - The payee object associated with the transaction.

#### Signature

```python
@property
def payee(self): ...
```

### Transaction().to_dict

[Show source in schemas.py:1361](../../pynab/schemas.py#L1361)

Converts the object to a dictionary representation.

#### Returns

- `dict` - A dictionary containing the object's attributes.

#### Signature

```python
def to_dict(self): ...
```

### Transaction().to_json

[Show source in schemas.py:1396](../../pynab/schemas.py#L1396)

Convert the object to a JSON string representation.

#### Arguments

- `indent` *int, optional* - The number of spaces to use for indentation. Defaults to 4.

#### Returns

- `str` - The JSON string representation of the object.

#### Signature

```python
def to_json(self, indent: int = 4): ...
```

### Transaction().transfer_account

[Show source in schemas.py:1437](../../pynab/schemas.py#L1437)

Returns the account associated with the transfer_account_id.

#### Returns

- [Account](#account) - The account associated with the transfer_account_id.

#### Signature

```python
@property
def transfer_account(self): ...
```

### Transaction().transfer_transaction

[Show source in schemas.py:1447](../../pynab/schemas.py#L1447)

Returns the transfer transaction associated with the current instance.

#### Returns

- [Transaction](#transaction) - The transfer transaction object.

#### Signature

```python
@property
def transfer_transaction(self): ...
```



## User

[Show source in schemas.py:12](../../pynab/schemas.py#L12)

#### Signature

```python
class User:
    def __init__(self, pynab=None, _json: str = None): ...
```

### User().to_dict

[Show source in schemas.py:30](../../pynab/schemas.py#L30)

Converts the object to a dictionary.

#### Returns

- `dict` - A dictionary representation of the object, containing the 'id' attribute.

#### Signature

```python
def to_dict(self): ...
```

### User().to_json

[Show source in schemas.py:39](../../pynab/schemas.py#L39)

Convert the object to a JSON string representation.

#### Arguments

- `indent` *int, optional* - The number of spaces to use for indentation. Defaults to 4.

#### Returns

- `str` - The JSON string representation of the object.

#### Signature

```python
def to_json(self, indent: int = 4): ...
```