"""
Tests for ynab_py.enums module.

Tests all enum classes and their values.
"""

import pytest
from ynab_py import enums


@pytest.mark.unit
class TestFrequency:
    """Test Frequency enum."""
    
    def test_all_values_exist(self):
        """Test all frequency values exist."""
        assert enums.Frequency.NEVER.value == "never"
        assert enums.Frequency.DAILY.value == "daily"
        assert enums.Frequency.WEEKLY.value == "weekly"
        assert enums.Frequency.EVERY_OTHER_WEEK.value == "everyOtherWeek"
        assert enums.Frequency.TWICE_A_MONTH.value == "twiceAMonth"
        assert enums.Frequency.EVERY_4_WEEKS.value == "every4Weeks"
        assert enums.Frequency.MONTHLY.value == "monthly"
        assert enums.Frequency.EVERY_OTHER_MONTH.value == "everyOtherMonth"
        assert enums.Frequency.EVERY_3_MONTHS.value == "every3Months"
        assert enums.Frequency.EVERY_4_MONTHS.value == "every4Months"
        assert enums.Frequency.TWICE_A_YEAR.value == "twiceAYear"
        assert enums.Frequency.YEARLY.value == "yearly"
        assert enums.Frequency.EVERY_OTHER_YEAR.value == "everyOtherYear"
        assert enums.Frequency.NONE.value is None
    
    def test_enum_access(self):
        """Test accessing enum by name."""
        freq = enums.Frequency.MONTHLY
        assert freq.value == "monthly"
        assert freq.name == "MONTHLY"


@pytest.mark.unit
class TestDebtTransactionType:
    """Test DebtTransactionType enum."""
    
    def test_all_values_exist(self):
        """Test all debt transaction type values."""
        assert enums.DebtTransactionType.PAYMENT.value == "payment"
        assert enums.DebtTransactionType.REFUND.value == "refund"
        assert enums.DebtTransactionType.FEE.value == "fee"
        assert enums.DebtTransactionType.INTEREST.value == "interest"
        assert enums.DebtTransactionType.ESCROW.value == "escrow"
        assert enums.DebtTransactionType.BALANCE_ADJUSTMENT.value == "balanceAdjustment"
        assert enums.DebtTransactionType.CREDIT.value == "credit"
        assert enums.DebtTransactionType.CHARGE.value == "charge"
        assert enums.DebtTransactionType.NONE.value is None


@pytest.mark.unit
class TestTransactionFlagColor:
    """Test TransactionFlagColor enum."""
    
    def test_all_values_exist(self):
        """Test all flag color values."""
        assert enums.TransactionFlagColor.RED.value == "red"
        assert enums.TransactionFlagColor.ORANGE.value == "orange"
        assert enums.TransactionFlagColor.YELLOW.value == "yellow"
        assert enums.TransactionFlagColor.GREEN.value == "green"
        assert enums.TransactionFlagColor.BLUE.value == "blue"
        assert enums.TransactionFlagColor.PURPLE.value == "purple"
        assert enums.TransactionFlagColor.NONE.value is None


@pytest.mark.unit
class TestTransactionClearedStatus:
    """Test TransactionClearedStatus enum."""
    
    def test_all_values_exist(self):
        """Test all cleared status values."""
        assert enums.TransactionClearedStatus.CLEARED.value == "cleared"
        assert enums.TransactionClearedStatus.UNCLEARED.value == "uncleared"
        assert enums.TransactionClearedStatus.RECONCILED.value == "reconciled"
        assert enums.TransactionClearedStatus.NONE.value is None


@pytest.mark.unit
class TestGoalType:
    """Test GoalType enum."""
    
    def test_all_values_exist(self):
        """Test all goal type values."""
        assert enums.GoalType.TARGET_CATEGORY_BALANCE.value == "TB"
        assert enums.GoalType.TARGET_CATEGORY_BALANCE_BY_DATE.value == "TBD"
        assert enums.GoalType.MONTHLY_FUNDING.value == "MF"
        assert enums.GoalType.PLAN_YOUR_SPENDING.value == "NEED"
        assert enums.GoalType.DEBT.value == "DEBT"
        assert enums.GoalType.NONE.value is None


@pytest.mark.unit
class TestAccountType:
    """Test AccountType enum."""
    
    def test_all_values_exist(self):
        """Test all account type values."""
        assert enums.AccountType.CHECKING.value == "checking"
        assert enums.AccountType.SAVINGS.value == "savings"
        assert enums.AccountType.CASH.value == "cash"
        assert enums.AccountType.CREDIT_CARD.value == "creditCard"
        assert enums.AccountType.LINE_OF_CREDIT.value == "lineOfCredit"
        assert enums.AccountType.OTHER_ASSET.value == "otherAsset"
        assert enums.AccountType.OTHER_LIABILITY.value == "otherLiability"
        assert enums.AccountType.MORTGAGE.value == "mortgage"
        assert enums.AccountType.AUTO_LOAN.value == "autoLoan"
        assert enums.AccountType.STUDENT_LOAN.value == "studentLoan"
        assert enums.AccountType.PERSONAL_LOAN.value == "personalLoan"
        assert enums.AccountType.MEDICAL_DEBT.value == "medicalDebt"
        assert enums.AccountType.OTHER_DEBT.value == "otherDebt"
        assert enums.AccountType.NONE.value is None
    
    def test_common_account_types(self):
        """Test commonly used account types."""
        checking = enums.AccountType.CHECKING
        assert checking.value == "checking"
        
        cc = enums.AccountType.CREDIT_CARD
        assert cc.value == "creditCard"
