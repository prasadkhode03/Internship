#🔹 Part D: Array Operations
'''6.	Elementwise operations:
o	Create two arrays of the same shape (e.g., a = [[1,2],[3,4]], b = [[5,6],[7,8]])
o	Perform elementwise:
	Addition
	Subtraction
	Multiplication
	Division'''
import numpy as np
array1 = np.array([[10,20],[30,40]])
array2 = np.array([[50,60],[70,80]])
print("Element-wise Operations - ")
print("\nAddition : \n", array1 + array2)
print("\nSubtraction : \n", array1 - array2)
print("\nMulitiplication : \n", array1 * array2)
print("\nDivision : \n", array1 / array2)


'''7.	Find:
o	Sum of all elements
o	Min, max, and average of an array'''

print("\n\nSum of all elements : ", np.sum(array1))
print("Smallest number of an array : ", np.min(array1))
print("Largest number of an array : ", np.max(array1))
print("Average number of an array : ", np.mean(array1))


'''8.	Use NumPy to compute:
o	Square root of every element in an array
o	Square of every element in an array'''
print("\n\nSquare root of every element :\n", np.sqrt(array1))
print("\nSquare of every element : \n", np.square(array1))