'''Create a Car Class
Attributes:

brand (string), model (string), speed (initially 0).

Methods:

accelerate() — Increases speed by 10.

brake() — Decreases speed by 5.

display_speed() — Shows the current speed.

Test it: Create a car object, call accelerate() and brake() a few times, and display the speed.'''

class Car:
    brand = "Maruti Suzuki"
    model = "800"
    speed = 0

    def accelerate(self):
        self.speed += 10
     
    def brake(self):
        self.speed -= 5

    def Car_speed(self):
        return self.speed

c = Car()
c.accelerate()
c.accelerate()
c.accelerate()
c.accelerate()
c.accelerate()
print("Speed is ",c.Car_speed())
c.brake()
c.brake()
c.brake()
print("Speed is ",c.Car_speed())
    

