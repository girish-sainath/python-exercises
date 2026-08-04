# Dictionary Methods

my_dict:dict[str, object] = {'name': 'John', 'age': 30, 'city': 'New York', 'state': 'New York'}

try:
    print(my_dict['dob'])
except KeyError as e:
    print('Accessing non-existing key `my_dict["dob"]`:', e)
print('Accessing non-existing key by get `my_dict.get("dob", "Unknown")`:', my_dict.get('dob', 'Unknown'))
print('Accessing existing key by get `my_dict.get("name")`:', my_dict.get('name'))

print('Key exists `"age" in my_dict`:', 'age' in my_dict)
print('Key does not exists `"dob" not in my_dict`:', 'dob' not in my_dict)

print('Keys `my_dict.keys()`:', my_dict.keys())
print('Values `my_dict.values()`:', my_dict.values())
print('Items `my_dict.items()`:', my_dict.items())