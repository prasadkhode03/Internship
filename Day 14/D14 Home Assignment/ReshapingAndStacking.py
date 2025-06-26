#🔹 Part E: Reshaping and Stacking
'''9.	Create a 1D array with numbers from 1–12 and:
o	Reshape it into a 3×4 array.
o	Flatten it back to a 1D array.'''
import numpy as np
arr1D = np.arange(1, 13)
print(f"Original Array : {arr1D}")
reshapedArray = arr1D.reshape(3, 4)
print(f"Reshaped Array : \n{reshapedArray}")
flattenArray = arr1D.flatten()
print(f"Flatten Array : {flattenArray}")


'''10.	Stack arrays:
o	Create a = [1, 2, 3] and b = [4, 5, 6]
o	Stack them vertically and horizontally.'''
a = np.stack([1, 2, 3])
b = np.stack([4, 5, 6])
verticalStack = np.vstack((a, b))
horizontalStack = np.hstack((a, b))
print(f"\nVertical Stack : \n{verticalStack}")
print(f"Horizontal Stack : \n{horizontalStack}")