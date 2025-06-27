'''22.	Geometric Calculator:
o	Create parent class Polygon (attribute sides).
o	Create child classes:
	Square: area = side^2.
	Rectangle: area = length * breadth.
	Triangle: area = (base * height)/2.
o	Polymorphically call area methods.'''
class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Square(Polygon):
    def __init__(self, side):
        super().__init__(4)
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__(4)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Square(5), Rectangle(4, 6), Triangle(3, 7)]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")

        