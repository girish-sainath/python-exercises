# List - Filter

letters: list = ['a', '', 'b', None, 'c', False, 'd']

print('Filtered Letters `list(filter(None, letters))`:',list(filter(None, letters)))

print('True Letters `list(filter(bool, letters))`:',list(filter(bool, letters)))


items: list = ['sql', '123', 'python', '456', 'java', '789']

print('Alphabetical Items `list(filter(bool, letters))`:',list(filter(str.isalpha, items)))

