#🔹 Part B: If-Elif-Else
"""3.	Ask the user to enter marks (0–100) and display grade:
o	90–100: Grade A
o	75–89: Grade B
o	50–74: Grade C
o	Below 50: Fail"""

#Ask the user to enter marks 
marks = int(input("Enter Marks (0-100) : "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=50 and marks<=74:
    print("Grade B")
elif marks<50:
    print("Fail")
else:
    print("Invalid Input!")

"""4.	Take temperature as input and:
o	If temp > 35, print "Too Hot"
o	If 25–35, print "Normal Weather"
o	If 15–24, print "Cool"
o	Else, print "Too Cold" """

#Taking temperature as input
temp = int(input("Enter Temperature : "))
if temp > 35:
    print("Too Hot")
elif temp >= 25 and temp < 35:
    print("Normal Weather")
elif temp >= 15 and temp < 24:
    print("Cool")
else:
    print("Too Cold")
