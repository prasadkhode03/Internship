'''Create a Person class
Add an _init_ method that takes name and age.

Add a method called introduce() that prints:

Hi, I am <name> and I am <age> years old.

Test:
Create an object (Person("Alice", 25)) and call introduce()'''

class Person:
    name = "Alice"
    age = 25

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, i am {self.name} and i am {self.age} year old ")

p1 = Person("Piyush",18)
p1.introduce()