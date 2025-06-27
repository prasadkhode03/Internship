'''21.	Employee Hierarchy Simulation:
o	Create parent class Person (name, age).
o	Create child classes:
	Employee inherits Person (add salary).
	Teacher inherits Employee (add subject).
	Engineer inherits Employee (add specialization).
o	Implement a display() method in each class.'''
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def display(self):
        print("\nName :", self.name)
        print("Age :", self.age)
        print("Salary :", self.salary)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def display(self):
        print("\nName :", self.name)
        print("Age :", self.age)
        print("Subject :", self.subject)
class Engineer(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization
    def display(self):
        print("\nName :", self.name)
        print("Age :", self.age)
        print("Specialization :", self.specialization)

emp = Employee("Nachiket Tidke", 20, 32520.03)
teacher = Teacher("Rutvik Tidke", 23, "Mechanics")
engi = Engineer("Satvik Tidke", 21, "Civil Engineering")
emp.display()
teacher.display()
engi.display()