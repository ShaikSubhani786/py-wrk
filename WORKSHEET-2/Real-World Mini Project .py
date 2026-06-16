class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Create Bank Account
account_number = input("Enter Account Number: ")
account_holder_name = input("Enter Account Holder Name: ")
initial_balance = float(input("Enter Initial Balance: "))

account = BankAccount(account_number, account_holder_name, initial_balance)

# Menu-Driven Program
while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        print("Thank you for using the banking system.")
        break

    else:
        print("Invalid choice. Please try again.")