import dictionary
nested_list =  [['T','T','T','C','C','A','T','T','T','A'],
                ['G','A','T','T','C','A','T','T','T','C'],
                ['T','T','T','C','C','A','T','T','T','T'],
                ['G','T','T','C','C','A','T','T','T','A']]

def display_menu():
    print("Homework 6 Menu")
    print("1 - Get Matrix Distance")
    print("2 - Exit")

def run_menu():
    display_menu()
    option = str(input("Select option 1 or option 2: "))
    while option not in ('1','2'):
        option = str(input("Invalid Option, Select option 1 or option 2: "))
    run_option(option)

def run_option(input):
    if input == '1':
        option_1()

    if input == '2':
        option_2()
        
def option_1():
    print("\nYou selected Option 1. Our Lists are the following")
    print("List#1 - ['T','T','T','C','C','A','T','T','T','A']")
    print("List#2 - ['G','A','T','T','C','A','T','T','T','C']")
    print("List#3 - ['T','T','T','C','C','A','T','T','T','T']")
    print("List#4 - ['G','T','T','C','C','A','T','T','T','A']")
    option = str(input("Select one of the lists (1-4) above to find the matrix distance: "))
    while option not in ('1','2','3','4'):
        option = str(input("Invalid List, Select from 1-4: "))
    option = int(option)
    y= dictionary.get_p_distance_matrix(nested_list)
    matrix_choice = y[option-1]
    print(f"\nThe matrix distance of List#{option} is {matrix_choice}.")
    print('Returning to Main Menu, Select 1 to Try Again, Select 2 to Exit')
    print('\n')
    run_menu()
    
def option_2():
    print("\nYou selected to Exit")
    while True:
        exit = input("Are you sure you want to exit? Y or N?: ")
        if exit in ('y','Y','yes','YES'):
            print('Exiting Program')
            break
        if exit in ('n','N','no','NO'):
            print("Returning to Main Menu\n")
            run_menu()
            break
        else:
            print("Invalid Option")
run_menu()