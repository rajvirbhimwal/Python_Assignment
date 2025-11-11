# ===============================================
# Project: Daily Calorie Tracker
# Author: Rajvir Bhimwal
# Date: 2025-11-10
# ===============================================

# ---------- Task 1: Setup & Introduction ----------
print("      Welcome to the Daily Calorie Tracker  ")
print("===============================================")
print("This tool helps you log your meals, calculate your total")
print("and average calorie intake, compare it with your daily limit,")
print("and optionally save your report for future tracking.\n")

# ---------- Task 2: Input & Data Collection ----------
meal_names = []
meal_calories = []
num_meals = int(input("How many meals do you want to log today? "))

for i in range(num_meals):
    print(f"\nEnter details for Meal #{i+1}:")
    meal = input("Meal name: ")
    calories = float(input("Calories consumed: "))
    meal_names.append(meal)
    meal_calories.append(calories)

# ---------- Task 3: Calculations ----------
total_calories = sum(meal_calories)
average_calories = total_calories / num_meals

daily_limit = float(input("\nEnter your daily calorie limit: "))

# ---------- Task 4: Limit Comparison ----------
if total_calories > daily_limit:
    limit_status = " You have exceeded your daily limit!"
else:
    limit_status = " Great! You're within your daily limit."

# ---------- Task 5: Output Summary Report ----------
print("\n===============================================")
print("            Daily Calorie Summary")
print("===============================================")
print(f"{'Meal Name':<15}{'Calories':>10}")
print("-----------------------------------------------")

for i in range(len(meal_names)):
    print(f"{meal_names[i]:<15}{meal_calories[i]:>10.2f}")

print("-----------------------------------------------")
print(f"{'Total:':<15}{total_calories:>10.2f}")
print(f"{'Average:':<15}{average_calories:>10.2f}")
print("-----------------------------------------------")
print(limit_status)
print("===============================================\n")
# ---------- Task 6: Optional File Saving ----------
save_choice = input("Would you like to save this session to a file? (yes/no): ").strip().lower()

if save_choice in ["yes", "y"]:
    filename = "calorie_log.txt"


    report = "===============================================\n"
    report += "           Daily Calorie Summary\n"
    report += "-----------------------------------------------\n"
    report += "Meal Name         Calories\n"
    report += "-----------------------------------------------\n"

    for i in range(len(meal_names)):
        report += f"{meal_names[i]:<15}{meal_calories[i]:>10.2f}\n"

    report += "-----------------------------------------------\n"
    report += f"Total:             {total_calories:>10.2f}\n"
    report += f"Average:           {average_calories:>10.2f}\n"
    report += "-----------------------------------------------\n"
    report += f"{limit_status}\n"
    report += "===============================================\n\n"

    with open(filename, "a") as file:
        file.write(report)

    print(f" Session saved successfully to '{filename}'.")
else:
    print(" Session not saved. Goodbye and stay healthy!")

print("\nThank you for using the Daily Calorie Tracker! ")
