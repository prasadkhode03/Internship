'''9.	Online Shopping Cart Simulation
o	Create a class Cart:
	Attribute: items (dictionary with item_name: price).
	Methods:
	add_item(name, price)
	remove_item(name)
	get_total()
	display()'''
class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            print(f"Item '{name}' already exists in the cart. Updating price to {price}.")
        self.items[name] = price
        print(f"Item '{name}' added to cart.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Item '{name}' removed from cart.")
        else:
            print(f"Item '{name}' not found in cart.")

    def get_total(self):
        return sum(self.items.values())

    def display(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nShopping Cart:")
            for name, price in self.items.items():
                print(f"{name} : {price}")
            print(f"\nTotal : {self.get_total()}")


cart = Cart()
cart.add_item("Apple", 100)
cart.add_item("Banana", 50)
cart.add_item("Orange", 120)
cart.display()
cart.remove_item("Banana")
cart.display()
print(f"\nTotal cost : {cart.get_total()}")

    