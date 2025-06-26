'''Create a Car Class
Attributes:
brand (string), model (string), speed (initially 0).
Methods:
accelerate() — Increases speed by 10.
brake() — Decreases speed by 5.
display_speed() — Shows the current speed.
Test it: Create a car object, call accelerate() and brake() a few times, and display the speed.'''
class Car:
    brand = "BMW" 
    model = "M4"
    speed = 0
    def accelerate(self):
        self.speed += 10
    def brake(self):
        self.speed -= 5
    def display_speed(self):
        return self.speed

C1 = Car()
C1.accelerate() #10
C1.accelerate() #20
C1.accelerate() #30
C1.accelerate() #40
print("Speed : ", C1.display_speed()) #40
C1.brake() #35
C1.brake() #30
C1.brake() #25
print("Speed : ", C1.display_speed()) #25

    