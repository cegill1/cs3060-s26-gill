# Immutability of Strings
s1 = "Rossum"
s1[2] = "a" # str doesn't support item assignment.
s1 = "Guido von"

# f-strings
price = 30
discount = 20
print("original price was", price, ", but after", discount, "% discount, it is now", price*(discount/100))
print(f"original price was {price}, but after {discount}% discount, it is now {price * (discount / 100)}")

# Printing
print(3)
print("a")
s1 = "Rossum"
print(s1)
print(s1, "Guido von," 13)

# Input
s0 = "Type your name:"
s1 = input(s0)

x = input("Type a number: ")    # If you enter 23...
y = x * 7     # y is assigned a str object, so it'll print 23 repeated 7 times.

x = int(input("Type a number: "))    # If you enter 23... Using type convesion...
y = x * 7     # y is assigned an int object, so it'll print the product of 23 and 7.

# In class Practice, evaluate T/F for each statement 
# (this pseudocode will not run directly)
cart_total = 120
is_member = True
has_coupon = False
# Free shipping if member AND cart over $50
is_member and (cart_total > 50) then print("Free shipping applied!") # true
# Discount if coupon OR total above $100
(has_coupon or (cart_total > 100)) then print("Discount applied!") # true
# If NOT member, suggest signup
(not is_member) then print("Sign up to save more!") # false 

# In-class exercise [Evaluated]
# Write a program that saves a secret number, asks the user for a number guess,
# and prints whether the guess is too low, too high, or same as the secret
secret_number = 21
guess = int(input("Guess the secret number: "))
if (guess < secret_number):
    print("Your guess is too low.")
elif (guess > secret_number):
    print("Your guess is too high.")
else:
    print(f"Congratulations! You guessed the secret number! It was {secret_number}.")

def factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    elif n == 0: # Base case: facotrial of 0 is 1
        return 1
    else: # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)