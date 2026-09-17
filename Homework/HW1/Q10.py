# Write a program that:  
# 1. Stores a secret 2-digit vault code.  
# 2. Prompts the user for a guess (input, cast to int).  
# 3. If the guess is correct, print: Vault open! Code accepted. 
# 4. If the guess is wrong, prompt the user for a second guess. Repeat the same check.  
# 5. If that guess is also wrong, prompt the user for a third and final guess. Repeat the same check.  
# 6. If all three guesses fail, print: Vault locked. Too many failed attempts.

secretCode = int("16")

guess = int(input("Guess a two-digit vault code: "))

if guess == secretCode:
    print("Vault open! Code accepted.")
else:
    guess2 = int(input("Guess a second number: "))
    if guess2 == secretCode:
        print("Vault open! Code accepted.")
    else:
        guess3 = int(input("Guess a third number: "))
        if guess3 == secretCode:
            print("Vault open! Code accepted.")
        else:
            print("Vault locked. Too many failed attempts.")