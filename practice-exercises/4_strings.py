single_quoted_string:str = 'This is a single quoted string'
double_quoted_string:str = "This is double quoted string"
multiline_string:str = """
This is a 
multi-line string
"""
print(single_quoted_string)
print(double_quoted_string)
print(multiline_string)

first_name: str = "jaSon"
last_name: str = "boUrne"
full_name: str = f"  {first_name} {last_name}  "

print(f"Concatenation - '{first_name}' + '{last_name}' = '{first_name + last_name}'")
print(f"Repetition - '{first_name}' * 3 = '{first_name * 3}'")
print(f"Indexing - '{first_name}'[0] = '{first_name[0]}'")
print(f"Slicing - '{first_name}'[1:4:1] = '{first_name[1:4:1]}'")
print(f"Strip-Character - '~~{full_name.strip()}~~'.strip('~~') = '{("~~" + full_name.strip() + "~~").strip("~~")}'")
print(f"Left-Strip-Character - '~~{full_name.strip()}~~'.lstrip('~~') = '{("~~" + full_name.strip() + "~~").lstrip("~~")}'")
print(f"Right-Strip-Character - '~~{full_name.strip()}~~'.rstrip('~~') = '{("~~" + full_name.strip() + "~~").rstrip("~~")}'")
print(f"Strip-Whitespace - '{full_name}'.strip() = '{full_name.strip()}'")
print(f"Left-Strip-Whitespace - '{full_name}'.lstrip() = '{full_name.lstrip()}'")
print(f"Right-Strip-Whitespace - '{full_name}'.rstrip() = '{full_name.rstrip()}'")
print(f"Title - '{full_name.strip()}'.title() = '{full_name.strip().title()}'")
print(f"Capitalize - '{full_name.strip()}'.capitalize() = '{full_name.strip().capitalize()}'")
print(f"Lower-Case - '{full_name.strip()}'.lower() = '{full_name.strip().lower()}'")
print(f"Upper-Case - '{full_name.strip()}'.upper() = '{full_name.strip().upper()}'")
print(f"Swap-Case - '{full_name.strip()}'.swapcase() = '{full_name.strip().swapcase()}'")
print(f"Split - '{full_name.strip()}'.split(' ') = '{full_name.strip().split(" ")}'")
print(f"Partition - '{full_name.strip()}'.partition(' ') = '{full_name.strip().partition(" ")}'")
print(f"Join - '-'.join(['{first_name}', '{last_name}']) = '{"-".join([first_name, last_name])}'")
print(f"Replace - '{full_name.strip()}'.replace(' ', 'space') = '{full_name.strip().replace(" ", "space")}'")

print()
sentence: str = "The quick brown fox jumps over the lazy dog"
print(f"Find - '{sentence}'.find('quick') = {sentence.find("quick")}")
print(f"Not-Found-Find - '{sentence}''.find('cat') = {sentence.find("cat")}")
print(f"Find - '{sentence.lower()}'.find('the') = {sentence.lower().find("the")}")
print(f"Right-Find - '{sentence.lower()}'.rfind('the') = {sentence.lower().rfind("the")}")
print(f"Index - '{sentence}'.index('quick') = {sentence.index("quick")}")
print(f"Index - '{sentence}'.index('the') = {sentence.index("the")}")
try:
    print(f"Not-Found-Index - '{sentence}''.index('cat') = {sentence.index("cat")}")
except ValueError as e:
    print(f"Not-Found-Index - {sentence}.index('cat') = ValueError: {e}")
print(f"Right-Index - '{sentence.lower()}'.rindex('the') = {sentence.lower().rindex("the")}")
print(f"Count - '{sentence.lower()}'.count('o') = {sentence.lower().count("o")}")
print(f"Startswith - '{sentence.lower()}'.startswith('the') = {sentence.lower().startswith("the")}")
print(f"Not-Startswith - '{sentence.lower()}'.startswith('some') = {sentence.lower().startswith("some")}")
print(f"Endswith - '{sentence.lower()}'.endswith('dog') = {sentence.lower().endswith("dog")}")
print(f"Not-Endswith - '{sentence.lower()}'.endswith('cat') = {sentence.lower().endswith("cat")}")
print(f"In-Operator - 'fox' in '{sentence.lower()}' = {"fox" in sentence.lower()}")
print(f"Not-Found-In-Operator - 'cat' not in '{sentence.lower()}' = {"cat" not in sentence.lower()}")

print()
print(f"Formatted Greeting - 'Hello, {{}} {{}} !!'.format('{first_name.title()}', '{last_name.title()}') - {"Hello, {} {}".format(first_name.title(), last_name.title())} !!")

print()
palindrome: str = "A man, a plan, a canal, Panama"
trimmed_palindrome: str = palindrome.lower().replace(' ', '').replace(',', '')
reversed_palindrome: str = trimmed_palindrome[::-1]
print(f"Palindrome = '{palindrome}'")
print(f"Original-Palindrome = '{trimmed_palindrome}'")
print(f"Reversed-Palindrome = '{reversed_palindrome}'")
print(f"Is Palindrome - '{trimmed_palindrome}' == '{reversed_palindrome}' = {trimmed_palindrome == reversed_palindrome}")

print()
words: list[str] = palindrome.split(' ')
print(f"Split-and-Print - '{palindrome}'.split(' ') = ", end=' ')
for word in words:
    print(word, end=' ')

digits: list[str] = []
alphas: list[str] = []
others: list[str] = []
spaces: int = 0

for char in palindrome:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        alphas.append(char)
    elif char.isspace():
        spaces += 1
    else:
        others.append(char)

print()
print(f"Digits = {digits}")
print(f"Alphas = {alphas}")
print(f"Spaces = {spaces}")
print(f"Others = {others}")
