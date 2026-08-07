single_quoted_string:str = 'This is a single quoted string'
double_quoted_string:str = "This is double quoted string"
multiline_string:str = """
This is a 
multi-line string
"""
print(single_quoted_string)
print(double_quoted_string)
print(multiline_string)

first_name = "John"
last_name = "Wick"
full_name = f" {first_name} {last_name} "

print(f"Concatenation - {first_name} + {last_name} = {first_name + last_name}")
print(f"Repetition - {first_name} * 3 = {first_name * 3}")
print(f"Indexing - {first_name}[0] = {first_name[0]}")
print(f"Slicing - {first_name}[1:3:1] = {first_name[1:3:1]}")
print(f"Upper-Case - {first_name}.upper() = {first_name.upper()}")
print(f"Lower-Case - {first_name}.lower() = {first_name.lower()}")
print(f"Capitalization - {first_name}.title() = {first_name.title()}")
print(f"Capitalization - {first_name}.capitalize() = {first_name.capitalize()}")
print(f"Swap-Case - {first_name}.swapcase() = {first_name.swapcase()}")
print(f"Strip-Whitespace - '{full_name}'.strip() = ~{full_name.strip()}~")
print(f"Strip-Character - '~~~{full_name}~~~'.strip('~') = {('~~~' + full_name + '~~~').strip('~')}")
print(f"Left Strip-Whitespace - '{full_name}'.lstrip() = ~{full_name.lstrip()}~")
print(f"Right Strip-Whitespace - '{full_name}'.rstrip() = ~{full_name.rstrip()}~")
print(f"Split - '{full_name.strip()}'.split(' ') = {full_name.strip().split(' ')}")
print(f"Partition - '{full_name.strip()}'.partition(' ') = {full_name.strip().partition(' ')}")
print(f"Join - '-'.join(['{first_name}', '{last_name}']) = {"-".join(full_name.strip().split(' '))}")
print(f"Replace - '{full_name}'.replace(' ', 'space') = {full_name.replace(' ', 'space')}")

sentence: str = "The quick brown fox jumps over the lazy dog"
print(f"Find - {sentence}.find('quick') = {sentence.find('quick')}")
print(f"(Not Found) Find - {sentence}.find('cat') = {sentence.find('wise')}")
print(f"Right Find - {sentence}.lower().rfind('the') = {sentence.lower().rfind('the')}")
print(f"Index - {sentence}.index('fox') = {sentence.index('fox')}")
try:
    print(f"Index - {sentence}.index('wolf') = {sentence.index('wolf')}")
except ValueError as e:
    print(f"(Not Found) Index - {sentence}.index('wolf') = ValueError: {e}")
print(f"Right Index - {sentence}.lower().index('the') = {sentence.lower().index('the')}")
print(f"In Operator - 'fox' in {sentence} = {"fox" in sentence}")
print(f"In Operator - 'cat' in {sentence} = {"cat" in sentence}")
print(f"Count - {sentence}.count('o') = {sentence.count('o')}")
print(f"Startswith - {sentence}.startswith('The') = {sentence.startswith('The')}")
print(f"Endswith - {sentence}.endswith('dog') = {sentence.endswith('dog')}")

greeting: str = "Hello, {} {}".format('Jason', 'Bourne')
print(f"Formatted Greeting - 'Hello, {{}} {{}}'.format('Jason', 'Bourne') - {greeting}")

palindrome: str = "A man, a plan, a canal, Panama"
trimmed_palindrome = palindrome.lower().replace(' ', '').replace(',', '')
print(f"Original Palindrome - {trimmed_palindrome}")
print(f"Reversed Palindrome - {trimmed_palindrome[::-1]}")
print(f"Is Palindrome - {palindrome} = {trimmed_palindrome == trimmed_palindrome[::-1]}")

words = palindrome.split(' ')
for word in words:
    print(word, end=' ')
print()

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
    print(char, end='')
print()

print(f"Digits - {digits}")
print(f"Alphas - {alphas}")
print(f"Spaces - {spaces}")
print(f"Others - {others}")
