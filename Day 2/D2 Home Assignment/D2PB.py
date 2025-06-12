#🔹 Part B: Type Conversion
"""3.	Take two numbers as input from the user and:
o	Convert them to integers
o	Add them and print the result
Example:
Enter first number: 10
Enter second number: 20
Output: The sum is 30"""

#Taking two numbers as input from the user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

#Converting them to integers
num1 = int(num1) 
num2 = int(num2)

#Adding them and printing the result
result = num1 + num2
print(f"The sum is {result}")


"""4.	Take a float input (like 98.6) and convert it to:
o	An integer
o	A string
Print all three formats."""

#Taking a float input
floatNum = float(input("Enter a Float Number : "))
intNum = int(floatNum) #Converted into integer
stringNum = str(floatNum) #Converted into string

#Printing all three formats
print(f"Float Format : {floatNum}")
print(f"Integer Format : {intNum}")
print(f"String Format : {stringNum}")
