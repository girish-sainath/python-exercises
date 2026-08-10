# Lists

## List Basics
empty_list: list[str] = []

vowels: list[str] = ["a", "e", "i", "o", "u"]
print(f"Vowels - 'vowels' = {vowels}")
print(f"Type Vowels - 'type({vowels})' = {type(vowels)}")
print(f"Length Vowels - 'len({vowels})' = {len(vowels)}")
print()

mixed: list[any] = ["a", 1, True, 3.1416, None]
print(f"Mixed - 'mixed' = {mixed}")
print(f"Type Mixed - 'type({mixed})' = {type(mixed)}")
print(f"Length Mixed - 'len({mixed})' = {len(mixed)}")
print()

letters: str = "python"
print(f"Letters - 'letters' = {letters}")

letters_list: list[str] = list(letters)
print(f"Letters List - 'letters_list' = {letters_list}")
print(f"Type Letters List - 'type({letters_list})' = {type(letters_list)}")
print(f"Length Letters List - 'len({letters_list})' = {len(letters_list)}")
print()

fibo_numbers: list[int] = [0, 1, 1, 2, 3, 5, 8]
print(f"Fibo Numbers - 'fibo_numbers' = {fibo_numbers}")
print(f"Type Fibo Numbers - 'type({fibo_numbers})' = {type(fibo_numbers)}")
print(f"Length Fibo Numbers - 'len({fibo_numbers})' = {len(fibo_numbers)}")
print()


## Matrix (Nested Lists)
matrix: list[list[str]] = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
]
print(f"Matrix - 'matrix' = {matrix}")
print(f"Type Matrix - 'type({matrix})' = {type(matrix)}")
print(f"Length Matrix - 'len({matrix})' = {len(matrix)}")
print()

mixed_matrix: list[list[any]] = [
    ["a", 1, True],
    [3.1416, None, "x"],
    ["y", "z", 31],
]
print(f"Mixed Matrix - 'mixed_matrix' = {mixed_matrix}")
print(f"Type Mixed Matrix - 'type({mixed_matrix})' = {type(mixed_matrix)}")
print(f"Length Mixed Matrix - 'len({mixed_matrix})' = {len(mixed_matrix)}")
print()


## List - Indexing and Slicing
vowels: list[str] = ["a", "e", "i", "o", "u"]
print(f"Vowels - vowels = {vowels}")
print(f"First Vowel - '{vowels}[0]' = {vowels[0]}")
print(f"Second Vowel - '{vowels}[1]' = {vowels[1]}")
print(f"Last Vowel - '{vowels}[-1]' = {vowels[-1]}")
print(f"Penultimate Vowel - '{vowels}[-2]' = {vowels[-2]}")
print(f"All Vowels - '{vowels[::1]}' = {vowels[::1]}")
print(f"Reversed Vowels - '{vowels[::-1]}' = {vowels[::-1]}")
print(f"First 3 Vowels - '{vowels[:3]}' = {vowels[:3]}")
print(f"Second to all Vowels - '{vowels}[2:]' = {vowels[2:]}")
print(f"In-between Vowels - '{vowels}[1:4]' = {vowels[1:4]}")
print(f"Alternate Vowels - '{vowels}[::2]' = {vowels[::2]}")
print()


## Nested List - Indexing and Slicing
matrix: list[list[str]] = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
]

print(f"Matrix - 'matrix' = {matrix}")
print(f"First Row - '{matrix}[0]' = {matrix[0]}")
print(f"Second Row - '{matrix}[1]' = {matrix[1]}")
print(f"Third Row - '{matrix}[2]' = {matrix[2]}")

