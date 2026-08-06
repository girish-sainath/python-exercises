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

print(f"Concatenation John + Wick = {first_name + last_name}")
print(f"Repetition John * 3 = {first_name * 3}")
print(f"Indexing John[0] = {first_name[0]}")
print(f"Slicing John[1:3:1] = {first_name[1:3:1]}")
print(f"Upper-Case John.upper() = {first_name.upper()}")
print(f"Lower-Case John.lower() = {first_name.lower()}")
print(f"Capitalization John.title() = {first_name.title()}")
print(f"Capitalization John.capitalize() = {first_name.capitalize()}")
print(f"Swap-Case John.swapcase() = {first_name.swapcase()}")
print(f"Strip-Whitespace ' John Wick '.strip() = ~{full_name.strip()}~")
print(f"Left Strip-Whitespace ' John Wick '.strip() = ~{full_name.lstrip()}~")
print(f"Right Strip-Whitespace ' John Wick '.strip() = ~{full_name.rstrip()}~")
print(f"Split 'John Wick'.split(' ') = {full_name.strip().split(' ')}")
print(f"Partition 'John Wick'.partition(' ') = {full_name.strip().partition(' ')}")
print(f"Join ['John', '-'.join(['John', 'Wick']) = {"-".join(full_name.strip().split(' '))}")
print(f"Replace ' John Wick '.replace(' ', 'space') = {full_name.replace(' ', 'space')}")
