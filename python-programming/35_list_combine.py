# Combining

letters: list[str] = ['a', 'b', 'c', 'd']
numbers: list[int] = [1, 2, 3, 4, 5]

print('Original letters list `letters`:', letters)
print('Original numbers list `numbers`:', numbers)

print('Combined list: `[letters, numbers]`', [letters, numbers])

print('Combined list with `(letters + numbers)`:', (letters + numbers))

print('Combined list with `(letters * 2)`:', (letters * 2))

comprehended: list[tuple] = [(letter, number) for letter in letters for number in numbers]
print('Combined list with list comprehension `(letter, number) for letter in letters for number in numbers]`:', comprehended)

zipped: zip = zip(letters, numbers, 'Hello')
zipped_list: list[tuple] = list(zipped)
print('Combined list with `list(zip(letters, numbers))`:', zipped_list)

numbers.extend(letters)
print('Original letters list:', letters)
print('Combined list with `numbers.extend(letters)`:', numbers)

ids = [101, 102, 103]
names = ['Alice', 'Bob', 'Charlie']
combined_list: list[tuple] = list(zip(ids, names))
print('Combined list with `list(zip(id, names))`:', combined_list)