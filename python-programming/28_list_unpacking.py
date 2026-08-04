# List: Unpacking

profile = ['Maria', 30, 'Engineer', 'New York']

# name = profile[0]
# age = profile[1]
# profession = profile[2]
# city = profile[3]

print("Code: `profile = ['Maria', 30, 'Engineer', 'New York']`")

print('\nUnpacking List:')
print('Code: `name, age, profession, city = profile`')
name, age, profession, city = profile
print(f'Profile: {profile}')
print(f'Name: {name}')
print(f'Age: {age}')
print(f'Role: {profession}')
print(f'City: {city}')

print('\nUnpacking List with * Operator:')
print('Code: `name, *details, city = profile`')
name, *details, city = profile
print(f'Profile: {profile}')
print(f'Name: {name}')
print(f'Details: {details}')
print(f'City: {city}')

print('\nUnpacking List with _ Placeholder:')
print('Code: `name, _, profession, _ = profile`')
name, _, profession, _ = profile
print(f'Profile: {profile}')
print(f'Name: {name}')
print(f'Profession: {profession}')

print('\nUnpacking List with * Operator with _ Placeholder:')
print('Code: `name, *_, city = profile`')
name, *_, city = profile
print(f'Profile: {profile}')
print(f'Name: {name}')
print(f'City: {city}')

vowels = 'AEIOU'
print("Code: `vowels = 'AEIOU'`")
print('\nUnpacking String with * Operator and _ Placeholder:')
print('Code: `a, _, *rest = vowels`')
a, _, *rest = vowels
print(f'Vowels: {vowels}')
print(f'First Vowel: {a}')
print(f'Rest of Vowels: {rest}')