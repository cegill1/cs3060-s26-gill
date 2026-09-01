# Write code to calculate the area and circumference of a circle
pi = 22/7
radius = 4.15
areaCircle = pi * radius**2
circumferenceCircle = 2 * pi * radius

# Strings
s1 = "hello"
s2 = 'world'
s3 = """multiline"""
# Using other types (typecasting)
s1 = str(123) # '123'
# Concatentation using the '+' operator
s1 = "hello" + " world"
# Repetition using the '*' operator
s1 = "no"
s2 = s1*3

# Indexing & Slicing
s = "Python"
s[0] # "P"
s[-1] # "n"

# Membership testing; check if a substring exists:
"Py" in "Python" # True
"x" not in "Python" # True

# What's the value of s1 and s2?
x = "+"
c = "/"
s1 = "s" + x + 2*c
y = "a"
z = "b"
x = "2"
s2 = (y+z)*int(x)

# s1 = s+//
# s2 = abab

# Length of string
len(s1) # Length of s1

# Slicing
s1[2:5:1] # Pick the character from 2-5, and jump 1 step. It's similar to a for loop.
s1[2:5:2] # Pick the character from 2-5, and jump 2 steps. 

# Indices go both ways
s1[2:3] # s
s1[3:5] # su
s1[4:5] #u
s1[1:5:2] # os
s1[:] # Rossum, goes through the entire string
s1[:-2] # Ross, start at 0 and stop at -2, which is 'u'
s1[::-1] # mussoR, you can remove the :: in this. Telling you to start at 0 and step back -1. 
s1[1::-2] # o, start at index 1 and step back 2. 'o' because there is nothing at two letters back? We don't wrap to -1?
s1[0:len(s1):1] # Rossum