#Use a function to implement menu driven for basic arithmetic operations
#Take two numbers and the operator from the user as a input
def ArithmeticOperations(num1, num2, ope):
    if(ope == '+'):
        result = num1 + num2
    elif(ope == '-'):
        result = num1 - num2
    elif(ope == '*'):
        result = num1 * num2
    elif(ope == '/'):
        result = num1 / num2
    elif(ope == "//"):
        result = num1 // num2
    elif(ope == '%'):
        result = num1 % num2
    elif(ope == "**"):
        result = num1 ** num2
    else:
        print("Invalid Input!")
    return result

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
ope = input("Enter the Operator (+, -, *, /, //, %, **) : ")

print(f"Output : {ArithmeticOperations(num1, num2, ope)}")