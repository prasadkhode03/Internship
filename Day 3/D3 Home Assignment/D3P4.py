# Part D: Expression Evaluation #
"""6.	Evaluate the following expressions:
print(5 + 3 * 2)
print((5 + 3) * 2)
print(10 - 3 ** 2 + 4)
print(100 // 3 % 2)
o	Write comments explaining why each output is as it is based on operator precedence."""

#Expression 1
print(5 + 3 * 2) 
#According to operator precedence, multiplication (*) has higher precedence than addition (+).
#So, 3 * 2 is evaluated first (3 * 2 = 6). Then, 5 + 6 = 11.
#Output: 11

#Expression 2
print((5 + 3) * 2)
#The parentheses override the default operator precedence, so (5 + 3) is evaluated first (5 + 3 = 8).
#Then, 8 * 2 = 16.
#Output: 16

#Expression 3
print(10 - 3 ** 2 + 4)
#According to operator precedence, exponentiation (**) has higher precedence than subtraction (-) and addition (+).
#So, 3 ** 2 is evaluated first (3 ** 2 = 9). 
#Then, 10 - 9 = 1,
#And finally 1 + 4 = 5.
#Output: 5

#Expression 4
print(100 // 3 % 2)
#According to operator precedence, both floor division (//) and modulus (%) have the same precedence and they are evaluated from left to right.
#So, 100 // 3 is evaluated first (100 // 3 = 33). 
#Then, 33 % 2 = 1
#Output: 1


"""7.	Write a small calculator program:
o	Ask user to enter two numbers and an operator (+, -, *, /)
o	Based on the operator, perform and display the result
Enter first number: 10
Enter second number: 5
Enter operator: *
Output: 10 * 5 = 50"""

#Asking user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

#Performing calculation based on operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Error: Invalid operator.")

#Displaying the result
print(f"{num1} {operator} {num2} = {result}")
