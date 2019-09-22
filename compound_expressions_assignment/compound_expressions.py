"""
Docstring:
This program is to test compound expressions.
"""

# Declaring variables
max_value = 10
min_value = 0

# User input for variable y
y = input("Please enter a number : ")

# If statements to test y for max and min values
if int(max_value) < int(y):
    print(str(y) + " is above " + str(max_value))
else:
    print(str(y) + " is below " + str(max_value))

if int(y) < int(min_value):
    print(str(y) + " is below " + str(min_value))
else:
    print(str(y) + " is above " + str(min_value))

# User input for variable x
x = input("Please enter a second number : ")

