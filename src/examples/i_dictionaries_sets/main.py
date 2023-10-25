#main program
import dictionaries

phonebook = {}
'''
for key in phonebook:
    print(key)

for value in phonebook.values():
    print(value)

for item in phonebook.items():
    print(item)
key,values in phonebook.items():
    print(key, values )
phonebook = {}
x = 'Y'
while x == 'Y':
    key = input("Enter Key: ")
    value = input("Enter value: ")
    phonebook[key] = value
    x = input("Press Y to enter another name to the phonebook: ")

print(phonebook)
key = input("Type name to delete: ")
del phonebook[key]

print(phonebook)
'''
'''
dictionaries.add_friend_phonebook('Chris','555-1111', phonebook)
dictionaries.add_friend_phonebook('Katie','555-2222', phonebook)
dictionaries.add_friend_phonebook('Daniel','555-3333', phonebook)
dictionaries.add_friend_phonebook('Robert','555-4444', phonebook)
dictionaries.add_friend_phonebook('Amanda','555-5555', phonebook)

for name, number in phonebook.items():
    print(name, number)

dictionaries.update_friend_phonebook('Chris','555-9999',phonebook)
print('\n')
dictionaries.delete_friend_phonebook('Katie', phonebook)
for name, number in phonebook.items():
    print(name, number)
'''
'''
myset = set('abc')
print(myset)

myset.add('d')
print(myset)

for item in myset:
    print(item)
'''
