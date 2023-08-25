# 4. Example using types: Recording medical records
first_name = input("What is your first name? ")
surname = input("What is your surname? ")
date_of_birth = input("What is your date of birth? ")

#age = 2023-date_of_birth
age = 2023-int(date_of_birth)

print("Your name is: ", first_name+surname) # concatenation 
print("Your age is: ", age) # concatenation 
