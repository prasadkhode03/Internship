'''2.	Student Class:
o	Make name and age private.
o	Use get_name(), set_name() and get_age(), set_age() methods.
o	Validate age to be a positive integer.'''
class Student:
    def __init__(self, name, age):
        self.__name = name
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative. Enter a valid age.")
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative. Enter a valid age.")
stud1 = Student("Rutvik Tidke", 12)
print(f"Student 1 Name : {stud1.get_name()}")
print(f"Student 1 Age : {stud1.get_age()}")
stud2 = Student("Satvik Tidke", 13)
print(f"Student 2 Name : {stud2.get_name()}")
print(f"Student 2 Age : {stud2.get_age()}")
stud1.set_age(15)
print(f"Student 1 Age : {stud1.get_age()}")