# Dictionary - Looping

my_dict:dict[str, object] = {'name': 'John', 'age': 30, 'city': 'New York', 'state': 'New York'}

print('Iterating over dictionary keys `for key in my_dict:`:')
for key in my_dict:
    print(f'Key: {key}, Value: {my_dict[key]}')

print('Iterating over dictionary items `for key, value in my_dict.items():`:')
for key, value in my_dict.items():
    print(f'Key: {key}, Value: {value}')