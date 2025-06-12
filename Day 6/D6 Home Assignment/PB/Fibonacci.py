#7.	Fibonacci Generator
'''Function fibonacci(n) returns a list of first n Fibonacci numbers.
Example: fibonacci(5) → [0, 1, 1, 2, 3]'''

def fibonacci(n):
    a = 0
    b = c = 1
    print("0 1 1", end = " ")     # 0 + 1 = 1 + 1 = 2 + 1 = 3 + 2 = 6 + 3 = 9.....
    for i in range(n):      #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
        a = b
        b = c
        c = a + b
        print(c, end = " ")

number = int(input("Enter a Number : "))
fibonacci(number)

