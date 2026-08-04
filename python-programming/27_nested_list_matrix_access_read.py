matrix:list[list[str]] = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(f'Matrix: {matrix}')
print(f'First Row: {matrix[0]}')
print(f'Second Row: {matrix[1]}')
print(f'Third Row: {matrix[-1]}')

print(matrix[0][0])
print(matrix[-1][-1])
print(matrix[1][1])

print('\nMatrix:')
for row in matrix:
    for element in row:
        print(element, end='\t')
    print()

print(matrix[:2])
print(matrix[1:])

print(matrix[2][:2])