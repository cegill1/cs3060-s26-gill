# Write a program that:  
# 1. Asks the user for their age (input, cast to int).  
# 2. Asks the user whether the showing is a matinee, as "yes" or "no" (input, kept as a string).  
# 3. Determines the base ticket price using these rules:  
#  - Age under 13: $8.00  
#  - Age 13 to 64: $12.00  
#  - Age 65 or older: $9.00  
# 4. If the showing is a matinee (the user typed "yes"), subtract $2.00 from the base price.  
# 5. Prints a receipt using an f-string, in the form: "Ticket price: $<price>"  
# State what your program prints for age = 30 and matinee = "yes".  

age = int(input("What is your age in years: "))
matinee = str(input("Are you going to a matinee? ['yes' or 'no']: "))
priceTotal = 0

child = age < 13
senior = age > 65
adult = age > 13 and age < 65

if child and matinee:
    priceTotal = 8.00
elif child and not matinee:
    priceTotal = 6.00
if senior and matinee:
    priceTotal = 7.00
elif senior and not matinee:
    priceTotal = 9.00
if adult and matinee:
    priceTotal = 10.00
elif adult and not matinee: 
    priceTotal = 12.00 

print(f"Ticket price: ${priceTotal}")

# The program will print "Ticket price: $10.0" for inputs 30 and "yes".