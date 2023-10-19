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

def get_list_total_while(list1):
    indx = 0
    sum = 0
    while(indx < len(list1)):
        sum += list1[indx]
        indx += 1
    return sum

def get_list_total_for(list1):
    sum = 0
    for i in range(0, len(list1)):
        sum += list1[i]
    return sum

def list_ref_parameter(list1):
    print(list1)
    print(id(list1))
    list1[0] = 0

def get_list_return_value(list1):
    list1[0] = 0
    return list1

def search_for_item_in_list(item, list1):
    return item in list1

def get_time_table(max_value):
    table = []

    for r in range(1, max_value+1):
        row = []
        for c in range(1, max_value+1):
            row.append(r*c)
        table.append(row)
        
    return table