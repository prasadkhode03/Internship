'''14.	Prime Numbers with NumPy:
o	Create an array of numbers from 1–100.
o	Use boolean masking to filter out only the prime numbers.'''
import numpy as np
arr = np.arange(1, 101)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

is_prime_vectorized = np.vectorize(is_prime)

prime_numbers = arr[is_prime_vectorized(arr)]
print(prime_numbers)
