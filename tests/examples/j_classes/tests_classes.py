import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_Bank_Account_Balance(self):
        account = BankAccount(50)
        self.assertEqual(account.get_balance(), 50)

    def test_deposit(self):
        account = BankAccount(200)
        account.deposit(100)
        self.assertEqual(account.get_balance(), 300)

    def test_withdraw(self):
        account = BankAccount(200)
        account.withdraw(10)
        self.assertEqual(account.get_balance(), 190)

    