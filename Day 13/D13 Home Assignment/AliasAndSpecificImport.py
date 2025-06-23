#Part B: Alias and Specific Import
'''4.	Import the math module as m:
o	Use it to compute the log10 of 1000.'''
import math as m
print(f"log10 of 1000 : {m.log10(1000)}")


'''5.	From the random module:
o	Import only the choice function and use it to pick a random element from a list of names.'''
from random import choice
names = ["Prasad", "Nachiket", "Satvik", "Rutvik", "Tanmay", "Om", "Aditya", "Piyush"]
print(f"\nRandom name from the list : {choice(names)}")