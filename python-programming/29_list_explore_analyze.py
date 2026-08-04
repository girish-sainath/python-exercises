# List: Explore & Analyze

numbers = [45, 2, 5, 800, 60, 15, 45, 30, 15, 15]

## Analyze
print('Analyze:')
print(f'Numbers: {numbers}')
print(f'Min: {min(numbers)}')
print(f'Max: {max(numbers)}')
print(f'Sum: {sum(numbers)}')
print(f'Length: {len(numbers)}')
print(f'Average: {sum(numbers) / len(numbers)}')

## Completeness and Existence Check
print('\nCompleteness and Existence Check:')
print(f'All Elements: {all(numbers)}')
print(f'Any Element: {any(numbers)}')

## Search & Count
print('\nSearch & Count:')
print(f'Count of 15: {numbers.count(15)}')
print(f'Index of First 15: {numbers.index(15)}')
print(f'Index of First 45: {numbers.index(45)}')

## Membership & Identity
print('\nMembership & Identity:')
print(f'Is 800 in Numbers? {"Yes" if 800 in numbers else "No"}')
print(f'Is 450 not in Numbers? {"Yes" if 450 not in numbers else "No"}')

## Analysis & Checks
print('\nAnalysis & Checks:')
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f'List1: {list1}')
print(f'List2: {list2}')
print(f'List1 == List2? {"Yes" if list1 == list2 else "No"}')
print(f'List1 is List2? {"Yes" if list1 is list2 else "No"}')

list3 = [5, 2, 3]
print(f'List3: {list3}')
print(f'List1 < List3? {"Yes" if list1 < list3 else "No"}')
print(f'List1 > List3? {"Yes" if list1 > list3 else "No"}')
