'''Create a Rectangle Class
Attributes: length, width.
Methods:
area() — Returns the area of the rectangle.
perimeter() — Returns the perimeter.
Test it: Create a few instances and print their area and perimeter.'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
R1 = Rectangle(45, 60)
# print("Area of Rectangle 1 : ", R1.area())
# print("Perimeter of Rectangle 1 : ", R1.perimeter())

R2 = Rectangle(10.3, 5.6)
# print("\nArea of Rectangle 2 : ", R2.area())
# print("Perimeter of Rectangle 2 : ", R2.perimeter())

for idx, rect in enumerate([R1, R2]):
    print(f"Area of Recangle {idx+1}: ", rect.area())
    print(f"Perimeter of Recangle {idx+1}: ", rect.perimeter(), "\n")