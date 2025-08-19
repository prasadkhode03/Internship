'''Calculator Class with Static Methods
Create a Calculator class:

add(a, b) — Static method

multiply(a, b) — Static method

is_even(number) — Static method

Test it: Call these methods without creating an object, like:

Calculator.add(5, 3)  # Returns 8'''

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
    @staticmethod
    def is_even(number):
        if number %2 == 0:
            return number

cal = Calculator()
print(cal.add(10,15))
print(cal.multiply(5,6))
print(cal.is_even(4))