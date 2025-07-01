#🔐 Part A: Encapsulation Basics
'''1.	BankAccount Class:
o	Make balance a private attribute.
o	Add deposit() and withdraw() methods.
o	Prevent withdrawals if balance is insufficient.'''
class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. Current balance : Rs.{self.__balance}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew Rs.{amount}. Current balance : Rs.{self.__balance}")
        else:
            print("Balance Insufficient.")
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
print(f"Initial balance : Rs.{account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)

print(f"Balance after few transactions : Rs.{account.get_balance()}")