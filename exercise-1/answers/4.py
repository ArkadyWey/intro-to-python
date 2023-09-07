# Write a Python program that accepts a sequence of 
# comma-separated numbers from the user and 
# generates a list and a tuple of those numbers. 

# Example: 
# Sample data : 3, 5, 7, 23
# Output :
# [3, 5, 7, 23]

# Hint: You will need to use:
# split, which is a method on lists. 
# a while loop
# type conversion
# pop, which is another method on lists. 
# append, which is another method on lists. 
# Google these!

numbers = input("Input some comma seprated numbers : ")
list_of_strs = numbers.split(",")
print('List of floats: ', list_of_strs)
print("The type of elements of the list is: ", type(list_of_strs[0]))

list_of_ints = []
while len(list_of_strs) != 0: # while the list is not empty
    number_string = list_of_strs.pop(0) # get the next float in the list
    number_int = int(number_string) # turn the float into an integer
    list_of_ints.append(number_int) # append the integer to a new list

print('List of integers: ', list_of_ints) # print the new list
print("The type of elements of the list is: ", type(list_of_ints[0]))
