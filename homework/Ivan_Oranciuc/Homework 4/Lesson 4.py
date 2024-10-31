my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': ["apple", "banana", "cherry", "pineapple", "onion"],
           'dict': {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5},
           'set': {"apple", "cherry", False, True, "1"}
           }
print(my_dict["tuple"][-1])

my_dict["list"].append(21)
my_dict['list'].remove('banana')

my_dict['dict']['i am a tuple'] = '2'
del my_dict['dict']['second']

my_dict['set'].add(5)
my_dict['set'].remove(True)

print(my_dict)
