# List - Copying
import copy

letters = ['a', 'b', 'c', 'd']
print(f'Original List: {letters}')

referenced_letters = letters
referenced_letters[3] = 'x'
print(f'Original List After Reference Modification: {letters}')
print(f'Referenced List: {referenced_letters}')

copied_letters = letters.copy()
copied_letters[2] = 'z'
print(f'Original List After Copy Modification: {letters}')
print(f'Copied List: {copied_letters}')

matrix = [[1, 2], [3, 4]]

print(f'Original Matrix: {matrix}')
referenced_matrix = matrix
referenced_matrix[0][0] = 10
print(f'Original Matrix After Reference Modification: {matrix}')
print(f'Referenced Matrix: {referenced_matrix}')


shallow_copied_matrix = matrix.copy()
shallow_copied_matrix[-1] = [5, 6]
shallow_copied_matrix[0][1] = 20
print(f'Original Matrix After Shallow Copy Modification: {matrix}')
print(f'Shallow Copied Matrix: {shallow_copied_matrix}')


deep_copy_matrix = copy.deepcopy(matrix)
deep_copy_matrix[0][0] = 30
print(f'Original Matrix After Deep Copy Modification: {matrix}')
print(f'Deep Copied Matrix: {deep_copy_matrix}')

