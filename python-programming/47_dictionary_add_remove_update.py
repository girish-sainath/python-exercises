# Dictionary - Add, Remove, Update

my_dict:dict[str, object] = {'name': 'John', 'age': 30, 'city': 'New York', 'state': 'New York'}
print('Dictionary:', my_dict)

my_dict['id'] = 12345
print('Add `my_dict["id"] = 12345`:', my_dict)

my_dict['age'] = 31
print('Update `my_dict["age"] = 31`:', my_dict)

my_dict.update({'age': 32, 'city': 'Los Angeles'})
print('Update `my_dict.update({"age": 32, "city": "Los Angeles"})`:', my_dict)

state = my_dict.pop('state')
print('Remove `my_dict.pop("state")`:', my_dict, 'Removed state:', state)

try:
    my_dict.pop('state')
except KeyError as e:
    print('Remove non-existing key `my_dict.pop("state")`:', e)

my_dict.pop('state', None)
print('Remove non-existing key by pop with default `my_dict.pop("state", None)`:', my_dict, 'Removed state:', None)

my_dict.popitem()
print('Remove `my_dict.popitem()`:', my_dict)

user = dict.fromkeys(['id', 'name', 'age', 'city'], None)
print('Create dictionary from keys `dict.fromkeys(["id", "name", "age"], None)`:', user)