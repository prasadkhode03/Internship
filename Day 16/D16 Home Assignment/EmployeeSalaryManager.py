'''4.	Employee Salary Manager
o	Create an Employee class:
	Attributes:
	Instance: name, salary.
	Class Attribute: min_wage = 10000.
	Method:
	adjust_salary() – If salary < min_wage, set it to min_wage.
	display() – Shows employee name and salary.
o	Test with different employee instances.'''
class Employee:
    min_wage = 10000
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def adjust_salary(self):
        if self.salary < self.min_wage:
            self.salary = self.min_wage
    def display(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee Salary : {self.salary}")

e1 = Employee("Piyush Patade", 15550)
print("Information of Employee 1 : ")
e1.display()
e2 = Employee("Om Loknar", 7500)
e2.adjust_salary()
print("\nInformation of Employee 2 : ")
e2.display()
        