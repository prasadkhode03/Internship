'''Final Mini Project
Perform the following in one script:
Create a 5x5 array of random integers between 1–100.
Find the min, max, mean, and sum of the array.
Replace all numbers > 50 with -1.
Save the array to a .npy file.
Load it back and print the contents.'''
import numpy as nm

# Create a 5x5 array of random integers between 1–100.
arr5x5random = nm.random.randint(1, 100, (5, 5))

# Find the min, max, mean, and sum of the array.
print("5x5 array : ", arr5x5random)
print("\nMinimum : ", arr5x5random.min())
print("Maximum : ", arr5x5random.max())
print("Mean : ", arr5x5random.mean())
print("Sum : ", arr5x5random.sum())

# Replace all numbers > 50 with -1.
arr5x5random[arr5x5random>50] = -1
print(arr5x5random)

# Save the array to a .npy file.
nm.save("array.npy", arr5x5random)

# Load it back and print the contents.
content = nm.load("array.npy")
print(content)