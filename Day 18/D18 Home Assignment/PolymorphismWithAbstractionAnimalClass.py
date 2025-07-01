'''🎨 Part D: Polymorphism with Abstraction
9.	Create an abstract class Animal:
o	Abstract method: make_sound()
10.	Subclasses:
o	Dog: Returns Woof
o	Cat: Returns Meow
o	Cow: Returns Moo
o	Test polymorphism by looping over instances and calling make_sound().'''
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{type(animal).__name__}: {animal.make_sound()}")
