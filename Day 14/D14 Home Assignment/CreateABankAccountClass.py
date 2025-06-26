'''Create a BankAccount Class
Attributes:
account_holder, balance.
Methods:
deposit(amount) — Adds money.
withdraw(amount) — Subtracts money if available.
display_balance() — Shows the balance.
Test it: Create an account, deposit money, withdraw money, and display the balance.'''

class BankAccount:
    account_holder = ""
    balance = 0
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_balance(self):
        return self.balance

B1 = BankAccount("Piyush More", 95205)
print("Initial Balance : ", B1.display_balance())
B1.withdraw(50000)
print("Balance after withdrawing 50000 : ", B1.display_balance())
B1.deposit(15000)
print("Balance after depositing 15000 : ", B1.display_balance())