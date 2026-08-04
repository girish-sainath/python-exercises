# Donne Martin Python for Data Structures Part 1 (Data Structures)
from cffi.backend_ctypes import xrange

## Tuple (one dimensional, fixed-length, immutable sequence)
### Create a tuple
tuple_1 = (1, 2, 3)
print('Tuple - `tuple_1 = (1, 2, 3)`:', tuple_1)

### Convert to a tuple from list
list_1 = [1, 2, 3]
print('List - `list_1 = [1, 2, 3]`:', list_1)
print('List type - `type(list_1)`:', type(list_1))
print('Tuple from List - `tuple(list_1)`:', tuple(list_1))
print('Tuple from List Type - `type(tuple(list_1))`:', type(tuple(list_1)))

##¸ Create a nested tuple
nested_tuple = ([1, 2, 3], (4, 5))
print('Nested tuple - `nested_tuple = ([1, 2, 3], (4, 5))`:', nested_tuple)

### Access a tuple's elements by index O(1)
print('Accessing element by index from Tuple O(1) - `nested_tuple[0]`:', nested_tuple[0])

### Tuples though immutable can contain mutable objects that can be changed
nested_tuple[0].append(4)
print('Changing the mutable object of a nested tuple - `nested_tuple[0].append(4)`:', nested_tuple)

### Concatenate tuples by creating a new tuple and copying objects:
tuple_1 = (1, 3, 2)
tuple_2 = (4, 5, 6)
concatenated_tuple = tuple_1 + tuple_2
print('Concatenated tuple - `(1, 3, 2) + (4, 5, 6)`:', concatenated_tuple)

### Multiply tuples to copy references to objects (objects themselves are not copied)
tuple_1 = ('foo', 'bar')
multiplied_tuple = tuple_1 * 2
print('Multiply tuple - `("foo", "bar") * 2`:', multiplied_tuple)

### Multiply nested tuples to copy references to objects (objects themselves are not copied)
nested_tuple = ([1, 2, 3], (4, 5))
multiplied_nested_tuple = nested_tuple * 2
print('Multiple Nested Tuple - `([1, 2, 3], (4, 5)) * 2`:', multiplied_nested_tuple)

### Modifying the mutable objects of a multiplied nested tuple
multiplied_nested_tuple[0].append(6)
print('Changing the mutable object of a nested tuple - `multiplied_nested_tuple[0].append(6)`:', multiplied_nested_tuple)

### Unpack tuples
a, b = nested_tuple
print('Unpacking Tuple - `a, b = nested_tuple`:', a, b)

### Unpack nested tuples
(a, b, c, d), (e, f) = nested_tuple
print('Unpacking nested tuple - `(a, b, c, d), (e, f) = nested_tuple`:', a, b, c, d, e, f)

### Unpacking when iterating over sequences of tuples or lists
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('Seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]', seq)
print('Iterating over list with unpacking - `for a, b, c in seq`:')
for a, b, c in seq:
    print(a, b, c)

## List (one dimensional, variable-length, mutable sequence)
### Create a list
list_1 = [1, 2, 3]
print('List - `list_1 = [1, 2, 3]`:', list_1)

### Convert to a list from tuple
tuple_1 = (1, 2, 3)
print('Tuple - `tuple_1 = (1, 2, 3)`:', tuple_1)
print('Tuple Type - `type(tuple_1)`:', type(tuple_1))
print('List from Tuple - `list(tuple_1)`:', list(tuple_1))
print('List from Tuple Type - `type(list(tuple_1))`:', type(list(tuple_1)))

### Create a nested list
nested_list = [(1, 2, 3), [4, 5]]
print('Nested List - `nested_list = [(1, 2, 3), [4, 5]]`:', nested_list)

### Access a list's elements by index O(1)
print('Element by Index from List O(1) - `nested_list[0]`:', nested_list[0])

### Append an element to a list O(1)
nested_list.append(6)
print('Append element to list - `nested_list.append(6)`:', nested_list)

### Insert an element to a list at a specific index (insert is expensive due to the shifts required) O(n)
nested_list.insert(0, 'start')
print('Insert element to list - `nested_list.insert(0, "start")`:', nested_list)

