import random
from customer import Customer
from atm import ATM

def scan_card(customer_list_size):
    choice = int(input("PIN: "))#1-3 for now
    return choice

def display_menu():
    print("COSC Bank")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Display Balance")
    print("4 - Exit")

def run_menu(atm):
    list_customers = [Customer(), Customer(), Customer()]

    while True:
        menu_choice = 0
        customer_index = scan_card(len(list_customers))
        customer = list_customers[customer_index]
        account_index = int(input("Enter 1 for checking, 2 for savings: "))
        while account_index not in(1,2):
            account_index = int(input("Invalid \nEnter 1 for checking, 2 for savings: "))
        account = customer.get_account(account_index)
        atm_instance = atm(account)
        while(menu_choice != '4'):
            display_menu()
            menu_choice = str(input("Enter Choice: "))
            menu_options(menu_choice, atm_instance)

def menu_options(menu_choice, ATM):
    if(menu_choice == '1'):
        ATM.make_deposit()
    elif(menu_choice == '2'):
        ATM.make_withdraw()
    elif(menu_choice == '3'):
        ATM.display_balance()
    elif(menu_choice == '4'):
        print("Exiting...")
    else:
        print("Invalid Choice, Exiting...")