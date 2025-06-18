'''12.	ATM Simulator
•	Initial balance = 5000
•	Ask user to withdraw an amount.
•	If amount > balance, raise an exception with message "Insufficient balance".
•	Always print "Transaction ended" in finally.'''
balance = 5000
try :
    amount = int(input("Enter withdraw amount : "))
    if amount > balance:
        raise Exception("Insufficient balance.")
    print(f"Rs. {amount} withdrawl successful.")
except Exception as e:
    print("Warning :", e)
finally:
    print("Transaction ended")
