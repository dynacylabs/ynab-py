# Enums



[Pynab Index](../README.md#pynab-index) / [Pynab](./index.md#pynab) / Enums

> Auto-generated documentation for [pynab.enums](../../pynab/enums.py) module.

- [Enums](#enums)
  - [AccountType](#accounttype)
  - [DebtTransactionType](#debttransactiontype)
  - [Frequency](#frequency)
  - [GoalType](#goaltype)
  - [TransactionClearedStatus](#transactionclearedstatus)
  - [TransactionFlagColor](#transactionflagcolor)

## AccountType

[Show source in enums.py:129](../../pynab/enums.py#L129)

Enum representing different types of accounts.

#### Attributes

- `CHECKING` *str* - Represents a checking account.
- `SAVINGS` *str* - Represents a savings account.
- `CASH` *str* - Represents a cash account.
- `CREDIT_CARD` *str* - Represents a credit card account.
- `LINE_OF_CREDIT` *str* - Represents a line of credit account.
- `OTHER_ASSET` *str* - Represents an other asset account.
- `OTHER_LIABILITY` *str* - Represents an other liability account.
- `MORTGAGE` *str* - Represents a mortgage account.
- `AUTO_LOAN` *str* - Represents an auto loan account.
- `STUDENT_LOAN` *str* - Represents a student loan account.
- `PERSONAL_LOAN` *str* - Represents a personal loan account.
- `MEDICAL_DEBT` *str* - Represents a medical debt account.
- `OTHER_DEBT` *str* - Represents an other debt account.
- `NONE` *None* - Represents no account type.

#### Signature

```python
class AccountType(Enum): ...
```



## DebtTransactionType

[Show source in enums.py:41](../../pynab/enums.py#L41)

Enum class representing different types of debt transactions.

#### Attributes

- `PAYMENT` *str* - Represents a payment transaction.
- `REFUND` *str* - Represents a refund transaction.
- `FEE` *str* - Represents a fee transaction.
- `INTEREST` *str* - Represents an interest transaction.
- `ESCROW` *str* - Represents an escrow transaction.
- `BALANCE_ADJUSTMENT` *str* - Represents a balance adjustment transaction.
- `CREDIT` *str* - Represents a credit transaction.
- `CHARGE` *str* - Represents a charge transaction.
- `NONE` *None* - Represents no transaction type.

#### Signature

```python
class DebtTransactionType(Enum): ...
```



## Frequency

[Show source in enums.py:4](../../pynab/enums.py#L4)

Enum representing different frequencies.

#### Attributes

- `NEVER` *str* - Represents never.
- `DAILY` *str* - Represents daily.
- `WEEKLY` *str* - Represents weekly.
- `EVERY_OTHER_WEEK` *str* - Represents every other week.
- `TWICE_A_MONTH` *str* - Represents twice a month.
- `EVERY_4_WEEKS` *str* - Represents every 4 weeks.
- `MONTHLY` *str* - Represents monthly.
- `EVERY_OTHER_MONTH` *str* - Represents every other month.
- `EVERY_3_MONTHS` *str* - Represents every 3 months.
- `EVERY_4_MONTHS` *str* - Represents every 4 months.
- `TWICE_A_YEAR` *str* - Represents twice a year.
- `YEARLY` *str* - Represents yearly.
- `EVERY_OTHER_YEAR` *str* - Represents every other year.
- `NONE` *None* - Represents none.

#### Signature

```python
class Frequency(Enum): ...
```



## GoalType

[Show source in enums.py:108](../../pynab/enums.py#L108)

Enum class representing different types of goals.

#### Attributes

- `TARGET_CATEGORY_BALANCE` *str* - Target category balance goal type.
- `TARGET_CATEGORY_BALANCE_BY_DATE` *str* - Target category balance by date goal type.
- `MONTHLY_FUNDING` *str* - Monthly funding goal type.
- `PLAN_YOUR_SPENDING` *str* - Plan your spending goal type.
- `DEBT` *str* - Debt goal type.
- `NONE` *None* - No goal type.

#### Signature

```python
class GoalType(Enum): ...
```



## TransactionClearedStatus

[Show source in enums.py:91](../../pynab/enums.py#L91)

Enum representing the cleared status of a transaction.

#### Attributes

- `CLEARED` *str* - Represents a cleared transaction.
- `UNCLEARED` *str* - Represents an uncleared transaction.
- `RECONCILED` *str* - Represents a reconciled transaction.
- `NONE` *None* - Represents no cleared status.

#### Signature

```python
class TransactionClearedStatus(Enum): ...
```



## TransactionFlagColor

[Show source in enums.py:68](../../pynab/enums.py#L68)

Enum class representing the color of a transaction flag.

#### Attributes

- `RED` *str* - The color red.
- `ORANGE` *str* - The color orange.
- `YELLOW` *str* - The color yellow.
- `GREEN` *str* - The color green.
- `BLUE` *str* - The color blue.
- `PURPLE` *str* - The color purple.
- `NONE` *None* - No color specified.

#### Signature

```python
class TransactionFlagColor(Enum): ...
```