# Dictionary - Challenge

user = {'id': 3, 'name': 'John', 'age': 30, 'city': 'New York', 'state': 'New York'}
print('Original dictionary:', user)

user_string_values_uppercase = {}
for key, value in user.items():
    if isinstance(value, str):
        user_string_values_uppercase[key] = value.upper()
print('Uppercase string values:', user_string_values_uppercase)

user_string_values_uppercase_comprehension = {key: value.upper() for key, value in user.items() if isinstance(value, str)}
print('Uppercase string values (comprehension) `{key: value.upper() for key, value in user.items() if isinstance(value, str)}`:', user_string_values_uppercase_comprehension)
