"""
Docstring:
This program is to test compound expressions.
"""

# Declaring variables
max_value = 10
min_value = 0

# User input for variable y
y = input("Please enter a number above " + str(max_value) + " or below " + str(min_value) + ":")

# If statement to test y for max and min values
if int(max_value) < int(y) < int(min_value):
    print("Sorry, " + str(y) + " is between " + str(max_value) + " and " + str(min_value) + ".")
else:
    print("Excellent, " + str(y) + " is not between " + str(max_value) + " and " + str(min_value) + ".")

# User input for variable x
# x = input()