### Pop an element from a list from a specific index (pop is expensive due to the shifts required) O(n)
popped = nested_list.pop(0)
print('Pop element from list - `nested_list.pop(0)`:', popped, nested_list)

### Locate the first value and remove O(n)
nested_list.remove([4, 5])
print('Remove element from list - `nested_list.remove([4, 5])`:', nested_list)

### Check if list contains a value O(n)
print('Check if list contains value - `6 in nested_list`:', (6 in nested_list))

### Concatenate lists by creating a new list and copying objects:
list_1 = [1, 3, 2]
list_2 = [4, 5, 6]
concatenated_list = list_1 + list_2
print('Concatenated List - `[1, 3, 2] + [4, 5, 6]`:', concatenated_list)

### Multiply tuples to copy references to objects (objects themselves are not copied)
list_1 = ['foo', 'bar']
multiplied_list = list_1 * 2
print('Multiply List - `["foo", "bar"] * 2`:', multiplied_list)

### Multiply nested lists to copy references to objects (objects themselves are not copied)
nested_list = [(1, 2, 3), [4, 5]]
multiplied_nested_list = nested_list * 2
print('Multiple Nested List - `[(1, 2, 3), [4, 5]] * 2`:', multiplied_nested_list)

### Extend a list by appending elements (faster than concatenating as it does not crete a new list)
list_3 = [7, 8, 9]
nested_list.extend(list_3)
print('Extend list by appending elements - `nested_list.extend([7, 8, 9])`:', nested_list)

## Dictionary (hash map or associative array, mutable collection of key-value pairs)
### Create a dict
dict_1 = {'a': 'foo', 'b': [0, 1, 2, 3]}
print('Dict - `dict_1 = {"a": "foo", "b": [0, 1, 2, 3]}`:', dict_1)

### Access a dict's elements by index or key O(1)
print('Accessing element by index or key - `dict_1["b"]`:', dict_1['b'])

### Insert or set a dict's elements by index or key O(1)
dict_1[5] = 'bar'
print('Insert or set a dict"s elements by index or key - `dict_1[5] = "bar"`:', dict_1)

### Check if a dict contains a index or key O(1)
print('Check if dict contains a key - `5 in dict_1`:', (5 in dict_1))

### Delete a value from a dict O(1)
dict_2 = dict(dict_1)
print('Create a dict from another dict - `dict_2 = dict(dict_1)`:', dict_2)
del dict_2[5]
print('Delete a value from a dict - `del dict_2[5]`:', dict_1, dict_2)

### Remove with 'pop' and return an element from a specified index O(1)
value = dict_2.pop('b')
print('Remove and return an element from a specified index - `value = dict_2.pop("b")`:', value, dict_2)

value = dict_2.pop('c', 'Unknown')
print('Remove and return an element from a specified index - `value = dict_2.pop("c", "Unknown")`:', value, dict_2)

### Remove with 'get' and return an element from a specified index O(1)
value = dict_2.get('b')
print('Remove and return an element from a specified index - `value = dict_2.get("b")`:', value, dict_2)

value = dict_2.get('c', 'Unknown')
print('Remove and return an element from a specified index - `value = dict_2.get("c", "Unknown")`:', value, dict_2)

### Return a default value with 'setdefault' if the key is not found
print('Return a default value if key not found - `dict_1.setdefault("b", None)`:', dict_1.setdefault('b', None), dict_1)
print('Return a default value if key not found - `dict_1.setdefault("c", None)`:', dict_1.setdefault('c', None), dict_1)

### In contrast to 'setdefault', 'defaultdict' from the 'collections' module lets you specify the default when the container is initialized
from collections import defaultdict

seq = ['foo', 'bar', 'baz']
first_letter = defaultdict(list)
print(first_letter)
for elem in seq:
    first_letter[elem[0]].append(elem)
print(first_letter)

### dict keys must be 'hashable', they must be immutable objects like scalers (int, float, string or tuples whose objects are all immutable)
### list is mutable so cannot be hashable and cannot
print('Hash of string - `hash("string")`:', hash('string'))
print('Hash of tuple - `hash((1, 2, (3, 4)))`:', hash((1, 2, (3, 4))))

