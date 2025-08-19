def factorial(n):
    if n == 0: # Base Case
        return 1
    else: # Recursive Step
        return n * factorial(n - 1) # Function calls itself

print(factorial(5))
