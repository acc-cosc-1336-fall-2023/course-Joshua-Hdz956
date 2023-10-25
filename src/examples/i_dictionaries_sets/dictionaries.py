def test_config():
    return True
def is_key_in_dictionary(key, dictionary):
    return key in dictionary

def add_friend_phonebook(name, number, phonebook):
    phonebook[name] = number

def update_friend_phonebook(name, number, phonebook):
    if name in phonebook:
        phonebook[name] = number

def delete_friend_phonebook(name, phonebook):
    if name in phonebook:
        del phonebook[name]