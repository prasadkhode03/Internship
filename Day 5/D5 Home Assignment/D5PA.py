#🔹 Part A: For Loops

#1.	Write a program to print numbers from 1 to 10 using a for loop.
print("1 to 10 Numbers using for loop - ")
for i in range (1, 11):
    print(i)


# 2. Print all even numbers from 1 to 50.
print("All even numbers from 1 to 50 - ")
for i in range (1, 51):
    if i % 2 == 0:
        print(i)

# 3. Print the multiplication table of a number (user input).
print("Printing Multiplication Table - ")
num = int(input("Enter a Number : "))
for i in range(1, 11):
    print(f"{num} X {i} = {i * num}")

