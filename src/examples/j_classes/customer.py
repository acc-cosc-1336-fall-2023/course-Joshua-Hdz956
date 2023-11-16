from bank_account import BankAccount
class Customer:
    __list_accounts = []

    def __init__(self):
        self.__list_accounts.append(BankAccount(-1))
        self.__list_accounts.append(BankAccount(-1))
    
    def get_account(self, index):
        return self.__list_accounts[index]