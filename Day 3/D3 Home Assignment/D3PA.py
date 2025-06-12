#🔹 Part A: Arithmetic Practice
"""1.	Take two numbers from the user and perform:
o	Addition
o	Subtraction
o	Multiplication
o	Division
o	Floor Division
o	Modulus
o	Exponentiation
Format your output nicely using f-strings.
Example:
print(f"Sum of {a} and {b} is {a+b}")"""

#Taking two numbers from the user
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("\nArithmetic Opertions")
print(f"\nSum of {a} and {b} is {a+b}") #Addition
print(f"Difference of {a} and {b} is {a-b}") #Subtraction
print(f"Multiplication of {a} and {b} is {a*b}") #Multiplication
print(f"Division of {a} and {b} is {a/b}") #Division
print(f"Floor Division of {a} and {b} is {a//b}") #Floor Division
print(f"Modulus of {a} and {b} is {a%b}") #Modulus
print(f"Exponentiation of {a} and {b} is {a**b}") #Exponentiation
