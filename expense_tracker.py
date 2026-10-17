


import os
from datetime import datetime

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.txt")
expenses = []


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    amount, category, date = line.strip().split("|")
                    expenses.append({
                        "amount": float(amount),
                        "category": category,
                        "date": date
                    })
                except ValueError:
                    continue

    print(f"Loaded {len(expenses)} expenses.")


def save_expenses():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for expense in expenses:
            file.write(
                f"{expense['amount']}|{expense['category']}|"
                f"{expense['date']}\n"
            )

    print("Saved to:", FILE_NAME)


def add_expense():
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()

        if not category or "|" in category:
            print("Enter a valid category.")
            return

        date = input("Enter date (YYYY-MM-DD): ").strip()
        datetime.strptime(date, "%Y-%m-%d")

        expenses.append({
            "amount": amount,
            "category": category,
            "date": date
        })

        save_expenses()
        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount or date.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\nAmount\tCategory\tDate")
    for expense in expenses:
        print(
            f"{expense['amount']:.2f}\t"
            f"{expense['category']}\t"
            f"{expense['date']}"
        )


def search_expenses():
    choice = input("1. Category  2. Date: ").strip()

    if choice == "1":
        value = input("Enter category: ").strip().lower()
        results = [
            e for e in expenses
            if e["category"].lower() == value
        ]
    elif choice == "2":
        value = input("Enter date (YYYY-MM-DD): ").strip()
        results = [e for e in expenses if e["date"] == value]
    else:
        print("Invalid choice.")
        return

    if results:
        for expense in results:
            print(expense)
    else:
        print("No matching expenses found.")


def show_total():
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: Rs. {total:.2f}")


def main():
    load_expenses()

    while True:
        print("\n--- PERSONAL EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Show Total Spent")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            show_total()
        elif choice == "5":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

def save_expenses():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for expense in expenses:
            file.write(
                f"{expense['amount']}|"
                f"{expense['category']}|"
                f"{expense['date']}\n"
            )
    print("Expenses saved successfully!")
