#⚡️ Part G: Complex Challenges
'''20.	Shape Manager:
o	Create a parent class Shape with a method draw().
o	Create child classes Square, Rectangle, Circle, and implement their draw() method.
o	Maintain a list of shapes and iterate over them, calling draw().'''
class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

shapes = [Square(), Rectangle(), Circle()]

for shape in shapes:
        shape.draw()