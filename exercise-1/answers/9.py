# Write a Python program that determines whether each number 
# in a series of numbers separated by a comma 
# (accepted from the user) is even or odd, 
# and prints an appropriate message to the user.

# Hint: 
# Use if statements and a while loop. 
# You might also need len(), which calculates the length of a list, 
# and pop(), which gets the next element of a list.
# An alternative is to use a for loop instead of a while loop - these are very important, 
# look these up, or see the solutions 
# for an answer using a for loop.

numbers = input("Please input some whole numbers separated by commas \
and I will tell you if each one is odd or even")

numbers_list = numbers.split(",")

print(numbers_list)

while len(numbers_list) > 0: 
    number_str = numbers_list.pop(0)
    number_int = int(number_str)
    number_modulo_2 = number_int%2
    print("When the number is {} the number_modulo_2 is {}".format(number_int,number_modulo_2))
    if number_modulo_2 == 1:
        print("The number {} is odd.".format(number_int))
    elif number_modulo_2 == 0:
        print("The number {} is even.".format(number_int))
    else: 
        raise Exception("The number {} neither odd or even... are you sure you inputted a whole number?")

# An alternative solution using a for loop:
# You should see that in this case, a for loop was better since the code 
# was shorter.
numbers = input("Please input some whole numbers separated by commas \
and I will tell you if each one is odd or even")

numbers_list = numbers.split(",")

print(numbers_list)

for number_str in numbers_list: 
    number_int = int(number_str)
    number_modulo_2 = number_int%2
    print("When the number is {} the number_modulo_2 is {}".format(number_int,number_modulo_2))
    if number_modulo_2 == 1:
        print("The number {} is odd.".format(number_int))
    elif number_modulo_2 == 0:
        print("The number {} is even.".format(number_int))
    else: 
        raise Exception("The number {} neither odd or even... are you sure you inputted a whole number?")

