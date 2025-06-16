'''9.	Inventory System
o	Create a dictionary inventory where keys are product names ("pen", "notebook", "eraser") and values are quantities.
o	Write a function update_stock(item, quantity) to increase stock.
o	If item is not in inventory, add it.'''

inventory = {"pen" : 500, "notebook" : 270, "eraser" : 100}

def update_stock(item, quantity):
    inventory[item] = quantity
    return inventory

print("Updating Stock : ", update_stock("pencil", 150))
print("Updating Stock : ", update_stock("eraser", 150))
