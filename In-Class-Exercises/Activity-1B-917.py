# Activity 1B
# RECURSIVE FIRST
def rec_factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    elif n == 0: # base case: factorial of 0 is 1
        return 1
    else: # Recursive case: n! = n * (n - 1)!
        return n * factorial(n - 1)

# ITERATIVE
def itr_factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result
print("For value 6: ")
start = time.perf_counter()
rec_factorial(6)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 0.00037850000080652535

start = time.perf_counter()
itr_factorial(6)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 0.00034309999318793416

print("for value 18: ")
start = time.perf_counter()
rec_factorial(18)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 0.00029090000316500664

start = time.perf_counter()
itr_factorial(18)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 0.0003677000058814883

print("For value 54: ")
start = time.perf_counter()
rec_factorial(54)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 0.0003378000110387802

start = time.perf_counter()
itr_factorial(54)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 0.0003630999999586493

print("For value 162: ")
start = time.perf_counter()
rec_factorial(162)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 0.0003203000233042985

start = time.perf_counter()
itr_factorial(162)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 0.00033389998134225607

print("For value 486: ")
start = time.perf_counter()
rec_factorial(486)
end = time.perf_counter()
print(f"{end - start}") # Recursive Result: 0.00044750000233761966

start = time.perf_counter()
itr_factorial(486)
end = time.perf_counter()
print(f"{end - start}") # Iterative Result: 0.0003763000131584704

