# Pynab

**Pynab** is a Python library designed for seamless interaction with the YNAB (You Need A Budget) API. It provides a user-friendly interface to manage your budgets, accounts, transactions, and more with ease.

Pynab currently works with YNAB's 1.72.0 API. For more information, see https://api.ynab.com/v1.

## Installation

To install Pynab, follow these steps:

```sh
git clone https://github.com/dynacylabs/pynab.git
cd pynab
python -m venv .venv
source .venv/bin/activate
pip install ./
```

## Usage

### Initialize Pynab

To begin using Pynab, initialize it with your YNAB Bearer token:

```python
from pynab import Pynab
pynab = Pynab(bearer="YOUR_BEARER_TOKEN_HERE")
```

### Retrieve Budgets

Fetch a dictionary of your budgets:

```python
budgets = pynab.budgets
```

### Retrieve a Budget by Name*

Retrieve a specific budget by its name:

```python
test_budget = pynab.budgets.by(field="name", value="test_budget", first=True)
```

### Retrieve Accounts for a Budget

Fetch all accounts associated with a budget:

```python
test_accounts = test_budget.accounts
```

### Retrieve an Account by Name*

Fetch a specific account within a budget by its name:

```python
test_account = test_budget.accounts.by(field="name", value="test_account", first=True)
```

### Retrieve Transactions for an Account

Fetch all transactions associated with a specific account:

```python
transactions = test_account.transactions
```

\* _Note: Multiple items may be returned. You should verify whether the result is a dictionary or a single `Budget`, `Account`, or `Transaction` instance._

```python
from pynab.schemas import Account
test_account = test_budget.accounts.by(field="name", value="test_account", first=False)
if isinstance(test_account, Account):
    # Single account returned
else:
    # Multiple accounts returned {account_id: account}
```

## Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**: Create a personal copy of the repository on your GitHub account.
2. **Clone the Repository**: Clone the forked repository to your local machine:
    ```sh
    git clone https://github.com/<your-username>/<repository-name>.git
    ```
3. **Create a Branch**: Always create a new branch for your changes to keep the history clean:
    ```sh
    git checkout -b <branch-name>
    ```
4. **Make Your Changes**: Edit the code using your preferred editor or IDE.
5. **Commit Your Changes**: Provide a clear commit message describing your changes:
    ```sh
    git commit -m "<commit-message>"
    ```
6. **Push Your Changes**: Push the changes to your forked repository:
    ```sh
    git push origin <branch-name>
    ```
7. **Submit a Pull Request**: On GitHub, open a pull request from your fork to the main repository for review.

Please ensure that your contributions do not break the live API tests. Run all tests before submitting your pull request.

## Testing

### Live API Testing

YNAB's API primarily offers read-only access, so you'll need to create a test budget manually for live API testing.

Live API tests confirm that Pynab's API calls are correctly interpreted by the server, and that Pynab can process the server's responses.

#### Importing a Test Budget

To import a test budget, upload `testing/test_budget.ynab4.zip` to YNAB by creating a new budget and using the "Migrate a YNAB 4 Budget" option.

#### Manually Creating a Test Budget

Follow these steps to manually create a test budget:

| Item               | Field            | Value                        | Notes                                              |
|--------------------|------------------|------------------------------|---------------------------------------------------|
| **Budget**          | `name`           | `Test Budget`                | Delete all **Category Groups** and **Categories** |
| **Category Group**  | `name`           | `Test Category Group`        |                                                   |
| **Category**        | `name`           | `Test Category`              |                                                   |
| **Account**         | `name`           | `Test Account`               |                                                   |
| **Transaction**     | `payee`          | `Test Payee`                 | Belongs to `Test Account`                         |
|                    | `memo`           | `Test Transaction`           |                                                   |
|                    | `category`       | `Test Category`              |                                                   |
| **Transaction**     | `date`           | _any future date_            | Belongs to `Test Account`                         |
|                    | `date > repeat`  | _any frequency_              |                                                   |
|                    | `memo`           | `Test Scheduled Transaction` |                                                   |

### Running Tests with Tox

Before running tests, create a `testing/.env` file with your API Bearer Token using the following format:
```sh
# ynab personal access token
API_KEY=your_API_token_goes_here
```

To run tests:
```sh
python -m venv .venv-test
source .venv-test/bin/activate
pip install -r testing/requirements.txt
tox
```

## Documentation

Please ensure any code changes are accompanied by corresponding updates to the documentation. You can generate updated documentation using Handsdown:

```sh
python -m venv .venv-docs
source .venv-docs/bin/activate
pip install -r docs/requirements.txt
handsdown
```

## Future Development

- Implement mock testing.
- Additional testing for:
  - Server knowledge validation.
  - All non-GET endpoints.
- Add comprehensive type definitions.

## License
Pynab is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
