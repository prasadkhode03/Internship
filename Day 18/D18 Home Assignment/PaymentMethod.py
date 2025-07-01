#⚔️ Part G: Bonus Challenges for Day 18
'''14.	Create an abstract class PaymentMethod:
o	Abstract method: pay(amount)
o	Subclasses:
	CreditCard
	PayPal
	BankTransfer'''
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Rs.{amount} paid by Credit Card.")
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Rs.{amount} paid by PayPal.")
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print(f"Rs.{amount} paid by Bank Transfer.")

credit_card = CreditCard(1500)
paypal = PayPal(2600)
bank_transfer = BankTransfer(3200)
