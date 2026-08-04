data = ("John", "Doe", 53.44)

# write your code here
"""
format_string = "Hello"
"""

format_string = "Hello %s %s. Your current balance is $%.2f."
print(format_string % data)

format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)