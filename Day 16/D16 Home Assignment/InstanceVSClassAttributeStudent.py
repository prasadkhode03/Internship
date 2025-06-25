#⚡ Part B: Advanced Attribute Handling
'''3.	Instance vs. Class Attribute Demo
o	Create a class Student:
	Class Attribute: school_name = "ABC High School"
	Instance Attributes: name, age, marks
	Method:
	display() – Shows student details and the school name.
o	Change school_name for one object, and observe the result on other instances.'''
class Student:
    school_name = "ABC High School"
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Name of Student : {self.name}")
        print(f"Age : {self.age}")
        print(f"Marks : {self.marks}")
        print(f"School Name : {self.school_name}")
s1 = Student("Om", 16, 45)
s2 = Student("Prasad", 18, 76)
print("Student 1 Information : ")
s1.display()
print("\nStudent 2 Information : ")
s2.display()
s3 = Student("Piyush", 17, 55)
s3.school_name = "K. K. Wagh High School"
print("\nStudent 3 Information : " )
s3.display()

