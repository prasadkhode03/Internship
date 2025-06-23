#🔹 Part C: Creating and Using a Custom Module
'''6.	Create a file math_utils.py with these functions:
o	add(a, b) – returns the sum.
o	multiply(a, b) – returns the product.
o	is_even(n) – returns True if even.'''
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

'''8.	Modify math_utils.py:
o	Add a greet() function that takes a name and returns a greeting.
o	Import and test it in main.py.'''
def greet(name):
    print(f"Hello {name}, welcome to python programming.")



