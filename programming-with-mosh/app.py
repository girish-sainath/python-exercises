# print('Patient Check In:')
#
# print('\nPatient 1 Data: ')
# first_name = 'Jason'
# last_name = 'Smith'
# age = 20
# new_patient = True
# print('Name: ' + first_name + ' ' + last_name)
# print('Age: ' + str(age))
# print('New Patient: ' + str(new_patient))
#
# print('\nPatient 2 Data: ')
# first_name = 'John'
# last_name = 'Smith'
# age = 27
# new_patient = True
# print('Name: ' + first_name + ' ' + last_name)
# print('Age: ' + str(age))
# print('New Patient: ' + str(new_patient))
#
# print('\nPatient 3 Data: ')
# first_name = 'Joaquin'
# last_name = 'Smith'
# age = 56
# new_patient = True
# print('Name: ' + first_name + ' ' + last_name)
# print('Age: ' + str(age))
# print('New Patient: ' + str(new_patient))

# input('\nPress Enter to continue...\n')
#
# input_name = input('Enter your name? ')
# print('Hello ' + input_name)
#
# birth_year = input('Enter your birth year? ')
# curr_age = 2025 - int(birth_year)
# print('You are either ' + str(curr_age) + ' or ' + str(curr_age - 1) + ' years old')
# print(str(float(birth_year)))

# first = float(input('First Number: '))
# second = float(input('Second Number: '))
#
# print('Sum Value = ' + str(first + second))

# course = 'Python for Beginners'
# print('statement => output')
# print('course.upper() => ' + course.upper())
# print('course.lower() => ' + course.lower())
# print('course.find(\'Beginners\') => ' + str(course.find('Beginners')))
# print('course.index(\'Beginners\') => ' + str(course.index('Beginners')))
# print('\'Python\' in course => ' + str('Python' in course))
# print('course.replace(\'for\', \'4\') => ' + course.replace('for', '4'))
# print('course => '+ course)
#
    # print(10 ** 3)
#
# x = 10
# x = x + 3
# x += 3
# x -= 3
# x = x - 3
# print(x)

# x = 3 == 4
# print(x)

# price = 25
# print(price > 10 and price < 30)
# print(10 < price < 30)
# print(price > 10 or price < 20)
# print(not price < 10)

# temperature = 15
#
# if temperature > 30:
#     print('It\'s a hot day')
#     print('Drink a lot of water')
# elif temperature > 20:
#     print('It\'s a nice day')
# elif temperature > 10:
#     print('It\'s a bit cold')
# else:
#     print('It\'s a cold day')
# print('Done with the weather stuff')

# weight = float(input('Weight: '))
# unit = input('(K)g or (L)bs: ')
# unit = unit.lower()
# if unit == 'k':
#     print('Weight in Lbs: ' + str(weight / 0.45))
# else:
#     print('Weight in Kgs: ' + str(weight * 0.45))

# i = 0
# while i < 10:
#     print(i * '*')
#     i += 1

# names = ['John', 'Bob', 'Mosh', 'Sam', 'Mary']
# print(names)
# print(len(names))
# print(names[0])
# print(names[-5])
# names[0] = 'Jon'
# print(names)
# print(names[0:3])
# print(names)

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers.append(6)
# print(numbers)
# numbers.insert( 0, 0)
# print(numbers)
# numbers.insert(0, -1)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# print(1 in numbers)
# print(9 in numbers)
# print(len(numbers))
# numbers.clear()
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# for item in numbers:
#     print(item)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# numbers = range(5)
# print(numbers)
# for item in numbers:
#     print(item)
#
# numbers = range(5, 10)
# print(numbers)
# for item in numbers:
#     print(item)
#
# numbers = range(5, 10, 2)
# print(numbers)
# for item in numbers:
#     print(item)
#
# for item in range(5):
#     print(item)


# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(numbers)
# print(numbers.count(5))
# print(numbers.index(3))

# def greeting():
#     print('Hi there!')
#     print('How are you?')
#     print('Welcome aboard')
#
# greeting()

# def greeting(first_name, last_name):
#     print(f'Hello, {first_name} {last_name}!')
#     print('Welcome aboard')
#
# greeting('Jim', 'Lee')

# def get_greeting(first_name, last_name):
#     return f'Hello, {first_name} {last_name}!'
#
# print(get_greeting('Jim', 'Lee'))

# def get_greeting(first_name, last_name):
#     return f"Hello {first_name} {last_name}!"

# message = get_greeting("John", "Smith")
# file = open('content.txt', 'w')
# file.write(message)
# file.close()

# def increment(number, by):
#     return number + by
#
# print(increment(number=2, by=1))

# def increment(number, by=1):
#     return number + by
#
# print(increment(2))
# print(increment(2, 5))

# def add(*numbers):
#     return sum(numbers)
#
# print(add(1, 2, 3))

# def multiply(*numbers):
#     value = 1
#     for number in numbers:
#         value *= number
#     return value
#
# print(multiply(2, 3, 4, 5))

# def save_user(**user):
#     print(user)
#
# save_user(id=1, first_name="John", last_name="Smith", age=22)

# def save_user(**user):
#     print(user['first_name'], user['last_name'])
#
# save_user(id=1, first_name="John", last_name="Smith", age=22)

# message = 'a'
#
# def global_modifier(mess):
#     mess = 'b'
#
# global_modifier(message)
# print(message)

# def fizz_buzz(input_number):
#     if input_number % 3 == 0 and input_number % 5 == 0:
#         return "FizzBuzz"
#     elif input_number % 3 == 0:
#         return "Fizz"
#     elif input_number % 5 == 0:
#         return "Buzz"
#     else:
#         return input_number
#
# print(fizz_buzz(7))

# f = open('text.txt', 'r')
# text = f.read()
# f.close()
#
# print(text)

with open('text.txt', 'r') as f:
    text = f.read()
    print(text)

from pathlib import Path
print(Path.cwd())