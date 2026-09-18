# Iteration to Recursion Conversions
# Activity 1A
# Convert recursion-based factorial() to iterative
# RECURSIVE FIRST
def factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    elif n == 0: # base case: factorial of 0 is 1
        return 1
    else: # Recursive case: n! = n * (n - 1)!
        return n * factorial(n - 1)
factorial(4)

# ITERATIVE
def factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result

factorial(4)

# Timing Recursive Solutions
import time
def factorial(n):
        if n < 0:
            raise ValueError("Negative number!")
        elif n == 0: # base case: factorial of 0 is 1
            return 1
        else: # Recursive case: n! = n * (n - 1)!
            return n * factorial(n - 1)

n = 30
start = time.perf_counter()
factorial(n)
end = time.perf_counter()
print(f"{end - start}")


