# Write a python program containing a for loop 
# to count the number of times the number 1 appears in a given random 
# list of numbers 

# Hint: 
# Uncomment the folliwing code to generate a list of 1s and 0s:
# Try to understand how this works!

import random
number_list = [0]*random.randint(0,10) + [1]*random.randint(0,20) 
random.shuffle(number_list)
print(number_list)

length_of_list = len(number_list)
indices_to_check = range(length_of_list)
# Initiate numbers that will count the number of ones and zero we've found
zero_counter = 0
one_counter = 0
# Execute the counter
for index in indices_to_check:
    element_at_index = number_list[index] # Get the next number in the list_of_numbers
    if element_at_index == 0:
        zero_counter = zero_counter + 1
    elif element_at_index == 1:
        one_counter = one_counter + 1
    else: 
        raise Exception("The number was not 0 or 1...did you really supply a list that only contains 0 and 1?")

print("The number of zeros in the list is {}.".format(zero_counter))
print("The number of ones in the list is  {}".format(one_counter))
    

