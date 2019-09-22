"""
Docstring:
This program is to test compound expressions.
"""

# Declaring variables
max_value = 10
min_value = 0

# User input for variable y
y = input("Please enter a number : ")

# If statements to test y
if int(max_value) < int(y):
    print(str(y) + " is above " + str(max_value))
else:
    print(str(y) + " is not above " + str(max_value))

if int(y) < int(min_value):
    print(str(y) + " is below " + str(min_value))
else:
    print(str(y) + " is not below " + str(min_value))

# User input for variable x
x = input("Please enter a second number : ")

# If statements to test x
if int(max_value) > int(x) > int(min_value):
    print(str(x) + " is between " + str(max_value) + " and " + str(min_value))
else:
    print(str(x) + " is not between " + str(max_value) + " and " + str(min_value))

if int(max_value) > int(x) >= int(min_value):
    print(str(x) + " is below " + str(max_value) + " and above or equal to " + str(min_value))
else:
    print(str(x) + " is not between " + str(max_value) + " and above or equal to " + str(min_value))

if int(max_value) >= int(x) > int(min_value):
    print(str(x) + " is below or equal to " + str(max_value) + " and above " + str(min_value))
else:
    print(str(x) + " is not below or equal to " + str(max_value) + " and above " + str(min_value))
