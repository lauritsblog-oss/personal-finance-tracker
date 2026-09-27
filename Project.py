import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FINANCE_FILE = os.path.join(BASE_DIR, "finance.json")

##### Personel Finance Tracker #####
def display_menu():
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Expenses")
    print("4. View income")
    print("5. Statistics")
    print("6. Delete Expense")
    print("7. Delete Income")
    print("8. Exit")

def save_data(personel_finance):
    with open(FINANCE_FILE, "w") as file:
        json.dump(personel_finance, file, indent=4)


def load_data():
    try:
        with open(FINANCE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"expenses": [], "Income": []}


def add_expense(personel_finance):
    if personel_finance["expenses"]:
        next_id = max(item["id"] for item in personel_finance["expenses"]) + 1
    else:
        next_id = 1

    while True:                                   
        try:
            amount = float(input("Amount of the purchase: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    description = input("What did you buy? ")
    category = input("What type of product? ")
    date = input("What date? ")

    entry = {"id": next_id, "description": description, "amount": amount, "category": category, "date": date}
    personel_finance["expenses"].append(entry)
    save_data(personel_finance)   
    print("Expense added successfully")

def add_income(personel_finance):
    if personel_finance["Income"]:
        next_id = max(item["id"] for item in personel_finance["Income"]) + 1
    else:
        next_id = 1
    description = input("Where did the money come from " )
    amount = float(input("How much " ))
    date = input("What date? " )

    entry = {"id": next_id, "description": description, "amount": amount, "date": date}
    personel_finance["Income"].append(entry)
    save_data(personel_finance)
    print("Income added successfully")


def view_expenses(personel_finance):
    if not personel_finance["expenses"]:
        print("No expenses")
        return
    
    for item in personel_finance["expenses"]:
        print(f"ID {item['id']} - {item['date']} - {item['description']}: ${item['amount']} ({item['category']})")

def view_income(personel_finance):
    if not personel_finance["Income"]:
        print("No income recorded yet.")
        return

    for item in personel_finance["Income"]:
        print(f"ID {item['id']} - {item['date']} - {item['description']}: ${item['amount']}")        

def statistics(personel_finance):
    expenses_list = personel_finance["expenses"]
    if len(expenses_list) == 0:
        print("No expenses recorded yet.")
        return
    
    total = 0
    amounts = []
    for item in personel_finance["expenses"]:
        total += item["amount"]
        amounts.append(item["amount"])

    average = total / len(expenses_list)
    largest = max(amounts)
    print(f"Total spending: ${total:.2f}")
    print(f"Average price: ${average:.2f}")        
    print(f"Largest expense: ${largest:.2f}")

    category_totals = {}
    for item in expenses_list:
        cat = item["category"]
        category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

    print("\nSpending by category:")
    for cat, total_amount in category_totals.items():
        print(f"  {cat}: ${total_amount:.2f}")

def delete_expense(personel_finance):
    if not personel_finance["expenses"]:
        print("No expenses")
        return

    while True:                                   
        try:
            target_id = int(input("Enter expense ID to delete: "))
            break
        except ValueError:
            print("Please enter a valid ID number.")

    found = False

    for item in personel_finance["expenses"]:
        if item["id"] == target_id:
            personel_finance["expenses"].remove(item)
            found = True
            save_data(personel_finance)   
            print("Expense deleted successfully.")
            break

    if not found:
        print("Expense ID not found.")



def delete_income(personel_finance):
    if not personel_finance["Income"]:
        print("No income")
        return
    while True:
        try:
            target_id = int(input("Enter income ID to delete: "))
            break
        except ValueError:
            print("Please enter valid ID number. ")

    found = False
    for item in personel_finance["Income"]:
        if item["id"] == target_id:
            personel_finance["Income"].remove(item)
            found = True
            save_data(personel_finance)
            print("Income deleted successfully. ")
    if not found:
        print("Income ID not found. ")

personel_finance = load_data()

while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense(personel_finance)
    elif choice == "2":
        add_income(personel_finance)
    elif choice == "3":
        view_expenses(personel_finance)
    elif choice == "4":
        view_income(personel_finance)
    elif choice == "5":
        statistics(personel_finance)
    elif choice == "6":
        delete_expense(personel_finance)
    elif choice == "7":
        delete_income(personel_finance)
    elif choice == "8":
        break
    else:
        print("Invalid option, try again.")
