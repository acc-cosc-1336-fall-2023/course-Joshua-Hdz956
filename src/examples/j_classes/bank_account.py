class BankAccount:
    __balance = 0

    def get_balance(self):
        return self.__balance
    
    def __init__(self, balance): #constructor -- initialize class data/variable
        self.__balance = balance
    
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount>0 and amount <= self.__balance:
            self.__balance -= amount
