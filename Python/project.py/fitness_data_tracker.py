import matplotlib.pyplot as plt

steps = []
calories = []

GOAL = 10000

def average():
    return sum(steps) / len(steps)

def total():
    return sum(calories)

def best_day():
    index = steps.index(max(steps))
    return index + 1

def bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(value):
    if value < 18.5:
        return "Underweight"
    elif value < 25:
        return "Normal"
    elif value < 30:
        return "Overweight"
    else:
        return "Obese"

def summary():
    if len(steps) == 0:
        print("No records available.")
        return

    goal_days = sum(1 for s in steps if s >= GOAL)

    print("\n--- Weekly Summary ---")
    print(f"Average steps: {average():.2f}")
    print(f"Total calories: {total()}")
    print(f"Best day: Day {best_day()} ({max(steps)} steps)")
    print(f"Goal days: {goal_days}/{len(steps)}")

def calculate_bmi():
    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if weight <= 0 or height <= 0:
            print("Invalid weight or height.")
            return

        value = bmi(weight, height)
        print(f"BMI: {value:.2f}")
        print("Category:", bmi_category(value))

    except ValueError:
        print("Please enter valid numbers.")

def show_chart():
    if len(steps) == 0:
        print("No records available.")
        return

    days = [f"Day {i+1}" for i in range(len(steps))]

    plt.bar(days, steps)
    plt.axhline(y=GOAL, linestyle="--", label="10000 Step Goal")
    plt.title("Daily Steps")
    plt.xlabel("Days")
    plt.ylabel("Number of Steps")
    plt.legend()
    plt.show()

while True:
    print("\n===== FITNESS DATA TRACKER =====")
    print("1. Add Record")
    print("2. Weekly Summary")
    print("3. Calculate BMI")
    print("4. Show Bar Chart")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            s = int(input("Enter steps: "))
            c = int(input("Enter calories burned: "))

            if s < 0:
                print("Invalid steps. Enter a non-negative whole number.")
                print("Record not saved.")
            elif c < 0:
                print("Invalid calories. Enter a non-negative whole number.")
                print("Record not saved.")
            else:
                steps.append(s)
                calories.append(c)
                day = len(steps)
                achieved = "Yes" if s >= GOAL else "No"
                percentage = (s / GOAL) * 100

                print(f"Record saved for Day {day}. Goal achieved: {achieved}")
                print(f"({percentage:.2f}% of goal)")

        except ValueError:
            print("Invalid input. Enter whole numbers.")

    elif choice == "2":
        summary()

    elif choice == "3":
        calculate_bmi()

    elif choice == "4":
        show_chart()

    elif choice == "5":
        print("Thank you for using Fitness Data Tracker!")
        break

    else:
        print("Invalid menu option. Try again.")