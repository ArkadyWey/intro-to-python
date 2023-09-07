# Write a Python program to calculate the absolute  difference
# between a given number and the number 5. 
# If the result is greater than 10, 
# then return twice the difference, 
# if its not, then just return the number.]

# Hint: You will need to use 
# - abs(), which calculates the absolute value of a number
# - An if statement

number_to_check = int(input("Please input the number to check "))

difference = number_to_check - 5
difference_absolute = abs(difference)

if difference_absolute > 10:
    result = 2*difference_absolute
else:
    result = difference_absolute

print("The result is: {}".format(result)) # Note that format is an alternative  
                                        # inputting values to a string - look it up!