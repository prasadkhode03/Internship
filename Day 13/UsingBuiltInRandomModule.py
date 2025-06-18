'''random Module
Task: Write a dice simulator.
On each run, it should randomly print a number between 1 and 6.
Bonus: Ask the user if they want to roll again.
Functions to use: randint, choice'''

import random
choice = "y"
while choice != "n":
    print(f"Your dice is showing {random.randint(1, 6 + 1)}")
    choice = input("Do you want to roll again? (y/n) : ").lower()
print("Game finished.")
