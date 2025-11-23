
# --- GLOBAL IN-MEMORY DATA STORES ---

# 1. Login/Admin Credentials (fixed, no need for a list since it's only one admin)
# Format: {'admin_username': 'admin', 'password': 'shrey'}
ADMIN_CREDENTIALS = {'admin': 'shrey'}

# 2. Bank Accounts
# Format: [{'acc_no': int, 'name': str, 'city': str, 'pin': int, 'balance': float}]
BANK_ACCOUNTS = []

# 3. Account Number Tracker (Replaces the 'sno' table)
NEXT_ACC_NO = 1001

# --- HELPER FUNCTIONS ---

def get_next_acc_no():
    """Generates the next unique account number."""
    global NEXT_ACC_NO
    acc_number = NEXT_ACC_NO
    NEXT_ACC_NO += 1
    return acc_number

def find_account(account_number):
    """Finds an account dictionary by account number. Note: Assumes account_number is already valid."""
    # This function is now less robust without the ValueError check, relying on calling context.
    acc_no_int = int(account_number)
    for account in BANK_ACCOUNTS:
        if account['acc_no'] == acc_no_int:
            return account
    return None

# --- CORE BANKING FUNCTIONS ---

def create_account():
    """Prompts for details and creates a new bank account."""
    print("\n---------- CREATE ACCOUNT ----------")
    
    name = input("Enter name: ").strip().title()
    city = input("Enter your city: ").strip().title()
    
    while True:
        pin = input("Enter 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            pin_int = int(pin)
            break
        print("Error: PIN must be exactly 4 digits.")
        
    new_acc_no = get_next_acc_no()
    
    new_account = {
        'acc_no': new_acc_no,
        'name': name,
        'city': city,
        'pin': pin_int,
        'balance': 0.00
    }
    
    BANK_ACCOUNTS.append(new_account)
    
    print("\nSUCCESS: Account created!")
    print(f"  Account Number: {new_acc_no}")
    print(f"  Account Holder: {name}")


def deposit_money():
    """Deposits money into an existing account."""
    print("\n----------- DEPOSIT MONEY -----------")
    
    # NOTE: If non-numeric input is provided here, the program will crash (due to lack of try/except).
    account_input = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    
    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return

    account = find_account(account_input)
    
    if account:
        account['balance'] += amount
        print(f"\nSUCCESS: Deposited ${amount:.2f}.")
        print(f"  New Balance for {account['acc_no']}: ${account['balance']:.2f}")
    else:
        print("Error: Account number not found.")


def withdraw_money():
    """Withdraws money from an existing account."""
    print("\n----------- WITHDRAW MONEY ----------")
    
    # NOTE: If non-numeric input is provided here, the program will crash (due to lack of try/except).
    account_input = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return
        
    account = find_account(account_input)
    
    if account:
        if account['balance'] < amount:
            print("Error: Insufficient balance.")
            print(f"  Current Balance: ${account['balance']:.2f}")
            return
        
        # Successful withdrawal
        account['balance'] -= amount
        print(f"\nSUCCESS: Withdrew ${amount:.2f}.")
        print(f"  New Balance for {account['acc_no']}: ${account['balance']:.2f}")
    else:
        print("Error: Account number not found.")


def display_account():
    """Displays the details of a single account."""
    print("\n---------- DISPLAY ACCOUNT ----------")
    # NOTE: If non-numeric input is provided here, the program will crash (due to lack of try/except).
    account_input = input("Enter account number: ")
    account = find_account(account_input)
    
    if account:
        print("\n--- Account Details ---")
        print(f"  Account No: {account['acc_no']}")
        print(f"  Name:       {account['name']}")
        print(f"  City:       {account['city']}")
        # PIN is kept hidden for display purposes
        print(f"  Balance:    ${account['balance']:.2f}")
        print("-----------------------")
    else:
        print("Error: Account number not found.")

# --- MAIN LOGIC ---

def admin_menu():
    """Shows the menu available after a successful login."""
    while True:
        print("\n==================================")
        print("ADMINISTRATION MENU")
        print("==================================")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Details")
        print("5. Display All Accounts (Admin View)")
        print("6. Logout")
        
        ch2 = input('Enter your choice: ').strip()
        
        if not ch2.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        ch2 = int(ch2)
        
        if ch2 == 1:
            create_account()
        elif ch2 == 2:
            deposit_money()
        elif ch2 == 3:
            withdraw_money()
        elif ch2 == 4:
            display_account()
        elif ch2 == 5:
            # Extra Admin Function to display all accounts
            print("\n---------- ALL ACCOUNTS (ADMIN) ----------")
            if not BANK_ACCOUNTS:
                print("No accounts currently open.")
                continue
            
            # Simple table view
            print(f"{'ACC NO':<8} | {'NAME':<20} | {'CITY':<15} | {'BALANCE':>10}")
            print("-" * 59)
            for acc in BANK_ACCOUNTS:
                print(f"{acc['acc_no']:<8} | {acc['name']:<20} | {acc['city']:<15} | ${acc['balance']:>9.2f}")
            print("------------------------------------------")
        elif ch2 == 6:
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please select from 1-6.")
                


def main():
    """Main program entry point with login loop."""
    print('--------------------------------')
    print('\tBANK MANAGEMENT SYSTEM')
    print('--------------------------------')

    # Initializing with some sample data for testing
    global BANK_ACCOUNTS, NEXT_ACC_NO
    BANK_ACCOUNTS.append({'acc_no': 1000, 'name': 'Shrey Admin', 'city': 'Indore', 'pin': 1234, 'balance': 50000.00})
    NEXT_ACC_NO = 1001
    
    while True:
        print("\n------ LOGIN / EXIT ------")
        print("1. Login (Admin)")
        print("2. Exit")
        
        ch = input("Enter your choice: ").strip()
        
        if ch == '1':
            password_input = input("Enter Admin password: ")
            
            # Authentication check using the dictionary
            if password_input == ADMIN_CREDENTIALS.get('admin'):
                print("Successfully logged in!")
                admin_menu()
            else:
                print('Wrong password. Please try again.')
                
        elif ch == '2':
            print("Exiting the Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