print(f"First Element in First Row - '{matrix}[0][0]' = {matrix[0][0]}")
print(f"Last Element in Last Row - '{matrix}[-1][-1]' = {matrix[-1][-1]}")
print(f"Second Element in Second Row - '{matrix}[1][1]' = {matrix[1][1]}")
print(f"First 2 Rows - '{matrix}[:2]' = {matrix[:2]}")
print(f"Last 2 Rows - '{matrix}[1:]' = {matrix[1:]}")
print(f"First Two Elements in Last Row - '{matrix}[2][:2]' = {matrix[2][:2]}")

print("Matrix:")
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()
print()


## List - Unpacking
profile: list[any] = ["Jason", "Bourne", 36, "Special-Agent", "USA"]
print(f"Profile - 'profile' = {profile}")

### Default unpacking
first_name, last_name, age, role, country = profile
print(f"Unpacking - 'first_name, last_name, age, role, country = profile' = {first_name, last_name, age, role, country}")

### Unpacking with * operator
first_name, last_name, *details, country = profile
print(f"Unpacking - 'first_name, last_name, *details, country = profile' = {first_name, last_name, details, country}")

### Unpacking with _ placeholder
first_name, last_name, _, role, _ = profile
print(f"Unpacking - 'first_name, last_name, _, role, _ = profile' = {first_name, last_name, role}")

### Unpacking with * operator and _ placeholder
first_name, last_name, *_, country = profile
print(f"Unpacking - 'first_name, last_name, *_, country = profile' = {first_name, last_name, country}")

### Unpacking with _ placeholder and * operator for string
vowels: str = "AEIOU"
a, _, *rest = vowels
print(f"Unpacking - 'a, _, *rest = vowels' = {a, rest}")
print()


## List - Explore and Analyze
### Analyze
fibo_numbers: list[int] = [0, 1, 1, 2, 3, 5, 8]

print(f"Fibo Numbers - 'fibo_numbers' = {fibo_numbers}")
print(f"Type Fibo Numbers - 'type({fibo_numbers})' = {type(fibo_numbers)}")
print(f"Length Fibo Numbers - 'len({fibo_numbers})' = {len(fibo_numbers)}")
print(f"Max Fibo Number - 'max({fibo_numbers})' = {max(fibo_numbers)}")
print(f"Min Fibo Number - 'min({fibo_numbers})' = {min(fibo_numbers)}")
print(f"Sum of Fibo Numbers - 'sum({fibo_numbers})' = {sum(fibo_numbers)}")
print(f"Average of Fibo Numbers - 'sum({fibo_numbers}) / len({fibo_numbers})' = {sum(fibo_numbers) / len(fibo_numbers)}")
print(f"Reversed Fibo Numbers - 'list(reversed({fibo_numbers}))' = {list(reversed(fibo_numbers))}")
print(f"Sort Reversed Fibo Numbers - 'list(sorted({list(reversed(fibo_numbers))}))' = {list(sorted(reversed(fibo_numbers)))}")
print()

### Completeness and Existence Check
print(f"All Numbers - 'all({fibo_numbers})' = {all(fibo_numbers)}")
print(f"Any Numbers - 'any({fibo_numbers})' = {any(fibo_numbers)}")
print()

### Search and Count
print(f"Count of 1 - '{fibo_numbers}.count(1)' = {fibo_numbers.count(1)}")
print(f"Index of 3 - '{fibo_numbers}.index(3)' = {fibo_numbers.index(3)}")
try:
    print(f"Index of 13 - '{fibo_numbers}.index(13)' = {fibo_numbers.index(13)}")
except ValueError as e:
        print(f"Not-Found-Index - Index of 13 - '{fibo_numbers}.index(13)' = ValueError: {e}")
print()

### Reference vs Value
evens: list[int] = [2, 4, 6]
evens_again: list[int] = [2, 4, 6]
print(f"Equals check - '{evens} == {evens_again}' = {evens == evens_again}")
print(f"Is check - '{evens} is {evens_again}' = {evens is evens_again}")

odds: list[int] = [1, 3, 5]
print(f"Evens > Odds - {evens} > {odds} = {evens > odds}")
print()

## Append and Insert

