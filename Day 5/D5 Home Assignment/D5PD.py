#🔹 Part D: Patterns with Loops
'''8.	Print the following right-angle triangle pattern using a for loop:
*
***
*****
*******'''

for i in range (5+1):
    for j in range (i):
        print("*", end="")
    print()


#9. Take a number n as input and print a triangle with n rows using *.
n = int(input("Enter number of rows : "))
for i in range (n+1):
    for j in range (i):
        print("*", end="")
    print()