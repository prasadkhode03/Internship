'''Task: Multilevel Inheritance
Create a class Number:
Attribute: value.
Create a class SquareNumber that inherits from Number:
Method: square() → returns value * value.
Create a class CubeNumber that inherits from SquareNumber:
Method: cube() → returns value * value * value.
Test:
Number(2) → value = 2
SquareNumber(3).square() → 9
CubeNumber(3).cube() → 27'''

class Number:
    def __init__(self, value):
        self.value = value
class SquareNumber(Number):
    def square(self):
        return self.value * self.value
class CubeNumber(Number):
    def cube(self):
        return self.value * self.value * self.value

print(Number(2).value)

print(SquareNumber(3).square())

print(CubeNumber(3).cube())