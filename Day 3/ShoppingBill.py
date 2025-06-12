""""task 1:
Create a "Shopping Bill" program:

Take input with proper data types: item name, quantity, price per item.

Calculate total = quantity × price.

finally,
Print a bill"""

item_name = input("Enter Item Name : ")
quantity = int(input("Enter Quantity : "))
price_per_item = float(input("Enter Price per Item : "))
total = quantity * price_per_item   

print("\n--- Shopping Bill ---")
print("Item Name : ",item_name) 
print("Quantity : ",quantity)
print("Price per Item : ",price_per_item)
print("Total : ",total)