### Get keys of a dictionary
print('Keys of a dictionary - `dict_1.keys()`:', dict_1.keys())

### Get values of a dictionary
print('Values of a dictionary - `dict_1.values()`:', dict_1.values())

### Iterate through dict's keys and values
print('Keys and Values of a dictionary with items - `for key, value in dict_1.items()`:')
for key, value in dict_1.items():
    print(key, value)

### Merge one dict into another
dict_1.update({'e': 'elephant', 'f': 'fish'})
print('Merge one dict into another - `dict_1.update({"e": "elephant", "f": "fish"})`:', dict_1)

### Pair up two sequences element-wise in a dict
mapping = dict(zip(range(7), reversed(range(7))))
print('Pair up two sequences element-wise in a dict - `mapping = dict(zip(range(7), reversed(range(7))))`:', mapping)

## Set
### Create a set
set_1 = set([0, 1, 2, 3, 4, 5])
print('Set - `set_1 = set([0, 1, 2, 3, 4, 5])`:', set_1)

set_2 = {1, 2, 3, 5, 8, 13}
print('Set - `set_2 = {1, 2, 3, 5, 8, 13}`:', set_2)

### Union of two sets
print('Union of two sets - `set_1 | set_2`:', (set_1 | set_2))
print('Union of two sets - `set_2 | set_1`:', (set_2 | set_1))

### Intersection of two sets
print('Intersection of two sets - `set_1 & set_2`:', (set_1 & set_2))
print('Intersection of two sets - `set_2 & set_1`:', (set_2 & set_1))

### Difference of one set from another set
print('Difference of set_1 from set_2 - `set_1 - set_2`:', (set_1 - set_2))
print('Difference of set_2 from set_1 - `set_2 - set_1`:', (set_2 - set_1))

### Symmetric Difference of two sets
print('Symmetric Difference of two sets - `set_1 ^ set_2`:', (set_1 ^ set_2))
print('Symmetric Difference of two sets - `set_2 ^ set_1`:', (set_2 ^ set_1))

set_3 = {1, 2, 3}
print('Set 3 - `set_3 = {1, 2, 3}`:', set_3)

### Subset of a set
print('Subset of a set - `set_3.issubset(set_2)`:', set_3.issubset(set_2))

### Superset of a set
print('Superset of a set - `set_2.issuperset(set_3)`:', set_2.issuperset(set_3))

### Set Equals
print('Set Equals - `{1, 2, 3} == {3, 2, 1}`:', ({1, 2, 3} == {3, 2, 1}))

# Donne Martin Python for Data Structures Part 2 (Data Structures Utilities)
## Slice - selects a section of list types (arrays, tuples, NumPy arrays with arguments [start:end:step]) - start is included and end is excluded
seq = 'Monty Python'
print('String - `seq = "Monty Python"`:', seq)
print('Seq from 6 to 10 - `seq[6:10]`:', seq[6:10])
print('Omit start to default to start of the sequence - `seq[:5]`:', seq[:5])
print('Omit end to default to end of the sequence - `seq[6:]`:', seq[6:])
print('Negative indices slice relative to the end - `seq[-12:-7]`:', seq[-12:-7])
print('Get every other element - `seq[::2]`:', seq[::2])
print('Passing -1 for the step to reverse - `seq[::-1]`:', seq[::-1])
seq = ['M', 'o', 'n', 't', 'y', 'P', 'y', 't', 'h', 'o', 'n']
print("List - `seq = ['M', 'o', 'n', 't', 'y', 'P', 'y', 't', 'h', 'o', 'n']`:", seq)
seq[12:] = ['H', 'a', 'l', 'l']
print('Assign elements to a slice - `seq[5:] = ["H", "a", "l", "l"]`:', seq)

## Range (range)
print('Range - `range(10)`:', range(10))
print('range(start, end, step) - `range(0, 20, 3)`:', range(0, 20, 3))

## XRange (xrange)
print('XRange - `xrange(100000)`:', xrange(100000))

seq = [1, 2, 2, 3, 5, 13]
print('Seq sorted - `seq = [1, 2, 2, 3, 5, 13]`:', seq)

