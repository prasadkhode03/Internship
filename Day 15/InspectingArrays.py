'''Inspecting Arrays
Create a sample array of float64
Find the shape, size, and dtype of an array.
Change the dtype of an array from float64 to int32.
Find the number of dimensions (ndim) of an array.'''
import numpy as nm

# Create a sample array of float64
float_array = nm.array([10.10, 20.10, 30.10, 40.10, 50.10], dtype=nm.float64)
print(float_array)

# Find the shape, size, and dtype of an array.
shape = nm.shape(float_array)
size = nm.size(float_array)
print(shape)
print(size)
print(float_array.dtype)

# Change the dtype of an array from float64 to int32.
float_array.dtype = nm.int32
print(float_array.dtype)
# Change the dtype from float64 to int32 using .astype()
arr = float_array.astype(nm.int32)
print(arr.dtype)

# Find the number of dimensions (ndim) of an array.
dimensions = nm.ndim(float_array)
print(dimensions)