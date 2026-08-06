number: int = 5
string: str = "Hello World!"
pi: float = 3.1416
boolean: bool = True
letters: list[str] = ["a", "b", "c"]
numbers: list[int] = [1, 2, 3]
intro: tuple[str, str, str] = ("Jason", "Bourne", "American")
vowels: set[str] = {"a", "e", "i", "o", "u"}
even_numbers: frozenset[int] = frozenset({2, 4, 6})
profile: dict[str, str] = {"first_name": "Jason", "last_name": "Bourne", "country": "USA"}
my_bytes: bytes = b"Hello"


print(number, type(number))
print(string, type(string))
print(pi, type(pi))
print(boolean, type(boolean))
print(letters, type(letters))
print(numbers, type(numbers))
print(intro, type(intro))
print(vowels, type(vowels))
print(even_numbers, type(even_numbers))
print(profile, type(profile))
print(my_bytes, type(my_bytes))
