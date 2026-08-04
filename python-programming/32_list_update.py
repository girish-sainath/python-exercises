# List - Update

numbers = [0, 1, 2, 3, 4]
print(f'Original List: {numbers}')
numbers[3] = 10
print(f'After Updating Index 3: {numbers}')
numbers[-1] = 20
print(f'After Updating Last Element: {numbers}')


matrix = [[1, 2], [3, 4], [5, 6]]
print(f'Original Matrix: {matrix}')
matrix[1][0] = 30
print(f'After Updating Element in Row 1: {matrix}')
matrix[-1][-1] = 60
print(f'After Updating Last Element in Last Row: {matrix}')

matrix[-1] = [7, 8]
print(f'After Updating Last Row: {matrix}')