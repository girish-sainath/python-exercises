# Matrix (Nested Lists)

matrix:list[list[str]] = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(f'Matrix: {matrix}')
print(f'Type: {type(matrix)}')
print(f'Length: {len(matrix)}')

mixed_matrix:list[list] = [['a', 1, True], [3.14, None, 'x'], ['y', 'z', 42]]
print(f'Mixed Matrix: {mixed_matrix}')
print(f'Type: {type(mixed_matrix)}')
print(f'Length: {len(mixed_matrix)}')