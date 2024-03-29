def get_p_distance(list1, list2):
    count = 0
    if len(list1) != len(list2):
        raise ValueError("LISTS NOT EQUAL IN LENGTH")
    else:
        for x in range(len(list1)):
            if list1[x] != list2[x]:
                count +=1
        return round((count/len(list1)),5)

def get_p_distance_matrix_for(nested_list):
    n = len(nested_list)
    matrix = []
    for i in range(n):
        list = []
        for j in range(n):
            x = get_p_distance(nested_list[i], nested_list[j])
            list.append(x)
        matrix.append(list)
    return matrix

def get_p_distance_matrix_while(big_list):
    n = len(big_list)
    matrix = []
    i = 0
    while i < n:
        row = [0.0] * n
        j = 0
        
        while j < n:
            row[j] = (get_p_distance(big_list[i], big_list[j]))
            j += 1
        
        matrix.append(row)
        
        i += 1
        
    return matrix

        