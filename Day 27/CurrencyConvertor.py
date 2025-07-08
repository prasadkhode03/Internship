'''Currency Converter
API: https://api.exchangerate-api.com/v4/latest/USD
Goal: Convert a given amount in INR to USD, EUR, etc'''
import requests

api = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(api)
data = response.json()

INR = float(input("What is your amount in Indian Rupees? "))

USD_TO_INR = data["rates"]["INR"]
USD_TO_EUR = data["rates"]["EUR"]

print(f"{INR} INR = {INR / USD_TO_INR:.2f} USD")
print(f"{INR} INR = {INR / USD_TO_INR * USD_TO_EUR:.2f} EUR")

# for currency, rate in data["rates"].items():
#     amount = INR / USD_TO_INR * rate
#     print(f"{INR} INR = {amount} {currency}")