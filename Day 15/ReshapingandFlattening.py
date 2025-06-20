'''Reshaping and Flattening
Create an array with numbers from 1–12 and reshape it into (3, 4).
Flatten the array back into a 1D array.'''
import numpy as nm

# Create an array with numbers from 1–12 and reshape it into (3, 4).
arr = nm.arange(1, 13)
reshaped_array = arr.reshape(3, 4)
print(reshaped_array)

# Flatten the array back into a 1D array.
flatten_array = reshaped_array.flatten()
print(flatten_array)