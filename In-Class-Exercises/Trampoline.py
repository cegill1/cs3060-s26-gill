def trampoline(f, *args):
    while callable(f):
        f = f(*args)
        args = ()
    return f

def factorial(n, acc=1):
    if n <= 1:
        return acc
    return lambda: factorial(n - 1, n * acc)

print(trampoline(factorial, 5))