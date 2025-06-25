'''Task: Polymorphism with Similar Methods (Duck Typing)
Create classes:
Car with method move() → returns "Car is driving..."
Boat with method move() → returns "Boat is sailing..."
Plane with method move() → returns "Plane is flying..."
Create a function:
def test_move(vehicle):
    print(vehicle.move())
Test by passing instances of Car, Boat, and Plane.'''
class Car:
    def move(self):
        return "Car is driving"
class Boat:
    def move(self):
        return "Boat is sailing"
class Plane:
    def move(self):
        return "Plane is flying"

def test_move(vehicle):
    print(vehicle.move())

c = Car()
b = Boat()
p = Plane()
test_move(c)
test_move(b)
test_move(p)