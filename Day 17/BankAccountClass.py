'''Create a BankAccount Class
Attributes:

account_holder, balance.

Methods:

deposit(amount) — Adds money.

withdraw(amount) — Subtracts money if available.

display_balance() — Shows the balance.

Test it: Create an account, deposit money, withdraw money, and display the balance.'''

class BankAccount:
    acc_holder = "Piyush More"
    balance = 5000

    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def dis_Bal(self):
        return self.balance
    
Bank = BankAccount()
print("Balance is ",Bank.dis_Bal())
Bank.deposit(1500)
print("Balance is ",Bank.dis_Bal())
Bank.withdraw(2000)
print("Balance is ",Bank.dis_Bal())
