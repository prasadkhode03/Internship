#Part B: Comparison Operators#
"""2.	Take age as input from the user and check if:
o	The person is 18 or older
o	The person is a senior citizen (>= 60)
"""

#Taking age as input from the user
age = int(input("Enter your Age : "))

#Checking the person is 18 or older
print(f"Is you are 18 or older? -> {age>=18}")

#Checking the person is a senior citizen (>= 60)
print(f"Is you are a Senior Citizen> -> {age>=60}")


"""3.	Take two numbers and check:
o	Which one is greater
o	Whether they are equal"""

#Taking two numbers
num1 = int(input("\n\nEnter First Number : "))
num2 = int(input("Enter Second Number : "))

#Checking which one is Greater
if(num1>num2):
    print(f"num1 = {num1} is Greater than num2 = {num2}")
else:
    print(f"num2 = {num2} is Greater than num1 = {num1}")

#Checking whether they are equal
print(f"\nIs {num1} and {num2} are equal? -> {num1==num2}")

