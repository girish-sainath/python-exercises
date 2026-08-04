# Dictionaries

my_dict:dict[str, object] = {'name': 'John', 'age': 30, 'city': 'New York', 'state': 'New York'}
print('Dictionary:', my_dict)
print('Dictionaries are Ordered:', my_dict)
print('Dictionaries do not allow Duplicate Keys:', my_dict)
print('Dictionaries allow Duplicate Values:', my_dict)
try:
    print(my_dict[1])
except KeyError as e:
    print('Dictionaries are Unindexed:', e)
print('Dictionaries are Keyed:', my_dict['name'])
my_dict['age'] = 31
print('Dictionaries are Mutable `my_dict["age"] = 31` :', my_dict)
