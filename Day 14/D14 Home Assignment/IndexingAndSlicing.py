#🔹 Part C: Indexing and Slicing
'''5.	Create an array:
arr = np.arange(1, 21).reshape(4, 5)
o	Print the first row.
o	Print the last column.
o	Slice the subarray of the first 2 rows and first 3 columns.'''

import numpy as np

arr = np.arange(1, 21).reshape(4, 5)

print("Original array : \n", arr)
print("\n\nFirst row : ", arr[0]) #OR arr[:1]
print("Last row : ", arr[3]) #OR arr[:-1]
print("First 2 rows and first 3 columns : \n", arr[:2, :3])