#⛓️ Part C: Multilevel Inheritance
'''6.	Create a parent class Animal:
o	Method: sound() returns Generic Animal Sound.'''
'''7.	Create a child class Dog inherits from Animal:
o	Override sound() returns Bark.'''
'''8.	Create a grandchild class Puppy inherits from Dog:
o	Override sound() returns Yip.'''
#9.	Test by creating instances of Animal, Dog, and Puppy and invoking their sound() methods.

class Animal:
    def sound(self):
        return "Generic Animal Sound."
class Dog(Animal):
    def sound(self):
        return "Bark."
class Puppy(Dog):
    def sound(self):
        return "Yip"
ani = Animal()
dog = Dog()
pup = Puppy()
print(ani.sound())
print(dog.sound())
print(pup.sound())