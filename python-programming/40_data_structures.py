# Data Structures - Ordered, Duplicates, Indexed, Mutable

## Lists
my_list:list[int] = [10, 30, 10, 20]
print('List:', my_list)
print('Lists are "Ordered" `my_list = [10, 30, 10, 20]`:', my_list)
print('Lists allow "Duplicates" `my_list = [10, 30, 10, 20]`:', my_list)
print('Lists are "Indexed" `my_list[0]`:', my_list[2])
my_list[3] = 40
print('Lists are "Mutable" `my_list[3] = 40` :', my_list)

## Tuples
my_tuple:tuple = (10, 30, 10, 20)
print('Tuple:', my_tuple)
print('Tuples are "Ordered" `my_tuple = (10, 30, 10, 20)`:', my_tuple)
print('Tuples allow "Duplicates" `my_tuple = (10, 30, 10, 20)`:', my_tuple)
print('Tuples are "Indexed" `my_tuple[0]`:', my_tuple[2])
try:
    my_tuple[3] = 40
except TypeError as e:
    print('Tuples are "Immutable" `my_tuple[3] = 40` :', e)
try:
    my_tuple.remove(10)
except AttributeError as e:
    print('Tuples are "Immutable" so it do not have "remove" method `my_tuple.remove(10)` :', e)
try:
    my_tuple.pop(0)
except AttributeError as e:
    print('Tuples are "Immutable" so it do not have "pop" method `my_tuple.pop(0)` :', e)
print('Sorting a Tuple gives a List `type(sorted(my_tuple))`:', type(sorted(my_tuple)))

## Sets
my_set:set[int] = {10, 50, 30, 10, 20}
print('Set:', my_set)
print('Sets are "Unordered" `my_set = {10, 30, 10, 20}`:', my_set)
print('Sets do not allow "Duplicates" `my_set = {10, 30, 10, 20}`:', my_set)
my_set.add(40)
print('Sets are "Mutable" `my_set.add(40)` :', my_set)
my_set.remove(10)
print('Sets are "Mutable" `my_set.remove(10)` :', my_set)
try:
    print('Sets are "Unindexed" `my_set[0]`:', my_set[0])
except TypeError as e:
    print('Sets are "Unindexed" `my_set[0]`:', e)