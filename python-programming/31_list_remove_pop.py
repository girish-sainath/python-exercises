# List - Remove and Pop

numbers = [0, 1, 2, 3, 4]
print(f'Original List: {numbers}')
numbers.clear()
print(f'After Clear: {numbers}')

numbers = [0, 1, 2, 3, 4]
print(f'Original List: {numbers}')
numbers.remove(2)
print(f'After Remove: {numbers}')
popped = numbers.pop()
print(f'Popped Element: {popped}')
print(f'After Pop: {numbers}')
popped = numbers.pop(-1)
print(f'Popped Element with Index: {popped}')
print(f'After Pop with Index: {numbers}')

matrix = [[1, 2], [3, 4], [5, 6]]
print(f'Original Matrix: {matrix}')
matrix.remove([3, 4])
print(f'After Remove: {matrix}')
popped_row = matrix.pop()
print(f'Popped Row: {popped_row}')
print(f'After Pop: {matrix}')

matrix = [[1, 2], [3, 4], [5, 6]]
print(f'Original Matrix: {matrix}')
matrix[0].remove(2)
print(f'After Removing Element from Row: {matrix}')
popped_element = matrix[1].pop()
print(f'Popped Element from Row: {popped_element}')
print(f'After Popping Element from Row: {matrix}')
popped_element = matrix[-1].pop(0)
print(f'Popped Element with Index from Row: {popped_element}')
print(f'After Popping Element with Index from Row: {matrix}')

