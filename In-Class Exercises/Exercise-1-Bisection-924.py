def f(x): 
    return x**3 - x - 2

def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2 # midpoint
        if f(c) == 0 or (b - a) / 2 < tol:
            return c # root found
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c # best guss after max iter

# Try it
root = bisection(1, 2)
print("Approx root: ", root)

# Turn into a while loop variant for funsies?
def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None
    
    while (max_iter > 0):
        c = (a + b) / 2 # midpoint
        if f(c) == 0 or (b - a) / 2 < tol:
            return c # root found
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        max_iter - 1
    return c # best guess
