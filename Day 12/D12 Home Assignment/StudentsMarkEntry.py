#🔹 Part D: Real-World Inspired Tasks
'''8. Student Marks Entry
o	Ask the user to enter a student’s mark (0–100).
o	If out of range, raise ValueError.
o	Catch the error and print "Invalid mark. Must be between 0 and 100."
'''
try:
    marks = int(input("Enter marks (0-100) : "))
    if marks < 0 or marks > 100:
        raise ValueError("Invalid mark. Must be between 0 and 100.")
except ValueError as e:
    print("Error :", e)
