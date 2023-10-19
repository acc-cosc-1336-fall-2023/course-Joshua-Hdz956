def create_tuple():
    num = (1,2,3,4,5)#tuple
    print(num)

    for i in num:
        print(i)

    for i in range(len(num)):
        print(num[i])

def create_list_from_tuple():
    num = (1,2,3,4,5)
    num_list = list(num)
    print (num_list)