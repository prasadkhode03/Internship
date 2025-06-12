#Part C: Data Formatting + Return
"""8.	Currency Converter
Function convert_to_usd(inr, rate=83.2) → converts INR to USD (default rate 83.2)"""

def convert_to_usd(inr, rate = 83.2):
    USD = inr / rate
    return USD

inr = int(input("Enter the amount of rupees : "))
print("USD =",convert_to_usd(inr))