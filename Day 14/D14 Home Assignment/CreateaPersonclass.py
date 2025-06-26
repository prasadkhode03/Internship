'''Create a Person class
Add an _init_ method that takes name and age.
Add a method called introduce() that prints:
Hi, I am <name> and I am <age> years old.
Test:
Create an object (Person("Alice", 25)) and call introduce().'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

P1 = Person("Prasad", 17)
P1.introduce()
