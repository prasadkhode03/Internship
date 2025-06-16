'''13.	Grades Lookup
•	Create a dictionary where keys are roll numbers and values are student names.
•	Ask user for a roll number and print the corresponding name.'''

student = {2 : "Aher", 13 : "Aditya", 16 : "Sachin", 19 : "Jayesh", 23 : "Prasad", 40 : "Piyush"}

roll_number = int(input("For which roll number are you looking for? : "))
print(f"Name of roll no.: {roll_number} is {student[roll_number]}")