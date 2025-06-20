'''Creating Arrays
Create a 1D array of numbers from 1–10.
Create an array of 10 zeros.
Create an array of 5 ones.
Create an array of even numbers from 2–20.
Create an array with random numbers between 0 and 1.
Create an array of shape (3, 3) filled with the number 7.
Create an identity matrix of size 4x4.'''
import numpy as nm
import random as rd

# Create a 1D array of numbers from 1–10.
arr = nm.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)

# Create an array of 10 zeros.
zeros = nm.zeros((1, 10))
print(zeros)

# Create an array of 5 ones.
ones = nm.ones((1, 5))
print(ones)

# Create an array of even numbers from 2–20.
even_numbers = nm.arange(2, 21, 2)
print(even_numbers)

#Create an array with random numbers between 0 and 1.
random_numbers = nm.array([rd.random()])
print(random_numbers)

# Create an array of shape (3, 3) filled with the number 7.
arr = nm.array([[7,7,7], [7,7,7], [7,7,7]])
print(nm.shape(arr))

# Create an identity matrix of size 4x4.
identity = nm.eye(4)
print(identity)

