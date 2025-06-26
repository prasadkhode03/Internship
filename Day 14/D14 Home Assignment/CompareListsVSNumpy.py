'''13.	Compare Lists vs NumPy:
o	Create a Python list and a NumPy array of the same data.
o	Compare their memory usage using sys.getsizeof() and .nbytes.
o	Compare their performance for an operation like adding 1 to every element.'''
import numpy as np
import sys
import time
mylist = [10, 20, 30, 40, 50]
myarray = np.array([10, 20, 30, 40, 50])
size1 = sys.getsizeof(mylist)
size2 = sys.getsizeof(myarray)
# size2 = myarray.nbytes
print("Size of list : ", size1)
print("Size of array : ", size2)


start = time.time()
list_result = [x + 1 for x in mylist]
end = time.time()
print("\nList addition time:", end - start, "seconds")

start = time.time()
numpy_result = myarray + 1
end = time.time()
print("NumPy addition time:", end - start, "seconds")