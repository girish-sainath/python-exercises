# Python for solving DSA problems

## Variables are dynamically typed
n = 0
print('n = ', n)
n = 'abc'
print('n = ', n)


## Multiple assignments
n, m, o = 0.125, 'abc', True
print('n = ', n, 'm = ', m, 'o = ', o)


## Increment
n = n + 1   # good
n += 1      # better
# n++       # not supported in Python


## None is null (absence of value)
n = None
print('n = ', n)


## If statements don't need parentheses or braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 1
print('n = ', n)


## Parentheses are required for multi-line conditions or expressions
n, m = 1, 2
if ((n > 2 and
    n != m) or n == m):
    print('n and m are some values')


## While loops are similar
n = 0
print('`while n < 5:`')
while n < 5:
    print('n = ', n)
    n += 1


## For loops are more like "for each" loops in other languages
print('`for i in range(5):`')
for i in range(5):
    print('i = ', i)

print('`for i in range(1, 10, 2):`')
for i in range(1, 10, 2):
    print('i = ', i)

print('`for i in range(4, 0, -1):`')
for i in range(4, 0, -1):
    print('i = ', i)


## Division is decimal by default
print('`5 / 2`:', 5 / 2)


## Double-slash is integer division
print('`5 // 2`:', 5 // 2)


## Careful most languages round towards zero, but Python rounds towards negative infinity
print('`-5 // 2`:', -5 // 2)


## Workaround to round towards zero is using int() on the float result
print('`int(-5 / 2)`:', int(-5 / 2))


## Modulo operator is the same as other languages
print('`5 % 2`:', 5 % 2)

## Except for negative numbers, where Python's modulo operator returns a positive result
print('`-5 % 2`:', -5 % 2)


## Use math module for more consistent behavior with other languages
import math
print('`int(math.fmod(-5, 2))`:', int(math.fmod(-5, 2)))
print('`math.floor(-5 / 2)`:', math.floor(-5 / 2))
print('`math.ceil(-5 / 2)`:', math.ceil(-5 / 2))


## Max and Min Integer
n = float("inf")
m = float("-inf")


## Python numbers are infinite so they never overflow
print('`math.pow(2, 200)`:', math.pow(2, 200))
print('`float("inf") > math.pow(2, 200)`:', n > math.pow(2, 200))


## Arrays (called lists in Python) are dynamic and can hold mixed types - Dynamic Arrays can be used as stacks or queues
arr = [1, 2, 3]
print('`arr = [1, 2, 3]`:', arr)

## Append and pop are O(1) operations
arr.append(4)
print('`arr.append(4)`:', arr)
arr.append(5)
print('`arr.append(5)`:', arr)
arr.pop()
print('`arr.pop()`:', arr)

## Insert is O(n) because it has to shift elements
arr.insert(1, 7)
print('`arr.insert(1, 7)`:', arr)

## Indexing is O(1) and assignment is O(1)
arr[0] = 8
arr[3] = 9
print('`arr[0] = 8` and `arr[3] = 9`:', arr)


## Indexing supports negative indices which count backwards from the end of the array
print('`arr[0]`:', arr[0])
print('`arr[-1]`:', arr[-1])


## Initialize an array with a fixed size and default value
arr = [0] * 5
print('`arr = [0] * 5`:', arr)


## Sublists aka slicing is O(k) where k is the size of the slice
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('`arr[1:4]`:', arr[1:4])
print('`arr[:3]`:', arr[:3])
print('`arr[2:]`:', arr[2:])
print('`arr[-3:]`:', arr[-3:])
print('`arr[:-3]`:', arr[:-3])
print('`arr[::2]`:', arr[::2])
print('`arr[::-1]`:', arr[::-1])
print('`arr[-3::-1]`:', arr[-3::-1])

## Unpacking
a, b, c = [1, 2, 3]
print('`a, b, c = [1, 2, 3]`:', a, b, c)


## Looping through an array
nums = [1, 2, 3, 4, 5]

print('Nums = ', nums)
print('`for num in nums:`')
for num in nums:
    print('num = ', num)

print('`for i in range(len(nums)):`')
for i in range(len(nums)):
    print('nums[', i, '] = ', nums[i])

print('`for i, num in enumerate(nums):`')
for i, num in enumerate(nums):
    print('nums[', i, '] = ', num)

arr = ['a', 'b', 'c', 'd', 'e']
print('Arr = ', arr)

print('`for num, char in zip(nums, arr):`')
for num, char in zip(nums, arr):
    print(num, char)


nums = [34, 21, 15, 56, 78, 12, 90]
print('Nums = ', nums)
print('`sorted(nums)`:', sorted(nums))
nums.sort()
print('`nums.sort()`:', nums)
print('Nums = ', nums)

nums.sort(reverse=True)
print('`nums.sort(reverse=True)`:', nums)

arr = ['alice', 'bob', 'charlie', 'david', 'eve', 'joseph']
print('Arr = ', arr)
arr.sort(key=len)
print('`arr.sort(key=len)`:', arr)


## List comprehensions are a concise way to create lists
squares = [x**2 for x in range(10)]
print('`squares = [x**2 for x in range(10)]`:', squares)

arr = [i*2 for i in range(10) if i % 2 == 0]
print('`arr = [i*2 for i in range(10) if i % 2 == 0]`:', arr)

arr_2d = [[i*j for j in range(5)] for i in range(5)]
print('`arr_2d = [[i*j for j in range(5)] for i in range(5)]`:', arr_2d)

## Strings are similar to arrays of characters, but they are immutable
s = 'hello'
print('`s = "hello"`:', s)