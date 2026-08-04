# Lambda

multiply = lambda x: x * 2
print('Multiple `multiply = lambda x: x * 2 && multiple(5.6)`:',multiply(5.6))

add = lambda x, y: x + y
print('Add `add = lambda x, y: x + y && add(5, 6)`:', add(5, 6))

sub = lambda x, y, z: x - y - z
print('Subtract `sub = lambda x, y, z: x - y - z && sub(10, 5, 2)`:', sub(10, 5, 2))

check = lambda i: i in "python"
print('Check for character `check = lambda i: i in "python" && check("o")`:', check('o'))

prices:list[str] = ['$5.99', '$12.49', '$3.50', '$8.75']

print('Floated Price Map Lambda `list(map(lambda price: float(price.replace("$", "")), prices))`:'
      , list(map(lambda price: float(price.replace('$', '')), prices)))

print('Floated Prices List Comprehension `[float(price.replace("$", "")) for price in prices]`:'
      , [float(price.replace('$', '')) for price in prices])


prices:list[int] = [120, 30, 300, 80]
print('Prices List:', prices)
print('Filtered Lambda `list(filter(lambda price: price >= 100, prices))`:'
      , list(filter(lambda price: price >= 100, prices)))

students:list[list] = [['Andrew', 85], ['Alice', 92], ['Bob', 78], ['Andy', 95]]
print('Students List:', students)
print('Students Above 80 `list(filter(lambda row: row[1] >= 80, students))`:'
      , list(filter(lambda row: row[1] >= 80, students)))
print('Students starting with "A" `list(filter(lambda row: row[0].startswith("A")))`'
      , list(filter(lambda row: row[0].startswith('A'), students)))
