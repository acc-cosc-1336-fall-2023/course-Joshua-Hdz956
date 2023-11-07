class BankAccount:
    __balance = 0

    def get_balance(self):
        return self.__balance
    
    def __init__(self, balance): #constructor -- initialize class data/variable
        self.__balance = balance
    
