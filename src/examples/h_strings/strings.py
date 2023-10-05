def test_config():
    return True

def loop_string_w_while(str):
    i = 0

    while i < len(str):
        print(str[i])
        i += 1
    
def loop_string_w_for(str):
    
    for i in range(0, len(str)):
        print(str[i])

def loop_string_w_special_for(str):
    for ch in str:
        print(ch)

def concat_strings(str1, str2):
    return str1 + str2

def slice_string(str):
    return str[6:10]

def slice_w_step_value(str):
    return str[0:len(str):2]

def search_in_string(str1, str2):
    return str1 in str2

def use_repetition_operator(num):
    for n in range(1, num+1):
        print('*' * n)