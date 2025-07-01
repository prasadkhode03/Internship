#⚡️ Part B: Abstraction with Abstract Classes
'''4.	Create an abstract class Shape:
o	Abstract method: area()
o	Abstract method: perimeter()'''
'''5.	Create concrete subclasses:
o	Rectangle: Implement area() and perimeter().
o	Circle: Implement area() and perimeter().'''
#6.	Test by creating instances of Rectangle and Circle and calling their methods.
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def perimeter():
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def perimeter(self):
        return 2 * pi * self.radius
rectangle = Rectangle(12.30, 45.30)
circle = Circle(4.2)
print(f"Area of Rectangle : {rectangle.area():.2f}")
print(f"Perimeter of Rectangle : {rectangle.perimeter():.2f}")
print(f"Area of Circle : {circle.area():.2f}")
print(f"Perimeter of Circle : {circle.perimeter():.2f}")
