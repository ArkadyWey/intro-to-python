# Write a Python program to print whether a number is 
# within the range [0,100] or (100,1000] or (1000, 2000].

# Hint: 
# Use if, elif, and else!

a = 1

if 0<=a<=100:
    statement_to_make = "Number {} is within [0,100]".format(a)
elif 100<a<=1000:
    statement_to_make = "Number {} is within [100,1000]".format(a)
elif 1000<a<=2000:
    statement_to_make = "Number {} is within (1000,2000]".format(a)
else: 
    statement_to_make = "Number {} is not within any of the ranges".format(a)

print(statement_to_make)
