'''Task: 
Create a parent class Vehicle with:
An attribute brand.
A method describe() that returns: "This is a vehicle."
Create a child class Car that inherits from Vehicle and:
Adds an attribute model.
Overrides the describe() method to return: "This is a [brand] [model]."
Test it:
Create an object of Car and call its describe() method.'''

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def describe(self):
        return "This is a vehicle."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def describe(self):
        return f"This is a {self.brand} {self.model} "
    
car = Car("Rolls Royce", "Phantom")
print(car.describe())