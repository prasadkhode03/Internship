'''Create a Rectangle Class
Attributes: length, width.

Methods:

area() — Returns the area of the rectangle.

perimeter() — Returns the perimeter.

Test it: Create a few instances and print their area and perimeter.'''

class Rectangle:
    length = 0
    width = 0
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
rec = Rectangle(10,5)
print(f"Length: {rec.length}, Width: {rec.width}")
print(f"Area: {rec.length * rec.width}")
print(f"Perimeter: {rec.perimeter()}")