import bisect
## Bisect (bisect.bisect) - Location to insert element in a sorted list
print('Bisect on a sorted list - `bisect.bisect(seq, 8)`:', bisect.bisect(seq, 8))

## Insort (bisect.insort) - Insert element in a sorted list
bisect.insort(seq, 8)
print('Insert in a sorted list - `bisect.insort(seq, 8)`:', seq)

seq = [13, 3, 2, 1, 2, 5]
print('Seq unsorted - `seq = [13, 3, 2, 1, 2, 5]`:', seq)

## Bisect (bisect.bisect) - Location to insert element in a unsorted list
print('Bisect on a unsorted list - `bisect.bisect(seq, 8)`:', bisect.bisect(seq, 8))

## Insort (bisect.insort) - Insert element in a unsorted list
bisect.insort(seq, 8)
print('Insert in a unsorted list - `bisect.insort(seq, 8)`:', seq)

## Sorted
print('Sorted function on unsorted list - `sorted(seq)`:', sorted(seq))

## Reversed
print('Reversed function on unsorted list - `reversed(seq)`:', list(reversed(seq)))

## Sort
seq.sort()
print('Sort method on unsorted list - `seq.sort()`:', seq)

## Sort Reverse
seq.sort(reverse=True)
print('Sort method on unsorted list with reverse - `seq.sort(reverse=True)`:', seq)

## Enumerate
strings = ['foo', 'bar', 'baz']
print("Strings - `strings = ['foo', 'bar', 'baz']`:", strings)
print('Enumerate with index and value - `for i, string in enumerate(strings)`:')
for i, string in enumerate(strings):
    print(i, string)

## Zip
strings = ['foo', 'bar', 'baz']
seq = [1, 2, 3]
print("Seq - `seq = [1, 2, 3]`:", seq)

bools = [True, False, None]
print("Bools - `bool = [True, False, None]`:", bools)

print('Zip with strings and seq and bools - `list(zip(strings, seq, bools))`:', list(zip(strings, seq, bools)))

for i, (a, b) in enumerate(zip(strings, seq)):
    print('%d: %s, %s' % (i, a, b))

## Zip can unzip a zipped sequence
a, b = zip(*(zip(strings, seq)))
print('Unzip a zip reference with zip function - `a, b = zip(*(zip(strings, seq)))`:', a, b)

## List Comprehensions - [expr for val in collection if condition]
strings = ['foo', 'bar', 'baz', 'f', 'fo', 'b', 'ba']
print("Strings - `strings = ['foo', 'bar', 'baz', 'f', 'fo', 'b', 'ba']`:", strings)

print("List comprehension - `[x.upper() for x in strings if x.startswith('b')]`:", [x.upper() for x in strings if x.startswith('b')])

## List comprehension nested
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('List comprehension nested - `[x for tup in list_of_tuples for x in tup]`:', [x for tup in list_of_tuples for x in tup])

## Dict comprehensions - {index: val for index, val in enumerate(collection) if condition}
strings = ['foo', 'bar', 'baz', 'f', 'fo', 'b', 'ba']
print("Strings - `strings = ['foo', 'bar', 'baz', 'f', 'fo', 'b', 'ba']`:", strings)

print('Dict comprehension - `{index: val for index, val in enumerate(strings) if val.startswith("b")}`:', {index: val for index, val in enumerate(strings) if val.startswith('b')})

## Set comprehensions - {val for val in collection if condition}
print("Set comprehension - `{len(x) for x in strings if x.startswith('b')}`:", {len(x) for x in strings if x.startswith('b')})

## Functions as objects in Python
import re

class TransformUtil:

    @staticmethod
    def remove_punctuation(value):
        """
        Removes !, #, and ?.
        """
        return re.sub('[!#?]', '', value)

    @staticmethod
    def clean_strings(strings, ops):
        """
        General purpose method to clean strings.

        Pass in a sequence of strings and the operations to perform
        """
        result = []
        for string in strings:
            for function in ops:
                string = function(string)
            result.append(string)
        return result


