# Write a program that:  
# 1. Asks the user for their full name.  
# 2. Prints the first and last character. 
# 3. Prints the name reversed.  
# 4. Prints whether the name contains 'a'. 

name = str(input("Type your full name: "))

print(name[0] + " " + name[len(name) - 1])

print(name[::-1])

if 'a' in name:
    print(name + " contains 'a'")
    