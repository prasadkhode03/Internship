'''7.	Employee Class
Attributes:
	Class Attribute: company_name = "TechCorp"
	Instance Attributes: name, salary
Method:
	give_raise(percent) – Increases the employee’s salary by the given percentage.
	display() – Prints employee details.'''
class Employee:
    company_name = "TechCorp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def give_raise(self, percent):
        self.percent = percent / 100
        self.salary *= (1 + percent / 100)
    def display(self):
        print(f"Employee name : {self.name}")
        print(f"Employee salary : {self.salary}")

e = Employee("Piyush Patade", 15550)
e.give_raise(2)
e.display()