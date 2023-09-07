# Write a Python program that calculates the area of a circle based on the radius entered by the user
# Hint: Use the input function we discussed in the session, and beware of types and conversions between them!


radius_string = input ("Input the radius of the circle please: ")
radius_float  = float(radius_string)
pi = 3.142

area_float = pi*radius_float**2

print ("The area of the circle with radius " + str(radius_float) + " is: " + str(area_float))