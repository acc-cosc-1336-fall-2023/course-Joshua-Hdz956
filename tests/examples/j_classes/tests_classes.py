import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_Bank_Account_Balance(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)

    