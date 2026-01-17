import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Rent): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully\n")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\nDate | Category | Amount | Note")
            print("-" * 40)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No expenses found\n")

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].startswith(month):
                    total += float(row[2])

        print(f"💰 Total expense for {month}: ₹{total}")
    except FileNotFoundError:
        print("No data available\n")

def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")

menu()
