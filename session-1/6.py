# 6.  Object methods 

my_string = "thIs Is a sTring"
print(my_string)

my_string_upper = my_string.upper()
print(my_string_upper)

my_string_lower = my_string.lower()
print(my_string_lower)

my_string = my_string_lower
print(my_string)

a = my_string.find("s")
print(a)

my_new_string = my_string.replace("s","S")
print(my_new_string)

my_better_string = my_string.replace("string", "BETTER string")
print(my_better_string)
