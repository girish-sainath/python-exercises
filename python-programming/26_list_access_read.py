# List: Access & Read

letters:list[str] = ['a', 'b', 'c', 'd']
print(f'letters: {letters}')
print(f'First Element: {letters[0]}')
print(f'Second Element: {letters[1]}')

print(f'Penultimate Element: {letters[-2]}')
print(f'Last Element: {letters[-1]}')

print(f'All Elements: {letters[:]}')

print(f'First Three Elements: {letters[0:3]}')

print(f'Elements from Index 2 to End: {letters[2:]}')

print(f'Elements from Start to Index 3: {letters[:3]}')

print(f'Elements from Index 1 to 2: {letters[1:3]}')

print(f'Every Second Element: {letters[::2]}')