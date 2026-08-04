# List - Sorting

numbers = [400, 100, 300, 200]
print(f'Original List: {numbers}')
numbers.sort()
print(f'After Sort: {numbers}')
numbers.sort(reverse=True)
print(f'After Sort in Reverse: {numbers}')

matrix = [[3, 4], [1, 2], [5, 6]]
print(f'Original Matrix: {matrix}')
matrix.sort()
print(f'After Sort: {matrix}')
matrix = [[3, 4], [1, 7], [5, 1]]
matrix.sort(key=lambda x: x[1])
print(f'After Sort by Second Element: {matrix}')

letters = ['d', 'b', 'a', 'c']
print(f'Original List: {letters}')

sorted_letters = sorted(letters)
print(f'Original List After Sorted: {letters}')
print(f'Sorted List (New): {sorted_letters}')

sorted_letters_desc = sorted(letters, reverse=True)
print(f'Original List After Sorted in Reverse: {letters}')
print(f'Sorted List in Reverse (New): {sorted_letters_desc}')

letters = ['d', 'b', 'a', 'c']
print(f'Original List After Reverse: {letters}')
letters.reverse()
print(f'After Reverse: {letters}')

print(f'Original List After Reverse: {letters}')
reversed_letters = list(reversed(letters))
print(f'Original List After Reversed: {letters}')
print(f'Reversed List (New): {reversed_letters}')
