#🔹 Part B: Inspecting Arrays
'''3.	Given:
arr = np.arange(12).reshape(3, 4)
o	Print its shape, size, ndim, and dtype.'''
import numpy as np
arr = np.arange(12).reshape(3, 4)
print("Shape of array : ", arr.shape)
print("Size of array : ", arr.size)
print("Number of dimensions of array : ", arr.ndim)
print("Data type of the array : ", arr.dtype)

# 4.	Change the dtype of an array from float64 to int32.
array = np.array([10.23, 45.32, 56.32, 46.20, 63.30])
print("Data type of array before changing : ", array.dtype)
array = array.astype(np.int32)
print("Data type of array after changing : ", array.dtype)
