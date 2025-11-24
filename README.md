Bank Management System (Python)

A simple, console-based Bank Management System built in Python.
This project lets an admin perform banking operations such as creating accounts, depositing money, withdrawing money, and viewing account details — all stored in memory without using a database.

This project is great for beginners learning Python, functions, lists, and basic data handling.

📌 Features
✅ Admin Login

Secure login using a predefined admin password.

Prevents unauthorized access.

✅ Create New Bank Accounts

Auto-generates unique account numbers starting from 1001.

Stores customer name, city, PIN, and balance.

✅ Deposit Money

Allows depositing any positive amount.

Updates account balance instantly.

✅ Withdraw Money

Withdraw only if sufficient balance exists.

User-friendly error messages for invalid actions.

✅ View Account Details

Displays a clean summary of a customer’s account.

✅ View All Accounts (Admin Only)

Displays a table of all existing accounts (account no, name, city, balance).

🛠️ How It Works

The system uses simple in-memory Python data structures:

BANK_ACCOUNTS → list of account dictionaries

NEXT_ACC_NO → auto-increment account number

ADMIN_CREDENTIALS → stored admin password

No external database is required.

This keeps the project lightweight and easy to understand.

📂 Project Structure
bank_management.py   # Main program file


All logic — login, account operations, helper functions — is inside this single file.

▶️ How to Run

Make sure you have Python 3 installed.

Save the code as:

bank_management.py


Open your terminal / command prompt.

Run:

python bank_management.py


Login using the default admin password:

Password: shrey


Choose options from the menu and start managing accounts.

📝 Admin Menu Options

Once logged in, you get:

1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Display Account Details
5. Display All Accounts (Admin View)
6. Logout

⚠️ Known Limitations (You Can Improve These)

The system crashes if the user enters non-numeric values in places like amount or account number (no try/except yet).

Data is not saved permanently (everything resets when the program closes).

Only one admin is supported.

PIN is stored and validated but not masked or encrypted.

These can be turned into great improvement ideas for version-2 of the project.

🌟 Why I Made This Project

This project demonstrates:

Python fundamentals

Working with lists & dictionaries

Menu-driven programs

Basic authentication

Real-world problem solving

And it is perfect for a beginner-level Python project submission.

📄 License

This project is free to use, modify, and improve.
