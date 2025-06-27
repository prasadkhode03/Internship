'''⚔️ Part F: Method Overriding & Super Usage
16.	Create a parent class Employee:
o	Attribute: name, salary.
o	Method: display().
17.	Create a child class Manager inherits from Employee:
o	New Attribute: department.
o	Override display() method and use super() to call parent method.
18.	Create a parent class BankAccount:
o	Method: calculate_interest() returns some value.
19.	Create a child class SavingsAccount:
o	Override the method to return a different interest rate.'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name :", self.name)
        print("Salary :", self.salary)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        super().display()
        print("Department :", self.department)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def calculate_interest(self):
        return self.balance * 0.05  #5 percent
class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    def calculate_interest(self):
        return self.balance * 0.07  #7 percent

manager = Manager("Om Loknar", 15200, "Marketing")
manager.display()
saving = SavingsAccount(9500)
print("Interest :", saving.calculate_interest())

    
