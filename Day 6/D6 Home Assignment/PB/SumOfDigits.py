#🔹 Part B: Math Logic
'''5.	Sum of Digits
Function sum_of_digits(n) returns the sum of all digits in a number.
Example: 123 → 6'''

def sum_of_digits(n):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        sum = sum + digit 
    return sum

number = int(input("Enter a Number : "))
print(sum_of_digits(number))
