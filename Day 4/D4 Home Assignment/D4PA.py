#🔹 Part A: Basic If/Else
"""1.	Ask the user for a number and:
o	Print "Even number" if divisible by 2
o	Otherwise, print "Odd number"
"""
#Asking the user for a number
num = int(input("Enter a Number : "))

#Checking if divisible by 2
if num%2==0:
    print("Even number")
else:
    print("Odd number")


"""2.	Ask the user to input age and check:
o	If age ≥ 18, print "Eligible to vote"
o	Else, print "Not eligible to vote"""

#Asking user to input age
age = int(input("Enter your age : "))

#Checking that age is greater or equal to 18
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")