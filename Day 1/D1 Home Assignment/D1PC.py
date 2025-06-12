#🔹 Part C: User Input
'''4.	Write a program that asks the user for:
o	Their name
o	Their favorite color
Then prints a sentence using both inputs.
Example:
Enter your name: Riya
Enter your favorite color: Blue
Output: Hello Riya! Your favorite color is Blue.'''

#Asking user for name and favorite color
name = input("Enter your name: ")
color = input("Enter your favorite color: ")

#Printing a sentence using both inputs
print(f"Hello {name}!, Your favorite color is {color}")



'''5.	Create a simple greeting bot:
o	Ask the user for their name and time of day (Morning/Afternoon/Evening)
o	Print: “Good [Time], [Name]! Have a nice day.”'''

#Creating a simple bot
name = input("Enter your name : ")
time = input("Enter the time of day (Morning/Afternoon/Evening) : ")
print(f"Good {time}, {name}! Have a nice day.")

