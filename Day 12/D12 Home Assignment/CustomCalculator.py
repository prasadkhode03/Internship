'''11.	Custom Calculator
•	Take two numbers and an operator as input.
•	Perform the calculation inside try.
•	Handle:
o	ZeroDivisionError
o	ValueError for bad input
o	Exception for invalid operators'''

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    operator = input("Enter an operator (+, -, *, /) : ")
    if operator == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operator == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        raise Exception("invalid operators")
except ZeroDivisionError:
    print(f"{num1} cannot be divided by zero.")
except ValueError:
    print("Bad Input.")
except Exception as e:
    print("Error : ", e)