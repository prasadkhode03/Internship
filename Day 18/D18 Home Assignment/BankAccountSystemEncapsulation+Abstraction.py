'''👥 Part E: Encapsulation + Abstraction Combined
11.	Build a Bank System:
o	Abstract class Account:
	Private balance
	Abstract method: calculate_interest()
o	Subclasses:
	SavingsAccount: 4% interest.
	CurrentAccount: 1% interest.
o	Methods:
	get_balance() – Returns the balance.
	set_balance() – Updates balance with checks.
	calculate_interest() – Returns calculated interest.
o	Test by creating instances and invoking methods.'''

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    @abstractmethod
    def calculate_interest(self):
        pass
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance.")

class SavingsAccount(Account):
    def __init__(self, initial_balance):
        super().__init__(initial_balance)

    def calculate_interest(self):
        interest_rate = 0.04
        interest = self.get_balance() * interest_rate
        return interest

class CurrentAccount(Account):
    def __init__(self, initial_balance):
        super().__init__(initial_balance)

    def calculate_interest(self):
        interest_rate = 0.01
        interest = self.get_balance() * interest_rate
        return interest

savings_account = SavingsAccount(1000)
print(f"Savings Account Balance : Rs.{savings_account.get_balance()}")
print(f"Savings Account Interest : Rs.{savings_account.calculate_interest():.2f}")

current_account = CurrentAccount(500)
print(f"Current Account Balance: Rs.{current_account.get_balance()}")
print(f"Current Account Interest: Rs.{current_account.calculate_interest():.2f}")

savings_account.set_balance(1500)
print(f"Updated Savings Account Balance: Rs.{savings_account.get_balance()}")
print(f"Updated Savings Account Interest: Rs.{savings_account.calculate_interest():.2f}")

    
