# Set Methods

a:set[int] = {10, 40, 30, 20}
print('Set:', a)
a.add(50)
print('Add `a.add(50)`:', a)
a.add(30)
print('Add `a.add(30)`:', a)
a.remove(20)
print('Remove `a.remove(20)`:', a)
a.discard(30)
print('Discard `a.discard(30)`:', a)

a.update('Hi')
print('Update `a.update("Hi")`:', a)
a.update([60, 70])
print('Update `a.update([60, 70])`:', a)

a |= {6, 34}
print('Union Update `a |= {1, 3}`:', a)

a.remove(34)
print('Remove `a.remove(34)`:', a)
try:
    a.remove(100)
except KeyError as e:
    print('Remove non-existing element `a.remove(100)`:', e)
a.discard(100)
print('Discard non-existing element `a.discard(100)`:', a)

a.pop()
print('Pop `a.pop()`:', a)