# Activity 2A - Convert iterative fibonacci() to recursive
# ITERATIVE
def itr_fibonacci(n):
    if n <= 1: 
        return
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# RECURSIVE
def rec_fibonacci(n):
    if n <= 1:
        return n
    return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)

# Time them!
import time
print("For value 6: ")
start = time.perf_counter()
rec_fibonacci(6)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 0.0004146999854128808

start = time.perf_counter()
itr_fibonacci(6)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 8

print("for value 18: ")
start = time.perf_counter()
rec_fibonacci(18)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 2584

start = time.perf_counter()
itr_fibonacci(18)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 2584

print("for value 18: ")
start = time.perf_counter()
rec_fibonacci(54)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 0.0006892000092193484

start = time.perf_counter()
itr_fibonacci(54)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 0.0004193000204395503