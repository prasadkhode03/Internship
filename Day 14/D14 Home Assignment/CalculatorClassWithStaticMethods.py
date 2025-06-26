'''Calculator Class with Static Methods
Create a Calculator class:
add(a, b) — Static method
multiply(a, b) — Static method
is_even(number) — Static method
Test it: Call these methods without creating an object, like:
Calculator.add(5, 3)  # Returns 8'''
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

C1 = Calculator()
print(f"Addition of 74 and 56 is : {C1.add(74, 56)}")
print(f"Addition of 70 and 4 is : {C1.multiply(70, 4)}")
print(f"Is 5 is even number ? : {C1.is_even(5)} ")