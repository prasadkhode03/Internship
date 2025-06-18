import mathops
def check_prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0:
        return "prime"
    else: 
        return "not prime"

def check_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

