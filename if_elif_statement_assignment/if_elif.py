"""Docstring
This program is for basic if / elif / else statements - it stores variables for subscription costs, takes input for
which subscription level the user would like to select, and prints out their cost."""

# Variables for what the costs are
platinum_cost = 60
gold_cost = 50
silver_cost = 40
bronze_cost = 30
trial_cost = 0

# Print statements for subscriptions and costs
print("Welcome to the Programmer's Toolkit Subscription, the subscription levels are as follows:")
print("Platinum = $" + str(platinum_cost) + ", Gold = $" + str(gold_cost) + ", Silver = $" + str(gold_cost) + ", Bronze = $" + str(bronze_cost) + ", Trial = $" + str(trial_cost) + ".")

# User input for which subscription level they would like
subscription_level = input("Please select which level you would like to subscribe to: ")

# If statement to print out what level they chose and the cost
if subscription_level == "Platinum" or "platinum":
    print("Congratulations, you have signed up for the Platinum subscription. Your cost today is $" + platinum_cost + ".")
elif subscription_level == "Gold" or "gold":
    print("Congratulations, you have signed up for the Gold subscription. Your cost today is $" + gold_cost + ".")
elif subscription_level == "Silver" or "silver":
    print("Congratulations, you have signed up for the Silver subscription. Your cost today is $" + silver_cost + ".")
elif subscription_level == "Bronze" or "bronze":
    print("Congratulations, you have signed up for the Bronze subscription. Your cost today is $" + bronze_cost + ".")
elif subscription_level == "Trial" or "bronze":
    print("Congratulations, you have signed up for the free trial. Your cost today is $" + trial_cost + ".")
else:
    # Error handling
    print("Invalid input, please try again.")