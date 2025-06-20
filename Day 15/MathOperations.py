'''Math Operations
Perform element-wise addition, subtraction, multiplication, and division between two arrays.
Perform power and square root operations.
Use np.sum(), np.mean(), np.min(), np.max(), and np.std().'''
import numpy as nm

arr1 = nm.arange(1, 11)
arr2 = nm.arange(11, 21)

# Perform element-wise addition, subtraction, multiplication, and division between two arrays.
# for i in range(len(arr1)):
#     print(arr1[i] + arr2[i])
print("Element-wise addition : ", arr1 + arr2)
print("Element-wise subtraction : ",arr1 - arr2)
print("Element-wise multiplication : ",arr1 * arr2)
print("Element-wise division : ",arr1 / arr2)

# Perform power and square root operations.
print("Element-wise power of 2 : ", nm.power(arr1, 2))
print("Square root of each element : ", nm.sqrt(arr1))

# Use np.sum(), np.mean(), np.min(), np.max(), and np.std().'
arr = nm.arange(1, 11)
print("Sum : ",nm.sum(arr))
print("Mean : ",nm.mean(arr))
print("Minimum : ",nm.min(arr))
print("Maximum : ",nm.max(arr))
print("Standard Deviation : ",nm.std(arr))



