#🔹 Part A: Importing Standard Modules

'''1.	Import the math module and:
o	Print the square root of 256.
o	Print the value of math.pi.'''
import math
print(f"Square root of 256 is {math.sqrt(256)}.")
print(f"Value of PI is {math.pi}")


'''2.	Import the random module:
o	Print a random integer between 1–100.'''
import random
print(f"\nRandom integer betn 1-100 : {random.randint(1, 101)}")



'''3.	Import the datetime module:
o	Print the current date and time.'''
import datetime
current = datetime.datetime.now()
print(f"\nCurrent date and time : {current}")