num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

try:
    div = num1 / num2 
    print("Division : ", div)
except ZeroDivisionError:
    print("\nCannot divide a number by 0.")