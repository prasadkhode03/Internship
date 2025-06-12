#Part B: While Loops

#4.	Print numbers from 10 to 1 using a while loop (reverse counting).
i = 10
while(i>=1):
    print(i)
    i-=1


#5.	Ask the user to enter a number, and keep asking until they enter a number greater than 100.
num = int(input("Enter a Number : "))
while(num<=100):
    num = int(input("Enter a Number : "))