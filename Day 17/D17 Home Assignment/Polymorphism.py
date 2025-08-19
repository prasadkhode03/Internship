'''🐍 Part E: Polymorphism
13.	Create three classes:
o	Bird (method move() returns Flies),
o	Fish (method move() returns Swims),
o	Dog (method move() returns Walks).
14.	Create a function test_move(obj) that takes any of these instances and calls its move() method.
15.	Create another example:
o	Add method that behaves differently:
	Takes 2 numbers and returns the sum.
	Takes a list of numbers and returns the total.'''
class Bird:
    def move(self):
        return "Flies"
class Fish:
    def move(self):
        return "Swims"
class Dog:
    def move(self):
        return "Walks"

bird = Bird()
fish = Fish()
dog = Dog()

def test_move(obj):
    print(obj.move())

test_move(bird)
test_move(fish)
test_move(dog)
