#Input from User
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print(f"Numbers Before Swapping : a = {a} and b = {b}")

#Swapping Code
c = a
a = b
b = c

print(f"Numbers After Swapping : a = {a} and b = {b}")