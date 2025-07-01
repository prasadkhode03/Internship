'''3.	Product Class:
o	Make price private.
o	Use a method to apply discount (without direct access).'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage and discount_percentage <= 100:
            discount_amount = (discount_percentage / 100) * self.__price
            self.__price -= discount_amount
            print(f"Discount applied: {discount_percentage}%")
        else:
            print("Invalid discount percentage.")

    def display_product_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: Rs.{self.__price:.2f}")

product = Product("Laptop", 40000)
product.display_product_info()

product.apply_discount(10)
product.display_product_info()
