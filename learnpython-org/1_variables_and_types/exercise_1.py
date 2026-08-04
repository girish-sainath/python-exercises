"""
The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
"""

# change this code
"""
my_string = None
my_float = None
my_int = None
"""

my_string = "hello"
my_float = 10.0
my_int = 20

# testing code
if my_string == "hello":
    print("String: %s" % my_string)
if isinstance(my_float, float) and my_float == 10.0:
    print("Float: %f" % my_float)
if isinstance(my_int, int) and my_int == 20:
    print("Integer: %d" % my_int)