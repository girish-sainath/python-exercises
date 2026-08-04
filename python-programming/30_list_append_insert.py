# List - Append and Insert

numbers = [0, 2, 3]
print(f'Original List: {numbers}')
numbers.append(4)
print(f'After Append: {numbers}')
numbers.insert(1, 1)
print(f'After Insert: {numbers}')

matrix = [[1, 2], [3, 4]]
print(f'Original Matrix: {matrix}')
matrix.append([5, 6])
print(f'After Append: {matrix}')
matrix.insert(1, [7, 8])
print(f'After Insert: {matrix}')

matrix[1].append(3)
print(f'After Appending to Row 1: {matrix}')

matrix[-1].insert(0, 0)
print(f'After Inserting to Last Row: {matrix}')