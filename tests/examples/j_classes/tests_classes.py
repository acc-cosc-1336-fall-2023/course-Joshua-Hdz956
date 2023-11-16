import unittest
from src.examples.j_classes.bank_account import BankAccount
from src.examples.j_classes.customer import Customer

class Test_Config(unittest.TestCase):

    def test_Bank_Account_Balance(self):
        account = BankAccount(50)
        self.assertEqual(account.get_balance(), "Balance: $50\n")

    def test_deposit(self):
        account = BankAccount(200)
        account.deposit(100)
        self.assertEqual(account.get_balance(), "Balance: $300\n")

    def test_withdraw(self):
        account = BankAccount(200)
        account.withdraw(10)
        self.assertEqual(account.get_balance(), "Balance: $190\n")

    def test_get_balance_db(self):
        for _ in range(1):
            account = BankAccount(-1)
            self.assertTrue(0 <= account.get_balance() <= 10000)
            print(account.get_balance())
    
    def test_get_account_customer(self):
        customer = Customer()
        account = customer.get_account(0)
        self.assertTrue(0 <= account.get_balance() <= 10000)
        account1 = customer.get_account(1)
        self.assertTrue(0 <= account1.get_balance() <= 10000)
        print(account)
        print(account1)