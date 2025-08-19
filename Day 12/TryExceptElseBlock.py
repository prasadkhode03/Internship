class Dog: # 'Dog' is the class name
    # Class attribute
    species = "Canis familiaris"

    # Constructor method to initialize object attributes
    def __init__(self, name, age):
        self.name = name # 'name' is an instance attribute
        self.age = age   # 'age' is an instance attribute

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
