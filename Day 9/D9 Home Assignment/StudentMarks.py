'''10.	Student Marks
•	Create a dictionary marks with subjects as keys and marks out of 100 as values.
•	Calculate total marks and average.
•	Print a message based on average:
o	>90: Excellent
o	70–90: Good
o	<70: Needs Improvement'''

marks = {"python" : 98, "java" : 85, "c++" : 87}
values = list(marks.values())

total = 0

for i in range(len(values)):
    total += values[i]

average = total/len(marks.keys())
print(f"Total - {total}")
print(f"Average - {average}")

if average > 90:
    print("Excellent")
elif average >= 70 and average <= 90:
    print("Good")
elif average < 70 and average > 40:
    print("Need Improvement") 
else:
    print("Fail!")
