'''23.	Zoo Simulation:
o	Create parent class Animal:
	Methods: sound(), move().
o	Create child classes:
	Lion: sound() -> Roar.
	Snake: move() -> Slither.
	Parrot: sound() -> Talk.
o	Maintain a list of animals and call their methods.'''
class Animal:
    def sound(self):
        print("Generic animal sound.")
    def move(self):
        print("Generic animal movement.")
class Lion(Animal):
    def sound(self):    
        print("Lion Roar.")
class Snake(Animal):
    def move(self):
        print("Snake Slither.")
class Parrot(Animal):
    def sound(self):
        print("Parrot Talk.")

objlist = [Lion(), Snake(), Parrot()]
for obj in objlist:
    obj.sound()
    obj.move()