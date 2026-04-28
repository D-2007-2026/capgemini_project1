balance = 10000
transactions = []

def show_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

def check_balance():
    print(f"Balance: Rs. {balance}")

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited Rs. {amount}")
        print("Done! New balance:", balance)
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))
    if amount > balance:
        print("Insufficient balance")
    elif amount > 0:
        balance -= amount
        transactions.append(f"Withdrawn Rs. {amount}")
        print("Done! Remaining balance:", balance)
    else:
        print("Invalid amount")

def statement():
    if not transactions:
        print("No transactions yet")
    else:
        for i, t in enumerate(transactions, 1):
            print(f"{i}. {t}")

pin = int(input("Enter PIN: "))
if pin != 1234:
    print("Wrong PIN!")
else:
    while True:
        show_menu()
        choice = input("Choice: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            statement()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
