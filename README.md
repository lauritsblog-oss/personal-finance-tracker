Personal Finance Tracker

A simple command-line app for tracking your personal expenses and income. Everything is stored locally in a JSON file, so there is no database, no account and no internet connection needed.

Features
Add expenses (amount, description, category, date)
Add income (source, amount, date)
View all recorded expenses and income
Statistics on your spending:
Total spending
Average expense
Largest expense
Spending broken down by category
Delete expenses and income by ID
Data is saved automatically after every change
Requirements
Python 3.6 or newer
No external libraries (uses only os and json from the standard library)
Getting Started
Clone the repository:
bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
Run the program:
bash
   python main.py

(Replace main.py with the name of your file.)

Usage

When the program starts you will see this menu:

1. Add Expense
2. Add Income
3. View Expenses
4. View income
5. Statistics
6. Delete Expense
7. Delete Income
8. Exit

Type the number of the option you want and press Enter.

Example session
Choose an option: 1
Amount of the purchase: 49.95
What did you buy? Groceries
What type of product? Food
What date? 2026-10-12
Expense added successfully
Choose an option: 5
Total spending: $49.95
Average price: $49.95
Largest expense: $49.95

Spending by category:
  Food: $49.95
Data Storage

All data is saved in finance.json, which is created automatically in the same folder as the script the first time you add something. If the file is missing or corrupted, the program starts with an empty record.

Structure of the file:

json
{
    "expenses": [
        {
            "id": 1,
            "description": "Groceries",
            "amount": 49.95,
            "category": "Food",
            "date": "2026-10-12"
        }
    ],
    "Income": [
        {
            "id": 1,
            "description": "Salary",
            "amount": 25000.0,
            "date": "2026-10-01"
        }
    ]
}

Each entry gets a unique ID, which is used when deleting entries.

Project Structure
.
├── main.py         # The application
├── finance.json    # Your data (created automatically)
└── README.md
Possible Improvements
Validate the date format (e.g. YYYY-MM-DD) and default to today's date
Add input validation for the income amount
Show a balance (income minus expenses)
Filter statistics by month or category
Support a currency setting (currently shown in $)
Export to CSV
License

Add a license of your choice here (for example MIT), or remove this section.
