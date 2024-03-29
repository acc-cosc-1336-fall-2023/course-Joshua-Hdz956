def write_to_file(file_name):
    out_file = open(file_name, 'w')
    #write to file
    out_file.write("John Locke\n")
    out_file.write("David Hume\n")
    out_file.write("Edmund Burke\n")
    #close the file
    out_file.close()

def read_from_file(file_name):
    in_file = open(file_name, 'r')
    file_contents = in_file.read()
    #close file
    in_file.close()
    print(file_contents)

def read_lines_from_files(file_name):
    in_file = open(file_name, 'r')
    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()

    in_file.close()

    print(line1.strip("\n"))
    print(line2.strip("\n"))
    print(line3.strip("\n"))

def write_names_to_file(file_name, file_mode):
    out_file = open(file_name, file_mode)
    user_choice = 'y'
    while(user_choice =='y'):
        name = input("Enter friend: ")
        out_file.write(name)
        out_file.write("\n")
        user_choice = input("Would you like to enter another friend? Press y to add another friend: ")
    
    out_file.close()

def read_from_file_while(file_name):
    in_file = open(file_name)
    line = in_file.readline()

    while(line!=''):
        print(line.rstrip('\n'))
        line = in_file.readline()

    in_file.close()

def read_from_file_for(file_name):
    in_file = open(file_name)
    for line in in_file:
        print(line.rstrip('\n'))

    in_file.close()

def write_sales_data(file_name, file_mode):
    out_file = open(file_name, file_mode)

    user = 'y'
    while user.upper()=='Y':
        data = float(input("Enter Sales Data: "))
        out_file.write(str(data)+'\n')
        
        user = input("Type Y to continue...")

    out_file.close()

def read_sales_date(file_n,):
    in_file = open(file_n)
    total_sales = 0
    for amount in in_file:
        print(f'{float(amount):.2f}')
        total_sales += float(amount)
    print('------------')
    print(f'{total_sales:.2f}')
    in_file.close()

def write_field_date(file_name, file_mode):
    out_file = open(file_name, file_mode)

    user = 'Y'
    while(user.upper()=='Y'):

        name = input("Enter Name: ")
        dept_id = input("Enter DEPT ID: ")
        lang = input("Enter Language: ")

        out_file.write(f'{name},{dept_id},{lang} \n')
        user = input("Enter y to continue...")
    out_file.close()
def read_field_date(filename):
    in_file = open(filename, 'r')

    for line in in_file:
        fields = line.rstrip('\n').split(',')
        name = fields[0]
        dept_id = fields[1]
        lang = fields[2]
        print(f'{name} {dept_id} {lang}')

    
    in_file.close()

def write_city_list_file(file_name):
    cities = ['New York','Boston','Atlanta','Dallas']
    out_file = open(file_name, 'w')

    for city in cities:
        out_file.write(city + '\n')

    out_file.close()

def read_city_list_file(file_name):
    in_file = open(file_name, 'r')
    cities = []
    for line in in_file:
        cities.append(line.rstrip('\n'))

    for x in range(len(cities)):
        print(cities[x])
    
