import random

class Die:
    __roll_value = None
    def roll(self):
        roll = random.randint(1,6)
        self.__roll_value = roll
        
    def get_role_value(self):
        return self.__roll_value