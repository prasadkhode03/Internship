#🚗 Part D: Real-World Simulation Challenges
'''6.	Car Service Center
o	Create a class Car:
	Attributes:
	brand, model, speed, fuel_level.
	Methods:
	accelerate() – Increases speed.
	brake() – Decreases speed.
	add_fuel(amount) – Increases fuel_level.
	status() – Prints the status of the car.'''
class Car:
    def __init__(self, brand, model, speed, fuel_level):
        self.brand = brand
        self.model = model
        self.speed = speed 
        self.fuel_level = fuel_level
    def accelerate(self):
        self.speed += 20
    def brake(self):
        self.speed -= 20
    def add_fuel(self, amount):
        self.fuel_level += amount
    def status(self):
        print(f"Car Brand : {self.brand}")
        print(f"Car Model : {self.model}")
        print(f"Car Speed : {self.speed}")
        print(f"Car Fuel Level : {self.fuel_level}")
        print(f"{self.brand} {self.model} is running on {self.speed} KM/H with {self.fuel_level} ltr. fuel")
c = Car("BMW", "M4", 120, 15)
c.accelerate()
c.accelerate()
c.brake()
c.add_fuel(2)
c.status()
