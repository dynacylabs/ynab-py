# Usage Guide

This guide provides comprehensive examples for using ynab-py to interact with the YNAB API.

## Table of Contents

- [Quick Start](#quick-start)
- [Initialization](#initialization)
- [Working with Budgets](#working-with-budgets)
- [Working with Accounts](#working-with-accounts)
- [Working with Transactions](#working-with-transactions)
- [Working with Categories](#working-with-categories)
- [Working with Payees](#working-with-payees)
- [Error Handling](#error-handling)
- [Advanced Usage](#advanced-usage)
- [Best Practices](#best-practices)

## Quick Start

### Basic Example

The simplest way to use ynab-py:

```python
from ynab_py import YnabPy

# Initialize with your API token
ynab = YnabPy(bearer="YOUR_API_TOKEN")

# Get all budgets
budgets = ynab.budgets
print(budgets)
```

### Getting Started

```python
from ynab_py import YnabPy

# Initialize the client
ynab = YnabPy(bearer="YOUR_API_TOKEN")

# Retrieve budgets
budgets = ynab.budgets

# Get a specific budget by name
my_budget = ynab.budgets.by(field="name", value="My Budget", first=True)

# Get accounts from that budget
accounts = my_budget.accounts

# Get a specific account
checking = my_budget.accounts.by(field="name", value="Checking", first=True)

# Get transactions from that account
transactions = checking.transactions
```

## Initialization

### Basic Initialization

```python
from ynab_py import YnabPy

# Initialize with API token
ynab = YnabPy(bearer="YOUR_API_TOKEN")
```

### Using Environment Variables

```python
import os
from ynab_py import YnabPy

# Get token from environment
api_token = os.environ.get("YNAB_API_TOKEN")
ynab = YnabPy(bearer=api_token)
```

### With .env File

```python
from dotenv import load_dotenv
import os
from ynab_py import YnabPy

# Load environment variables
load_dotenv()
api_token = os.environ.get("YNAB_API_TOKEN")
ynab = YnabPy(bearer=api_token)
```

## Working with Budgets

### Get All Budgets

```python
from ynab_py import YnabPy

ynab = YnabPy(bearer="YOUR_API_TOKEN")

# Get all budgets as a dictionary
budgets = ynab.budgets

# Iterate through budgets
for budget_id, budget in budgets.items():
    print(f"Budget: {budget.name} (ID: {budget_id})")
```

### Get a Specific Budget

```python
from ynab_py import YnabPy
from ynab_py.schemas import Budget

ynab = YnabPy(bearer="YOUR_API_TOKEN")

# Get by name (returns first match)
budget = ynab.budgets.by(field="name", value="My Budget", first=True)

# Check if single budget returned
if isinstance(budget, Budget):
    print(f"Found budget: {budget.name}")
else:
    print("Multiple budgets found or budget not found")

# Get all budgets matching criteria (returns dict)
budgets = ynab.budgets.by(field="name", value="My Budget", first=False)
```

### Budget Properties

```python
# Access budget properties
print(f"Budget Name: {budget.name}")
print(f"Budget ID: {budget.id}")
print(f"Last Modified: {budget.last_modified_on}")
print(f"First Month: {budget.first_month}")
print(f"Last Month: {budget.last_month}")
```

## Working with Accounts

### Get All Accounts

```python
# Get all accounts for a budget
accounts = budget.accounts

# Iterate through accounts
for account_id, account in accounts.items():
    print(f"Account: {account.name}")
    print(f"  Type: {account.type}")
    print(f"  Balance: ${account.balance / 1000:.2f}")
    print(f"  On Budget: {account.on_budget}")
```

### Get a Specific Account

```python
from ynab_py.schemas import Account

# Get by name
checking = budget.accounts.by(field="name", value="Checking", first=True)

# Verify single account returned
if isinstance(checking, Account):
    print(f"Account: {checking.name}")
    print(f"Balance: ${checking.balance / 1000:.2f}")
```

### Filter Accounts

```python
# Get only on-budget accounts
on_budget_accounts = budget.accounts.by(field="on_budget", value=True, first=False)

# Get only open accounts (not closed)
open_accounts = budget.accounts.by(field="closed", value=False, first=False)

# Get by account type
checking_accounts = budget.accounts.by(field="type", value="checking", first=False)
```

### Account Properties

```python
print(f"Account Name: {account.name}")
print(f"Account ID: {account.id}")
print(f"Type: {account.type}")
print(f"Balance: ${account.balance / 1000:.2f}")
print(f"On Budget: {account.on_budget}")
print(f"Closed: {account.closed}")
print(f"Note: {account.note}")
```

## Working with Transactions

### Get Transactions for an Account

```python
# Get all transactions for an account
transactions = account.transactions

# Iterate through transactions
for txn_id, transaction in transactions.items():
    amount = transaction.amount / 1000  # Convert milliunits to dollars
    print(f"Date: {transaction.date}")
    print(f"  Payee: {transaction.payee_name}")
    print(f"  Amount: ${amount:.2f}")
    print(f"  Memo: {transaction.memo}")
```

### Filter Transactions

```python
from ynab_py.schemas import Transaction

# Get transactions by date
today_txns = account.transactions.by(field="date", value="2023-11-24", first=False)

# Get approved transactions
approved = account.transactions.by(field="approved", value=True, first=False)

# Get cleared transactions
cleared = account.transactions.by(field="cleared", value="cleared", first=False)

# Get a specific transaction
specific_txn = account.transactions.by(field="memo", value="Grocery shopping", first=True)
```

### Transaction Properties

```python
print(f"Transaction ID: {transaction.id}")
print(f"Date: {transaction.date}")
print(f"Amount: ${transaction.amount / 1000:.2f}")
print(f"Memo: {transaction.memo}")
print(f"Cleared: {transaction.cleared}")
print(f"Approved: {transaction.approved}")
print(f"Payee Name: {transaction.payee_name}")
print(f"Category Name: {transaction.category_name}")
print(f"Account ID: {transaction.account_id}")
```

### Understanding Amounts

YNAB API uses milliunits for amounts (1 dollar = 1000 milliunits):

```python
# Convert from milliunits to dollars
amount_dollars = transaction.amount / 1000

# Negative amounts are outflows (spending)
# Positive amounts are inflows (income)
if transaction.amount < 0:
    print(f"Spent: ${abs(transaction.amount / 1000):.2f}")
else:
    print(f"Received: ${transaction.amount / 1000:.2f}")
```

## Working with Categories

### Get Categories

```python
# Categories are organized in category groups
category_groups = budget.category_groups

for group_id, group in category_groups.items():
    print(f"Category Group: {group.name}")
    
    for category in group.categories:
        print(f"  Category: {category.name}")
        print(f"    Budgeted: ${category.budgeted / 1000:.2f}")
        print(f"    Activity: ${category.activity / 1000:.2f}")
        print(f"    Balance: ${category.balance / 1000:.2f}")
```

### Get a Specific Category

```python
# Find a category by name (across all groups)
groceries = None
for group_id, group in budget.category_groups.items():
    for category in group.categories:
        if category.name == "Groceries":
            groceries = category
            break
    if groceries:
        break

if groceries:
    print(f"Found category: {groceries.name}")
    print(f"Balance: ${groceries.balance / 1000:.2f}")
```

## Working with Payees

### Get All Payees

```python
# Get all payees for a budget
payees = budget.payees

for payee_id, payee in payees.items():
    print(f"Payee: {payee.name}")
    if payee.transfer_account_id:
        print(f"  (Transfer to account {payee.transfer_account_id})")
```

### Get a Specific Payee

```python
from ynab_py.schemas import Payee

# Get by name
amazon = budget.payees.by(field="name", value="Amazon", first=True)

if isinstance(amazon, Payee):
    print(f"Payee: {amazon.name}")
    print(f"Payee ID: {amazon.id}")
```

## Error Handling

### Basic Error Handling

```python
from ynab_py import YnabPy

try:
    ynab = YnabPy(bearer="INVALID_TOKEN")
    budgets = ynab.budgets
except Exception as e:
    print(f"Error: {e}")
```

### Handling Missing Items

```python
from ynab_py.schemas import Budget

# Check if item was found
budget = ynab.budgets.by(field="name", value="Nonexistent Budget", first=True)

if budget is None:
    print("Budget not found")
elif isinstance(budget, Budget):
    print(f"Found budget: {budget.name}")
else:
    print("Multiple budgets found")
```

### API Rate Limiting

YNAB API has rate limits. Handle them gracefully:

```python
import time
from ynab_py import YnabPy

ynab = YnabPy(bearer="YOUR_API_TOKEN")

try:
    budgets = ynab.budgets
except Exception as e:
    if "rate limit" in str(e).lower():
        print("Rate limit exceeded. Waiting before retry...")
        time.sleep(60)  # Wait 1 minute
        budgets = ynab.budgets
    else:
        raise
```

## Advanced Usage

### Working with Multiple Budgets

```python
from ynab_py import YnabPy

ynab = YnabPy(bearer="YOUR_API_TOKEN")

# Get all budgets
all_budgets = ynab.budgets

# Process each budget
for budget_id, budget in all_budgets.items():
    print(f"\nBudget: {budget.name}")
    
    # Get total balance across all accounts
    total_balance = 0
    for account_id, account in budget.accounts.items():
        if account.on_budget and not account.closed:
            total_balance += account.balance
    
    print(f"Total On-Budget Balance: ${total_balance / 1000:.2f}")
```

### Analyzing Spending

```python
from datetime import datetime, timedelta

# Get transactions from the last 30 days
thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

total_spending = 0
spending_by_category = {}

for txn_id, transaction in account.transactions.items():
    if transaction.date >= thirty_days_ago and transaction.amount < 0:
        # This is spending (negative amount)
        amount = abs(transaction.amount)
        total_spending += amount
        
        category = transaction.category_name or "Uncategorized"
        spending_by_category[category] = spending_by_category.get(category, 0) + amount

print(f"Total spending (last 30 days): ${total_spending / 1000:.2f}")
print("\nSpending by category:")
for category, amount in sorted(spending_by_category.items(), key=lambda x: x[1], reverse=True):
    print(f"  {category}: ${amount / 1000:.2f}")
```

### Creating Reports

```python
from collections import defaultdict

def generate_budget_report(budget):
    """Generate a comprehensive budget report."""
    
    report = {
        "budget_name": budget.name,
        "total_accounts": len(budget.accounts),
        "total_balance": 0,
        "on_budget_balance": 0,
        "off_budget_balance": 0,
        "account_types": defaultdict(int),
        "total_transactions": 0
    }
    
    # Analyze accounts
    for account_id, account in budget.accounts.items():
        report["account_types"][account.type] += 1
        
        if account.on_budget:
            report["on_budget_balance"] += account.balance
        else:
            report["off_budget_balance"] += account.balance
        
        report["total_balance"] += account.balance
        report["total_transactions"] += len(account.transactions)
    
    return report

# Generate and print report
ynab = YnabPy(bearer="YOUR_API_TOKEN")
budget = ynab.budgets.by(field="name", value="My Budget", first=True)
report = generate_budget_report(budget)

print(f"Budget Report: {report['budget_name']}")
print(f"Total Accounts: {report['total_accounts']}")
print(f"Total Balance: ${report['total_balance'] / 1000:.2f}")
print(f"On-Budget Balance: ${report['on_budget_balance'] / 1000:.2f}")
print(f"Off-Budget Balance: ${report['off_budget_balance'] / 1000:.2f}")
print(f"Total Transactions: {report['total_transactions']}")
```

## Best Practices

### 1. Store API Token Securely

```python
# ✓ Good: Use environment variables
import os
api_token = os.environ.get("YNAB_API_TOKEN")

# ✗ Bad: Hardcode token
api_token = "your_token_here"  # Don't do this!
```

### 2. Check Return Types

```python
from ynab_py.schemas import Budget

# Always check if single item or dict was returned
result = ynab.budgets.by(field="name", value="My Budget", first=True)

if isinstance(result, Budget):
    # Single budget
    print(result.name)
else:
    # Dict of budgets or None
    if result:
        for budget_id, budget in result.items():
            print(budget.name)
```

### 3. Handle API Errors

```python
try:
    ynab = YnabPy(bearer=api_token)
    budgets = ynab.budgets
except Exception as e:
    print(f"API Error: {e}")
    # Handle error appropriately
```

### 4. Be Mindful of Rate Limits

```python
import time

# Don't make too many requests too quickly
for budget_id, budget in ynab.budgets.items():
    # Process budget
    time.sleep(0.1)  # Small delay between operations
```

### 5. Work with Milliunits Correctly

```python
# Always convert milliunits to dollars for display
dollars = milliunits / 1000

# When creating transactions, convert dollars to milliunits
milliunits = dollars * 1000
```

## Examples Repository

For more examples and complete scripts, check the repository's examples directory or visit the [GitHub repository](https://github.com/dynacylabs/ynab-py).

---

## Advanced Features

### Automatic Rate Limiting

ynab-py automatically manages YNAB's 200 requests/hour rate limit, preventing errors.

```python
from ynab_py import YnabPy

# Rate limiting is enabled by default
ynab = YnabPy(bearer="your_token", enable_rate_limiting=True)

# Make as many requests as you need - rate limiter handles it
for budget in ynab.budgets.values():
    accounts = budget.accounts  # Won't exceed rate limit
    for account in accounts.values():
        transactions = account.transactions  # Automatically throttled

# Check rate limit statistics
stats = ynab.get_rate_limit_stats()
print(f"Used: {stats['requests_used']}/{stats['max_requests']}")
print(f"Remaining: {stats['requests_remaining']}")
print(f"Usage: {stats['usage_percentage']:.1f}%")
```

### Response Caching

Built-in caching reduces API calls and improves performance.

```python
# Caching is enabled by default with 5-minute TTL
ynab = YnabPy(
    bearer="your_token",
    enable_caching=True,
    cache_ttl=600  # 10 minutes
)

# First call hits the API
budgets = ynab.budgets  # API call

# Subsequent calls use cache (within TTL)
budgets_again = ynab.budgets  # From cache (fast!)

# Check cache statistics
cache_stats = ynab.get_cache_stats()
print(f"Cache hit rate: {cache_stats['hit_rate_percent']:.1f}%")
print(f"Cache size: {cache_stats['size']}/{cache_stats['max_size']}")

# Clear cache when needed
ynab.clear_cache()
```

### Enhanced Error Handling

Detailed, specific exceptions make debugging easier.

```python
from ynab_py import YnabPy
from ynab_py.exceptions import (
    AuthenticationError,
    RateLimitError,
    NotFoundError,
    NetworkError
)

ynab = YnabPy(bearer="your_token")

try:
    budget = ynab.budgets.by(field="name", value="Nonexistent", first=True)
except AuthenticationError:
    print("Invalid API token")
except NotFoundError as e:
    print(f"Resource not found: {e.error_detail}")
except RateLimitError as e:
    print(f"Rate limit exceeded. Retry after {e.retry_after} seconds")
except NetworkError as e:
    print(f"Network issue: {e.message}")
```

### Utility Functions

#### Amount Formatting

```python
from ynab_py import utils

# Convert between milliunits and dollars
milliunits = 25000
dollars = utils.milliunits_to_dollars(milliunits)  # 25.0

dollars = 15.50
milliunits = utils.dollars_to_milliunits(dollars)  # 15500

# Format for display
formatted = utils.format_amount(25000)  # "$25.00"
formatted = utils.format_amount(-15500, currency_symbol="€")  # "-€15.50"
```

#### Export to CSV

```python
from ynab_py import utils

# Export transactions to CSV
utils.export_transactions_to_csv(
    account.transactions,
    file_path="transactions.csv"
)

# Or get CSV string
csv_data = utils.export_transactions_to_csv(account.transactions)

# Custom columns
utils.export_transactions_to_csv(
    account.transactions,
    file_path="custom.csv",
    include_columns=['date', 'payee_name', 'amount', 'memo']
)
```

#### Date Filtering

```python
from ynab_py import utils
from datetime import date, timedelta

# Get transactions from last 30 days
thirty_days_ago = date.today() - timedelta(days=30)
recent = utils.filter_transactions_by_date_range(
    account.transactions,
    start_date=thirty_days_ago
)

# Specific date range
january = utils.filter_transactions_by_date_range(
    account.transactions,
    start_date="2025-01-01",
    end_date="2025-01-31"
)
```

#### Spending Analysis

```python
from ynab_py import utils

# Spending by category
spending_by_category = utils.get_spending_by_category(account.transactions)
for category, amount in sorted(spending_by_category.items(), key=lambda x: x[1], reverse=True):
    print(f"{category}: {utils.format_amount(amount)}")

# Spending by payee
spending_by_payee = utils.get_spending_by_payee(account.transactions)
top_10_payees = sorted(spending_by_payee.items(), key=lambda x: x[1], reverse=True)[:10]

# Calculate net worth
net_worth = utils.calculate_net_worth(budget)
print(f"Net Worth: {utils.format_amount(net_worth)}")
```

### Advanced Configuration

Customize ynab-py to your needs.

```python
from ynab_py import YnabPy

ynab = YnabPy(
    bearer="your_token",
    enable_rate_limiting=True,      # Automatic rate limiting
    enable_caching=True,             # Response caching
    cache_ttl=600,                   # Cache for 10 minutes
    log_level="DEBUG"                # Enable debug logging
)

# Monitor performance
print("Rate Limit Stats:", ynab.get_rate_limit_stats())
print("Cache Stats:", ynab.get_cache_stats())
```

---

## API Reference

For detailed information about the YNAB API endpoints and data structures, visit the [official YNAB API documentation](https://api.ynab.com/).
