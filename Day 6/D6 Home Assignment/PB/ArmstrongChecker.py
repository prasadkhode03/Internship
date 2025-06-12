#6.	Armstrong Number Checker
"""Function is_armstrong(n) returns True if number is an Armstrong number.
(e.g., 153 → 1³ + 5³ + 3³ = 153)"""

def is_armstrong(n):
    temp = n
    sum = 0
    digits = len(str(n))
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        power = digit ** digits
        sum = sum + power
    if sum == n:
        return True
    else:
        return False


# def is_armstrong(n):
#     for i in range (1, n):
#         temp = i
#         sum = 0
#         digits = len(str(i))
#         while temp > 0:
#             digit = temp % 10
#             temp = temp // 10
#             power = digit ** digits
#             sum = sum + power
#         if sum == i:
#             print(i)


number = int(input("Enter a Number : "))
print(is_armstrong(number))