class TestTransformUtil():
    states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']

    expected_output = ['Alabama',
                       'Georgia',
                       'Georgia',
                       'Georgia',
                       'Florida',
                       'South Carolina',
                       'West Virginia']

    def test_remove_punctuation(self):
        assert TransformUtil.remove_punctuation('!#?') == ''

    def test_map_remove_punctuation(self):
        output = map(TransformUtil.remove_punctuation, self.states)
        assert '!#?' not in output

    def test_clean_strings(self):
        clean_ops = [str.strip, TransformUtil.remove_punctuation, str.title]
        output = TransformUtil.clean_strings(self.states, clean_ops)
        assert output == self.expected_output


tester = TestTransformUtil()
tester.test_remove_punctuation()
tester.test_clean_strings()
tester.test_map_remove_punctuation()


## Lambda Functions - anonymous
strings = ['foo', 'bar,', 'baz', 'f', 'fo', 'b', 'ba']
strings.sort(key=lambda x: len(x))
print('Custom Sort with Lambda - `strings.sort(key=lambda x: len(x))`:', strings)

## Closures - dynamically-generated functions returned by another function, with the returned function having access to the local variables of the enclosing function
def make_closure(x):
    def closure():
        print('Secret value is:', x)
    return closure

my_closure = make_closure(7)
my_closure()


def make_watcher():
    dict_seen = {}

    def watcher(x):
        if x in dict_seen:
            return True
        else:
            dict_seen[x] = True
            return False

    return watcher


my_watcher = make_watcher()
seq = [1, 1, 2, 3, 5, 8, 13, 2, 5, 13]
print([my_watcher(x) for x in seq])


## *args & **kwargs - variable-length argument lists
def foo(func, arg, *args, **kwargs):
    print('arg: ', arg)
    print('args: ', args)
    print('kwargs: ', kwargs)

    print('func result: ', func(args))

foo(sum, 'foo', 1, 2, 3, 4, 5)


## Currying - derive new functions from existing ones by partial argument application
def add_numbers(x, y):
    return x + y

add_seven = lambda y: add_numbers(7, y)
print(add_seven(3))

from functools import partial

add_five = partial(add_numbers, 5)
print(add_five(3))

## Generators - functions that yield values one at a time, allowing for lazy evaluation and efficient memory usage
def squares(n = 5):
    print('Calling squares')
    for x in range(1, n + 1):
        yield x ** 2

gen = squares(6)

for x in squares():
    print(x)


## Generator Expressions - similar to list comprehensions but with lazy evaluation
gen = (x ** 2 for x in range(1, 6))

for x in gen:
    print(x)

## itertools - a standard library module that provides functions for creating iterators for efficient looping
import itertools

first_letter = lambda x: x[0]
strings = ['foo', 'bar', 'baz']

for letter, gen_names in itertools.groupby(strings, first_letter):
    print(letter, list(gen_names))


## Notes:
"""
- Tuples are immutable
- Tuples can contain references to mutable objects (references cannot modified by object referenced can be modified)
- Multiplying tuples will only copy references to objects (not the objects themselves)
- Tuple Operations
    - Access element by index - O(1)
- List Operations
    - Access element by index - O(1)
    - Append element at the end - O(1)
    - Insert element at a specific index - O(n)
    - Pop element from a specific index - O(n)
    - Remove element from a specific index - O(n)
    - Check if a list contains value - O(n)
- Dict Operations
    - Access element by index or key - O(1)
    - Insert element by index or key - O(1)
    - Check if a dict contains key - O(1)
    - Delete value from dict - O(1)
    - Remove value from dict - O(1)
    - Pop value from dict - O(1)
    - Get value from dict - O(1)
- Keys of a dict must be hashable so thereby immutable objects like scalars (int, float, string, tuples whose objects are all immutable)
- Set Operations
    - Union (set_1 | set_2)
    - Intersection (set_1 & set_2)
    - Difference (set_1 - set_2) (set_2 - set_1)
    - Symmetric Difference (set_1 ^ set_2)
    - Subset (set_1.issubset(set_2))
    - Superset (set_1.issuperset(set_2))
    - Equality (set_1 == set_2)
- List Comprehensions - [expr for val in collection if condition]
- Dict Comprehensions - {index: val for index, val in enumerate(collection) if condition}
- Set Comprehensions - {expr for val in collection if condition}
"""

