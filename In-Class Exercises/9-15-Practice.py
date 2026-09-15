def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

# It will throw RecursionError after 999 recursion calls.

# This will call itself infinitely bc there's no stopping condition
def countdown():
    countdown()

countdown()

# This also causes an error. 
n = 0
def countdown(n):
    print(n)
    n = n + 1;
    countdown(n)

countdown(n)

# Convert Newton-Raphson into recursive form pseudocode
def newtonRaphson(f, f', x0, tolerance e, max iterations N_max):
    # error case / base case
    if n <= 0:
        print "Derivative zero. no solution found"
        exit
    endif

    # Recursive case
    x_new <- x - f(x) / f'(x)
        
    if |x_new - x | < e then
        Print "Root found at", x_new
        Exit
    endif

    newtonRaphson(f, f', x_new, e, N_max, k + 1)