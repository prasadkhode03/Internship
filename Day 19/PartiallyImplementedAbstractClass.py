'''Partially Implemented Abstract Class
Instructions:
Create an abstract class named Employee:
Abstract method: calculate_salary().
Concrete method: display_role() (prints role).
Create concrete classes:
FullTimeEmployee with a calculate_salary() method.
PartTimeEmployee with a calculate_salary() method.
Instantiate both and test both methods.'''
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_role(self, role):
        self.role = role
        print("Employee Role :", self.role)

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full Time Employee Salary : 50000")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part Time Employee Salary : 15000")

full = FullTimeEmployee()
part = PartTimeEmployee()
full.display_role("Software Developer")
full.calculate_salary()
part.display_role("Web Developer")
part.calculate_salary()