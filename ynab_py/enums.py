from enum import Enum


class Frequency(Enum):
    """
    Enum representing different frequencies.

    Attributes:
        NEVER (str): Represents never.
        DAILY (str): Represents daily.
        WEEKLY (str): Represents weekly.
        EVERY_OTHER_WEEK (str): Represents every other week.
        TWICE_A_MONTH (str): Represents twice a month.
        EVERY_4_WEEKS (str): Represents every 4 weeks.
        MONTHLY (str): Represents monthly.
        EVERY_OTHER_MONTH (str): Represents every other month.
        EVERY_3_MONTHS (str): Represents every 3 months.
        EVERY_4_MONTHS (str): Represents every 4 months.
        TWICE_A_YEAR (str): Represents twice a year.
        YEARLY (str): Represents yearly.
        EVERY_OTHER_YEAR (str): Represents every other year.
        NONE (None): Represents none.
    """

    NEVER = "never"
    DAILY = "daily"
    WEEKLY = "weekly"
    EVERY_OTHER_WEEK = "everyOtherWeek"
    TWICE_A_MONTH = "twiceAMonth"
    EVERY_4_WEEKS = "every4Weeks"
    MONTHLY = "monthly"
    EVERY_OTHER_MONTH = "everyOtherMonth"
    EVERY_3_MONTHS = "every3Months"
    EVERY_4_MONTHS = "every4Months"
    TWICE_A_YEAR = "twiceAYear"
    YEARLY = "yearly"
    EVERY_OTHER_YEAR = "everyOtherYear"
    NONE = None


class DebtTransactionType(Enum):
    """
    Enum class representing different types of debt transactions.

    Attributes:
        PAYMENT (str): Represents a payment transaction.
        REFUND (str): Represents a refund transaction.
        FEE (str): Represents a fee transaction.
        INTEREST (str): Represents an interest transaction.
        ESCROW (str): Represents an escrow transaction.
        BALANCE_ADJUSTMENT (str): Represents a balance adjustment transaction.
        CREDIT (str): Represents a credit transaction.
        CHARGE (str): Represents a charge transaction.
        NONE (None): Represents no transaction type.
    """

    PAYMENT = "payment"
    REFUND = "refund"
    FEE = "fee"
    INTEREST = "interest"
    ESCROW = "escrow"
    BALANCE_ADJUSTMENT = "balanceAdjustment"
    CREDIT = "credit"
    CHARGE = "charge"
    NONE = None


class TransactionFlagColor(Enum):
    """
    Enum class representing the color of a transaction flag.

    Attributes:
        RED (str): The color red.
        ORANGE (str): The color orange.
        YELLOW (str): The color yellow.
        GREEN (str): The color green.
        BLUE (str): The color blue.
        PURPLE (str): The color purple.
        NONE (None): No color specified.
    """

    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    NONE = None


class TransactionClearedStatus(Enum):
    """
    Enum representing the cleared status of a transaction.

    Attributes:
        CLEARED (str): Represents a cleared transaction.
        UNCLEARED (str): Represents an uncleared transaction.
        RECONCILED (str): Represents a reconciled transaction.
        NONE (None): Represents no cleared status.
    """

    CLEARED = "cleared"
    UNCLEARED = "uncleared"
    RECONCILED = "reconciled"
    NONE = None


class GoalType(Enum):
    """
    Enum class representing different types of goals.

    Attributes:
        TARGET_CATEGORY_BALANCE (str): Target category balance goal type.
        TARGET_CATEGORY_BALANCE_BY_DATE (str): Target category balance by date goal type.
        MONTHLY_FUNDING (str): Monthly funding goal type.
        PLAN_YOUR_SPENDING (str): Plan your spending goal type.
        DEBT (str): Debt goal type.
        NONE (None): No goal type.
    """

    TARGET_CATEGORY_BALANCE = "TB"
    TARGET_CATEGORY_BALANCE_BY_DATE = "TBD"
    MONTHLY_FUNDING = "MF"
    PLAN_YOUR_SPENDING = "NEED"
    DEBT = "DEBT"
    NONE = None


class AccountType(Enum):
    """
    Enum representing different types of accounts.

    Attributes:
        CHECKING (str): Represents a checking account.
        SAVINGS (str): Represents a savings account.
        CASH (str): Represents a cash account.
        CREDIT_CARD (str): Represents a credit card account.
        LINE_OF_CREDIT (str): Represents a line of credit account.
        OTHER_ASSET (str): Represents an other asset account.
        OTHER_LIABILITY (str): Represents an other liability account.
        MORTGAGE (str): Represents a mortgage account.
        AUTO_LOAN (str): Represents an auto loan account.
        STUDENT_LOAN (str): Represents a student loan account.
        PERSONAL_LOAN (str): Represents a personal loan account.
        MEDICAL_DEBT (str): Represents a medical debt account.
        OTHER_DEBT (str): Represents an other debt account.
        NONE (None): Represents no account type.
    """

    CHECKING = "checking"
    SAVINGS = "savings"
    CASH = "cash"
    CREDIT_CARD = "creditCard"
    LINE_OF_CREDIT = "lineOfCredit"
    OTHER_ASSET = "otherAsset"
    OTHER_LIABILITY = "otherLiability"
    MORTGAGE = "mortgage"
    AUTO_LOAN = "autoLoan"
    STUDENT_LOAN = "studentLoan"
    PERSONAL_LOAN = "personalLoan"
    MEDICAL_DEBT = "medicalDebt"
    OTHER_DEBT = "otherDebt"
    NONE = None
