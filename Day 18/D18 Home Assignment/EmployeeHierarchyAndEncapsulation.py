'''13.	Employee Hierarchy with Encapsulation:
o	Abstract class: Employee
	Abstract method: calculate_salary()
	Private attribute: base_salary
o	Subclasses:
	FullTimeEmployee (adds benefits and bonuses).
	PartTimeEmployee (hourly rate and hours worked).'''
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, base_salary):
        self.__base_salary = base_salary

    def get_base_salary(self):
        return self.__base_salary

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, base_salary, benefits, bonuses):
        super().__init__(base_salary)
        self.__benefits = benefits
        self.__bonuses = bonuses

    def calculate_salary(self):
        return self.get_base_salary() + self.__benefits + self.__bonuses

class PartTimeEmployee(Employee):
    def __init__(self, base_salary, hourly_rate, hours_worked):
        super().__init__(base_salary)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.get_base_salary() + (self.__hourly_rate * self.__hours_worked)

full_time_employee = FullTimeEmployee(50000, 10000, 5000)
print(f"Full-time Employee Salary : Rs.{full_time_employee.calculate_salary()}")

part_time_employee = PartTimeEmployee(20000, 50, 100)
print(f"Part-time Employee Salary : Rs.{part_time_employee.calculate_salary()}")