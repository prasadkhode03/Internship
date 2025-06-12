#🔹 Part C: Nested If
"""5.	Take a number as input. Check if it is:
o	Positive
	If yes, also check whether it is greater than 100 or not
o	Negative
o	Zero
Example Output:
Number is positive and greater than 100"""

#Taking a number as input
num = int(input("Enter a Number : "))
if num>0:
    print("Positive")
    if num>100:
        print("Number is positive and greater than 100")
elif num<0:
    print("Negative")
else:
    print("Zero")