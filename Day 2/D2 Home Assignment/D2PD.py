#🔹 Part D: Real-Life Scenario
"""6.	Create a small bill calculator:
o	Input: item name, quantity, price per item
o	Output: total cost = quantity × price
Example:
Enter item: Pen
Enter quantity: 3
Enter price per item: 15
Output: Total cost for 3 Pens is ₹45"""

#Taking Input item name, quantity, price per item
item_name = input("Enter item : ")
quantity = int(input("Enter quantity : "))
price_per_item = float(input("Enter price per item : "))
total = quantity * price_per_item   

#Output
print(f"\nTotal cost for {quantity} {item_name} is ₹{total} : ")


"""
7.	Ask the user to enter their name and age. Print how many years are left until they turn 100.
Example:
Enter your name: Anjali
Enter your age: 25
Output: Hello Anjali, you will turn 100 in 75 years!"""

#Asking the user to enter their name and age
name = input("\n\nEnter your name: ")
age = int(input("Enter your age: "))

#Printing how many years are left until they turn 100
print(f"Hello {name}, you will turn 100 in {100-age} years!")

