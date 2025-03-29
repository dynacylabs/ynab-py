# Pynab



[Pynab Index](../README.md#pynab-index) / [Pynab](./index.md#pynab) / Pynab

> Auto-generated documentation for [pynab.pynab](../../pynab/pynab.py) module.

- [Pynab](#pynab)
  - [Pynab](#pynab-1)
    - [Pynab().budgets](#pynab()budgets)
    - [Pynab().server_knowledges](#pynab()server_knowledges)
    - [Pynab().user](#pynab()user)

## Pynab

[Show source in pynab.py:5](../../pynab/pynab.py#L5)

#### Signature

```python
class Pynab:
    def __init__(self, bearer: str = None): ...
```

### Pynab().budgets

[Show source in pynab.py:65](../../pynab/pynab.py#L65)

Retrieves the budgets from the API.

#### Returns

- `list` - A list of budgets.

#### Signature

```python
@property
def budgets(self): ...
```

### Pynab().server_knowledges

[Show source in pynab.py:40](../../pynab/pynab.py#L40)

Retrieves the server knowledge for a specific endpoint.

#### Arguments

- `endpoint` *str* - The endpoint for which to retrieve the server knowledge. If not provided, the default value is None.

#### Returns

- `int` - The server knowledge for the specified endpoint. If server knowledge tracking is disabled, returns 0.

#### Signature

```python
def server_knowledges(self, endpoint: str = None): ...
```

### Pynab().user

[Show source in pynab.py:55](../../pynab/pynab.py#L55)

Retrieves the user information from the API.

#### Returns

- `dict` - A dictionary containing the user information.

#### Signature

```python
@property
def user(self): ...
```