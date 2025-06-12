#Write a program to print factorial of a number
def factorial(num):
    fact = i = 1
    while(i<=num):
        fact *= i
        i+=1
    return fact
    
    #OR

    """for i in range(1, num+1):
        fact *= i
    return fact"""
    
num = int(input("Enter a Number : "))
factNum = factorial(num)
print(f"Factorial of {num} is {factNum}")