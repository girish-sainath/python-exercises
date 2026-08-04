# List - Iterable and Iterator

letters: list[str] = ['a', 'b', 'c']
upper_letters:list[str] = []
for letter in letters:
    upper_letters.append(letter.upper())
    print(upper_letters)

upper_letters:list[str] = []
print('Enumerate `enumerate(letters)`:', enumerate(letters))
print('List Enumerate `list(enumerate(letters, start=1)`:', list(enumerate(letters, start=1)))
for idx, letter in enumerate(letters):
    upper_letters.append(letter.upper())
    print(f"Index: {idx}, Letter: {letter}, Upper Letters: {upper_letters}")

print('Reversed List `list(reversed(letters))` :',list(reversed(letters)))

numbers:list[int] = [1, 2, 3]
print('Zipped List `list(zip(letters))` :',list(zip(letters, numbers)))
for l, n in zip(letters, numbers):
    print(f'Letter: {l}, Number: {n}')

print([letter+letter.upper() for letter in letters])

lower_letters = ['a', 'b', 'c']
print('Mapped List `map = map(str.upper, lower_letters)`:', map(str.upper, lower_letters))
print('Mapped List `list(map(str.upper, lower_letters))`:', list(map(str.upper, lower_letters)))

numbers:list[str] = ['1', '2', '3']
print('Mapped List `list(map(int, numbers))`:', list(map(int, numbers)))

names = ['  Maria ', ' Susan  ', '  John   ']
print('Mapped List `list(map(str.strip, names))`:', list(map(str.strip, names)))

print('Iterating over mapped list `map(str.strip, names)`:')
for name in map(str.strip, names):
    print(f'Name: "{name}"')