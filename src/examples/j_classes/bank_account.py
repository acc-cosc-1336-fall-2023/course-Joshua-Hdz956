import random
class BankAccount:
    __balance = 0

    def get_balance(self):
        return f"Balance: ${self.__balance}\n"
    
    def __init__(self, balance): #constructor -- initialize class data/variable
        if balance >= 0:
            self.__balance = balance
        else:
            self.__get_balance_from_db()
    
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount>0 and amount <= self.__balance:
            self.__balance -= amount

    def __get_balance_from_db(self):
        self.__balance = random.randint(0, 10000)

    def __str__(self):
        return f"Balance: ${self.__balance:,.2f}\n"