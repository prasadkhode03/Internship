import math_utils

print("main.py is running")
result = math_utils.square(5)
print("Square from main:", result)






'''Create and Run a Utility Module
Step 1: Create a file math_utils.py
def square(n):
    return n * n

def cube(n):
    return n * n * n

if _name_ == "_main_":
    print("Testing square:", square(3))
    print("Testing cube:", cube(2))

Step 2: Create another file main.py
import math_utils

print("main.py is running")
result = math_utils.square(5)
print("Square from main:", result)

Task:

Run math_utils.py and observe the output.

Run main.py and observe what happens.'''