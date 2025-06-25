#🐍 Part A: Classes with Logic
'''1.	Bank Account Simulation
o	Create a class BankAccount:
	Attributes: account_number, account_holder, balance.
	Methods:
	deposit(amount)
	withdraw(amount) (check for insufficient balance)
	display() (prints account details)'''
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not Enough Balance.")
        else:
            self.balance -= amount
    def display(self):
        print("Account Number : ", self.account_number)
        print("Account Holder : ", self.account_holder)
        print("Account Balance : ", self.balance)
bank = BankAccount("S0223031121", "Prasad Khode", 78536)
print("\nAccount details initially :\n")
bank.display()
bank.deposit(4500)
bank.deposit(1200)
bank.withdraw(2300)
bank.withdraw(3600)
print("\nAccount details after transactions :\n")
bank.display()