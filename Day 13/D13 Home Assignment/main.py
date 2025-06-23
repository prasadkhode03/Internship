#7.	In a separate script (main.py), import math_utils and test all its functions.
import math_utils
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(f"\nSum of {num1} and {num2} is {math_utils.add(num1, num2)}")
print(f"\nProduct of {num1} and {num2} is {math_utils.multiply(num1, num2)}")
print(f"\nIs {num1} even? : {math_utils.is_even(num1)}")
print(f"\nIs {num2} even? : {math_utils.is_even(num2)}")

'''8.	Modify math_utils.py:
o	Add a greet() function that takes a name and returns a greeting.
o	Import and test it in main.py.'''
from math_utils import greet
name = input("\n\nWhat is your name? ")
greet(name)
