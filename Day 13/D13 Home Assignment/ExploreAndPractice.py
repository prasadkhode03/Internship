#🔹 Part E: Explore and Practice
'''10.	Import the os module:
o	List all files in the current directory.
o	Get the current working directory.'''
import os 
current_direc = os.getcwd()
print("Files : ")
for item in os.listdir():
    if os.path.isfile(item):
        print(item)
print(f"\nCurrent Working Directory : {current_direc}\n")



'''11.	Import the sys module:
o	Print the version of Python (sys.version).
o	Print the command-line arguments (sys.argv).'''
import sys
print(f"Version of Python : {sys.version}")
print(f"Comman-line arguments : {sys.argv}")


'''12.	Import the statistics module:
o	Calculate the mean and median of the list [1, 2, 3, 4, 5, 100].'''
import statistics
mylist = [1, 2, 3, 4, 5, 100]
print(f"\nMean of list : {statistics.mean(mylist)}")
print(f"Median of list : {statistics.median(mylist)}")