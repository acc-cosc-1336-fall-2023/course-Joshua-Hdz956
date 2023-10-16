def get_p_distance(list1, list2):
    count = 0
    if len(list1) != len(list2):
        return 'Invalid, Lists NOT of Equal Length'
    else:
        for x in range(len(list1)):
            if list1[x] != list2[x]:
                count +=1
        return count/10

def get_p_distance_matrix(big_list):
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