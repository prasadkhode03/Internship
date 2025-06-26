#🔹 Part A: Creating NumPy Arrays
'''1.	Import NumPy and:
o	Create a 1D array with numbers from 1–10.
o	Create a 2D array of shape (3, 3) with numbers from 1–9.'''
import numpy
arr1D = numpy.arange(1, 11)
    #OR
# arr1D = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
print("1D array : ", arr1D)

arr2D = numpy.arange(1, 10).reshape(3, 3)
    #OR
# arr2D = numpy.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]] ) 
print("\n2D array : \n", arr2D)

'''2.	Create an array of:
o	All zeros (shape = (3, 3))
o	All ones (shape = (2, 5))
o	All random numbers (shape = (4,))'''
zero = numpy.zeros((3, 3))
print("\nZeros array : ", zero)
one = numpy.ones((2, 5))
print("\nOnes array : ", one)
random_numbers = numpy.random.randint(1, 10, (4, ))
print("4 random numbers : ", random_numbers)