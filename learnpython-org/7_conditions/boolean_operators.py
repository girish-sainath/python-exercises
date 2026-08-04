name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


statement = False
another_statement = True
if statement is True:
    # do something
    print("Statement is True")
    pass
elif another_statement is True: # else if
    print("Another statement is True")
    # do something else
    pass
else:
    print("Another statement is also False")
    # do another thing
    pass


x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


print(not False) # Prints out True
print((not False) == (False)) # Prints out False