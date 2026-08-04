# Create Lists

empty:list[str] = []

vowels:list[str] = ['a', 'e', 'i', 'o', 'u']
print('Vowels `vowels`:', vowels)
print('Type `type(vowels)`:', type(vowels))
print('Length `len(vowels)`:', len(vowels))

mixed:list = ['a', 1, True, 3.14, None]
print('Mixed `mixed`:', mixed)
print('Type `type(mixed)`:', type(mixed))
print('Length `len(mixed)`:', len(mixed))

letters:str = 'Python'
print('Letters `letters`:', letters)

letters_list:list[str] = list(letters)
print('Letters List `list(letters)`:', letters_list)

numbers:list[int] = list(range(5))
print('Numbers `numbers`:', numbers)
print('Type: `type(numbers)`:', type(numbers))
print('Length `len(numbers)`:', len(numbers))
