'''16.	Build a robust Student Registration System:
o	Abstract class: Person
	Abstract method: get_role()
o	Subclasses:
	Student (encapsulates marks and validates range).
	Teacher (encapsulates salary).
	AdminStaff (encapsulates department).'''
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, role):
        self.role = role
    @abstractmethod
    def get_role(self):
        return self.role
class Student(Person):
    def __init__(self, role, marks):
        super().__init__(role)
        self.marks = marks
    def set_marks(self, marks):
        if 0 >= marks >= 100:
            self.marks = marks
    def get_marks(self):
        return self.marks
class Teacher(Person):
    def __init__(self, role, salary):
        super().__init__(role)
        self.salary = salary
    def set_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary
class AdminStaff(Person):
    def __init__(self, role, department):
        super().__init__(role)
        self.department = department
    def set_department(self, department):
        self.department = department
    def get_department(self):
        return self.department

student = Student("Student", 78)
print(f"Marks of Student : {student.get_marks()}")
teacher = Teacher("Lecturer", 45000)
teacher.set_salary(50000)
print(f"Salary of {teacher.get_role} is {teacher.get_salary}.")
admin_staff = AdminStaff("Adminstrator", "Technical Department")
print(f"Department of {admin_staff.get_role} is {admin_staff.get_department}")

    
    