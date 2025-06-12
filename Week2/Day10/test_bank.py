# Write unit tests for the bank account project
# to ensure all methods work correctly

import pytest
from bank import Bank, SavingAccount

@pytest.fixture
def bank_account():
    return Bank("Noor Ul Huda", 1000)

def test_deposit(bank_account):
    bank_account.deposit(500)
    
    assert bank_account.current_amount == 1500

def test_withdraw(bank_account):
    bank_account.withdraw(300)
    
    assert bank_account.current_amount == 700

def test_check_balance(bank_account):
    assert bank_account.current_amount == 1000
    

def test_add_interest():
    account = SavingAccount("Ali", 1000)
    account.add_interest()
    
    assert account.current_amount == 1030.0




