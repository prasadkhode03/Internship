'''2.	Inventory Item
o	Create a class Item:
	Attributes: name, price, quantity.
	Methods:
	add_stock(amount) – Increase quantity.
	sell_stock(amount) – Decrease quantity if available.
	get_total_value() – Returns total value of stock (price * quantity).'''
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def add_stock(self, amount):
        self.quantity += amount
    def sell_stock(self, amount):
        if amount > self.quantity:
            print("Quantity out of stock.")
        else:
            self.quantity -= amount
    def get_total_value(self):
        return  self.price * self.quantity

item = Item("Laptop", 42950.20, 30)
item.add_stock(10)
item.sell_stock(15)
print(item.get_total_value())