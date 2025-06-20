'''Random Numbers
Create an array of 5 random numbers between 1–100.
Create a 3x3 array with random floats between 0–1.
Create a 4x4 array of random integers between 10–50.'''

import numpy as nm

# Create an array of 5 random numbers between 1–100.
random_number = nm.random.randint(1, 100, size=5)
print("Array of 5 random numbers betn 1 to 100 : ", random_number)

# Create a 3x3 array with random floats between 0–1.
arr3x3random = nm.random.rand(3, 3)
print("3x3 array with random floats betn 0 to 1 : ",arr3x3random)

# Create a 4x4 array of random integers between 10–50.
arr4x4random = nm.random.randint(10, 50, (4, 4))
print("4x4 array of random integers between 10 to 50 : ",arr4x4random)
