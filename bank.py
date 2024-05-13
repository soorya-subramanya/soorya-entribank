import random

class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully. New balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn successfully. New balance:", self.balance)
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print("Account Balance:", self.balance)

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder):
        account_number = random.randint(10000, 99999)
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)
        self.accounts[account_number] = Account(account_number, account_holder)
        print("Account created successfully. Account Number:", account_number)

    def login(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Invalid account number!")
            return None

def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_holder = input("Enter your name: ")
            bank.create_account(account_holder)
        elif choice == '2':
            account_number = int(input("Enter your account number: "))
            account = bank.login(account_number)
            if account:
                while True:
                    print("\nWelcome,", account.account_holder)
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    option = input("Enter your option: ")
                    if option == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    elif option == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                    elif option == '3':
                        account.display_balance()
                    elif option == '4':
                        break
                    else:
                        print("Invalid option!")
        elif choice == '3':
            print("Thank you for using the Bank. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

