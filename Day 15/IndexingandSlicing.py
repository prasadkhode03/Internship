'''Indexing and Slicing
Extract the first 5 elements of an array.
Extract the last 3 elements.
Change every second element of an array.
Extract an element from a 2D array.
Slice a 2D array to get its first 2 rows and first 2 columns'''

import numpy as nm 

arr = nm.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Extract the first 5 elements of an array.
print(arr[:5])

# Extract the last 3 elements.
print(arr[-3:])

# Change every second element of an array.
arr[::2] = 25
print(arr)

# Extract an element from a 2D array.
arr2d = nm.array([[10, 20, 30],[40, 50, 60]])
print(arr2d[1][1])

# Slice a 2D array to get its first 2 rows and first 2 columns
print(arr2d[:2, :2])



