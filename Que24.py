"""
Q.24.Write a Python class BankAccount with attributes like account_number,
balance, date_of_opening and customer_name, and methods like deposit,
withdraw, and check_balance.    
"""


class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(
                f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal unsuccessful.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


account = BankAccount("1234567890", 10000, "2023-01-01", "John Doe")

account.check_balance()

account.deposit(5000)

account.withdraw(2000)

account.withdraw(20000)

account.check_balance()
