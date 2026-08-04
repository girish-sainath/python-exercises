# List - Relationship Methods

a:set[int] = {10, 20}
b:set[int] = {30, 40, 50, 60}

print('Set A:', a)
print('Set B:', b)

print('A is subset of B `a.issubset(b)`:', a.issubset(b))
print('B is subset of A `b.issubset(a)`:', b.issubset(a))
print('A is superset of B `a.issuperset(b)`:', a.issuperset(b))
print('B is superset of A `b.issuperset(a)`:', b.issuperset(a))
print('A and B are disjoint `a.isdisjoint(b)`:', a.isdisjoint(b))