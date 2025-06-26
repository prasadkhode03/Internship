#🔹 Part F: Advanced NumPy Practice
'''11.	Create an array of 100 random numbers and:
o	Find the top 5 maximum numbers
o	Find the average
o	Find the indices of all numbers > 50'''
import numpy as np
arr = np.random.randint(1, 100, size = 100)
print(arr)
top5max = np.sort(arr)[-5:]
print("Top 5 maximum numbers : ", top5max)
average = np.average(arr)
print("Average of array : ", average)
indices = np.where(arr > 50)[0]
print("\nIndices of Numbers > 50:")
print(indices)


'''12.	Create a 5x5 array of random numbers between 10–100 and:
o	Find its transpose
o	Find the sum of its diagonal
o	Extract the diagonal elements'''
arr5x5 = np.random.randint(10, 100, (5,5))
print("\n5x5 array of random numbers : \n", arr5x5)
transposeArray = np.transpose(arr5x5)
print("\nTranspose array : \n", transposeArray)
diag = np.diagonal(transposeArray)
sum = np.sum(diag)
print("Sum of digonal : ", sum)
print("Diagonal : ", diag)






'''15.	Moving Averages:
o	Given an array of daily temperatures, write a NumPy script to compute a 3 day moving average.'''
