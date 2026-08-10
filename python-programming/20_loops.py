# Loops

fruits = ['apple', 'banana', 'strawberry', 'grapes', 'plum']

## Classic for in loop
print('Classic for in loop `for fruit in fruits`:')
for fruit in fruits:
    print(fruit)

## Enumerate for in loop
print('\nEnumerate for in loop `for idx, fruit in enumerate(fruits)`:')
for idx, fruit in enumerate(fruits):
    print(f'Index: {idx} - Item: {fruit}')

## Range for in loop
print('\nRange for in loop `for i in range(len(fruits))`:')
for i in range(len(fruits)):
    print(f'Index: {i} - Item: {fruits[i]}')

## List Comprehension
print('\nList Comprehension `[print(fruit) for fruit in fruits]`:')
[print(fruit) for fruit in fruits]

## While loop
print('\nWhile loop `while idx < len(fruits)`:')
idx = 0
while idx < len(fruits):
    print(f'Index: {idx} - Item: {fruits[idx]}')
    idx += 1

## Zip for in loop
colors = ['red', 'yellow', 'pink', 'purple']
print('\nZip for in loop `for fruit, color in zip(fruits, colors)`:')
for fruit, color in zip(fruits, colors):
    print(f'The {fruit} is {color}')