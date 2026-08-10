fruits: list[str] = ["apple", "banana", "strawberry", "grapes", "plum"]

print(f"Fruits = {fruits}")
print()

# for item in iterator:
print("Class for-in loop - 'for item in iterator:'")
for fruit in fruits:
    print(f"Fruit: {fruit}")
print()

# [func(item) for item in iterator]
print("List Comprehension - '[func(item) for item in iterator]'")
fruit_in_upper: list[str] = [fruit.upper() for fruit in fruits]
print(fruit_in_upper)
print()

# for index, item in enumerate(iterator):
print("Enumerate for-in loop - 'for index, item in enumerate(iterator):'")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: Fruit '{fruit}'")
print()

# for index in range(len(collection)):
print("Range for-in loop - 'for index in range(len(collection)):'")
for i in range(len(fruits)):
    print(f"Index {i}: Fruit '{fruits[i]}'")
print()

# while condition: break-condition
print("While loop - 'while condition: break-condition'")
index: int = 0
while index < len(fruits):
    print(f"Index {index}: Fruit '{fruits[index]}'")
    index += 1
print()

colors: list[str] = ["red", "yellow", "pink", "purple"]
print(f"Colors = {colors}")
print()

# for item_1, item_2 in zip(iterator_1, iterator_2):
print("Zip 'for-in loop - for item_1, item_2 in zip(iterator_1, iterator_2)'")
for fruit, color in zip(fruits, colors):
    print(f"The '{fruit}' fruit is '{color}' in color")
print()
