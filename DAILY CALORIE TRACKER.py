# Name : Raman Raj Shrivastava
# Roll No.:- 2501010021
# Date: 25 October 2025
# Project: Daily Calorie Tracker
# Task 1: Setup & Introduction
print("=========================================")
print("     Welcome to the Daily Calorie Tracker")
print("=========================================")
print("This tool helps you record your daily meals and track your total calorie intake.")
print("You can compare it with your daily calorie limit and see if you’re on track!\n")

# Task 2: Input & Data Collection
meal_names = []
calorie_amounts = []

num_meals = int(input("How many meals did you have today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name (e.g., Breakfast): ")
    calories = float(input("Enter calorie amount (e.g., 350): "))

    meal_names.append(meal)
    calorie_amounts.append(calories)

# Task 3: Calorie Calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / len(calorie_amounts)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    print("\n WARNING: You have exceeded your daily calorie limit!")
else:
    print("\n Great job! You are within your daily calorie limit.")

# Task 5: Neatly Formatted Output
print("\n=========================================")
print("         DAILY CALORIE SUMMARY")
print("=========================================")
print(f"{'Meal Name':<20}{'Calories'}")
print("-----------------------------------------")

for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal:<20}{cal}")

print("-----------------------------------------")
print(f"{'Total:':<20}{total_calories}")
print(f"{'Average:':<20}{average_calories:.2f}")
print("=========================================")