#🗂️ Part A: Single Inheritance
'''1.	Create a parent class Person with attributes:
o	name, age.
o	Method: display().'''
'''2.	Create a child class Student that inherits Person:
o	Add roll_number attribute.
o	Override the display() method.'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
    def display(self):
        super().display()
        print("Roll No. : ", self.roll_number)
student = Student("Rutvik Tidke", 16, 60)
student.display()