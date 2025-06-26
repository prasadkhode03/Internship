'''Tasks on Encapsulation
Task: Private Attribute and Method
Instructions:
Create a class Car.
Add a private attribute __speed.
Create a method accelerate(value) to increase the __speed.
Create a method get_speed() to return the current __speed.
Try accessing __speed directly (and understand why it doesn’t work).'''
class Car:
    def __init__(self, speed):
        self.__speed = speed
    def accelerate(self, value):
        self.__speed += value
    def get_speed(self):
        return self.__speed

car = Car(50)
car.accelerate(20)
car.accelerate(20)
#print(car.__speed) AttributeError: 'builtin_function_or_method' object has no attribute '__speed'
#If you access the variable speed directly it will show AttributeError because it is private attribute of Car class so we cannot access it directly
print("Current Car Speed : ", car.get_speed())