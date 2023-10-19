import dictionary
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
    print("\nYou selected Option 1")
    y = create_list()
    while True:
        try:
            z = dictionary.get_p_distance_matrix_for(y)
            break
        except ValueError:
            print("STRINGS NOT OF EQUAL LENGTH, TRY AGAIN")
            y = create_list()
    print("\nThe matrix distance of your list is:")
    for i in range(len(z)):
        print(z[i])
    print('Returning to Main Menu, Select 1 to Try Again, Select 2 to Exit\n')
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
            
def create_list():
    data = []
    while True:
        try:
            n = int(input("Enter the total amount of lists you want to find the matrix distance from: "))
            if n >= 1:
                break
            else:
                print("Must input at least 1 or more")
        except ValueError:
            print("Not a whole number")
    print(f"Enter your {n} lists, SEPARATE strings with commas")
    for i in range(n):
        user_string = input(f"List No.{i+1}: ")
        user_list = user_string.split(',')
        data.append(user_list)
        
    return data

run_menu()