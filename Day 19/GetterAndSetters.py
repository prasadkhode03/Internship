'''Task: Getters and Setters
Instructions:
Create a class Person.
Add a private attribute __age.
Create:
A method set_age(value) that validates if the age is a positive number.
A method get_age() to return the age.
Try setting both valid and invalid ages.'''
class Person:
    # def __init__(self, age):
    #     self.__age = age
    def set_age(self, value):
        if value > 0:
            self.__age = value
            print("Valid Age..")
        else:
            print("Invalid Age, Age cannot be negative!")
    def get_age(self):
        return self.__age

person = Person()
person.set_age(-2)
person.set_age(15)
print("Current Age :", person.get_age())
