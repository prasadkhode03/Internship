'''math Module
Task: Create a program that:
Asks the user for a number.
Prints:
Square root of the number
Ceiling and floor values
Sine of the number (in radians)
Functions to use: sqrt, ceil, floor, sin'''

import math
num = float(input("Enter a number : "))
print(f"Square root of {num} is {math.sqrt(num)}")
print(f"Ceiling value of {num} is {math.ceil(num)}")
print(f"Floor value of {num} is {math.floor(num)}")
print(f"Sine of {num} is {math.sin(num)}")
