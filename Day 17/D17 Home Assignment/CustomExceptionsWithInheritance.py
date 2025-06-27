'''24.	Custom Exceptions with Inheritance:
o	Create a parent exception BankError.
o	Create child exceptions:
	InsufficientBalanceError.
	InvalidAmountError.
o	Simulate a bank withdrawal method that raises these errors appropriately.'''

class BankError(Exception):
    """Base class for all bank-related errors."""
    pass

class InsufficientBalanceError(BankError):
    """Raised when withdrawal amount exceeds the balance."""
    def __init__(self, message="Insufficient balance for withdrawal."):
        super().__init__(message)

class InvalidAmountError(BankError):
    """Raised when withdrawal amount is zero or negative."""
    def __init__(self, message="Invalid amount. Enter a positive number."):
        super().__init__(message)


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError()
        elif amount > self.balance:
            raise InsufficientBalanceError()
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")

if __name__ == "__main__":
    account = BankAccount(balance=1000)

    try:
        account.withdraw(0)  
    except BankError as e:
        print(f"Error: {e}")

    try:
        account.withdraw(1500) 
    except BankError as e:
        print(f"Error: {e}")

    try:
        account.withdraw(300)  
    except BankError as e:
        print(f"Error: {e}")

