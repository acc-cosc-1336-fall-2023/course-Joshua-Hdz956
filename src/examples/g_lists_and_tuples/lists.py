def display_nums_list():
    list1 = [5, 10, 20]
    print(list1)

def display_list_w_while():
    list1 = [5, 10, 20]
    index = 0
    while index < len(list1):
        print(list1[index])
        index += 1

def display_list_w_for():
    list1 = [5, 10, 20]
    for x in range(len(list1)):
        print(list1[x])

def display_reverse_list_w_while():
    list1 = [5, 10, 20]
    len_list = len(list1)-1
    while len_list >= 0:
        print(list1[len_list])
        len_list -= 1

def display_list_w_for_reverse():
    list1 = [5, 10, 20]
    for x in range(len(list1), 0, -1):
        print(list1[x-1])

def display_list_w_for_reverse_again():
    list1 = [5, 10, 20]
    list1 = list1[::-1]
    for x in range(len(list1)):
        print(list1[x])