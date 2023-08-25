# 1. hello world
print("hello world")

# 2. Declaring variables and name conventions
variable = 1
this_is_a_variable = 2 
thisisavariable = 3 
thisIsAVariable = 4
another_variable = variable

print(variable)
print("variable")

# 3. Objects and their types 
x = "1"
print(type(x))
x = 1
print(type(x))
x = 1.0
print(type(x))
x = True
print(type(x))

x = "3.14"
print("x: ", x, "\ntype(x): ", type(x))

x = float(x)
print("x: ", x, "\ntype(x): ", type(x))

x = int(x)
print("x: ", x, "\ntype(x): ", type(x))

## 4. Example using types: Recording medical records
#first_name = input("What is your first name? ")
#surname = input("What is your surname? ")
#date_of_birth = input("What is your date of birth? ")
#
##age = 2023-date_of_birth
#age = 2023-int(date_of_birth)
#
#print("Your name is: ", first_name+surname) # concatenation 
#print("Your age is: ", age) # concatenation 
#
## 5. Write a similar program to input a height in feet and return height in m
## NB: m = feet*3.28
#height_feet = input("What is your height in feet? ")
#height_metres = float(height_feet)*3.28
#print("Your height in metres is: ", height_metres) 

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

# 7. Arithmetic operators

a = 10/3 # float 
print(a, type(a))

b = 10//3 # nearest integer
print(b, type(b))

c = 10%3 # integer remainder
print(c, type(c))

d = 10**3
print(d, type(d))

e = 10.0**3
print(e, type(e))

a = 2
b = a+1
print(b, type(b))
c = a+1.0
print(c, type(c))

d = c*a
print(d,type(d))
e=d-a
print(e,type(e))

a = 10+3*2
print(a)
b = 10 +   3*2
print(a-b)
c = 10+(3*2)
print(a-c)
d = (10+3)*2
print(d)

# 8. Logical operators 
a = 1==1
print(a, type(a))

a = 1.0==1
print(a, type(a))

b = 1!=1
print(b)

b = 1!=2
print(b)

c = 10>3
print(c)

d = 10<=20
print(d)

e = 10>3 and 10<=20
print(e)

f = 10>3 or 10<=20
print(f)

g = 10>3 and not 10<=20
print(g)

# 9. If statements 
stock_price = 10.1

if 0<=stock_price<=5:
    print("Stock is cheap. Buy it!!!") # note the indent - code gets ignored if boolean after if is False
elif 5<stock_price<=10: 
    print("Stock is neither cheap nor expensive. Hold it")
else: 
    print("Stock is expensive. Sell it!!!")

# 10. Write an if-elif-else statement that tells me to 
# I don't need a coat if the temperature is greater than 15 degrees 
# I do need a coat if the temperature is between 0 and 15 degrees 
# I shouldn't be outside at all in any other case (i.e., if the temperature is less than zero)
temperature = input("What is the temperature? ")
temperature = float(temperature)
t = temperature

if t>15:
    print("You won't need a coat, buddy!")
elif 0<=t<=15:
    print("You should probably bring a coat")
else: 
    print("Don't go outside at all, your coat isn't strong enough!!")


# 11. Exercise: Write a program that changes the score depending on which team scored. 

man_utd = 0
man_city = 0

scorer = input("Which team scored? Was it Manchester United or Manchester City or Neither? ")

if scorer.find("United") != -1:
    print(scorer.find("United"))
    man_utd = man_utd + 1
elif scorer.find("City") != -1:
    man_city = man_city + 1
else: 
    pass

print("The score is: " + "MUN " + str(man_utd) + "-" + str(man_city) + " MNC")

# 13. While loops 

i = 0
while i < 10:
    print(i)
    i = i+1


# 14. Exercise: Make it so we record the score once a minute:

man_utd = 0
man_city = 0


minute = 1

while minute <=10:
    scorer = input("Which team scored in minute " + str(minute) + "? Was it Manchester United or Manchester City or Neither? ")

    if scorer.find("United") != -1:
        print(scorer.find("United"))
        man_utd = man_utd + 1
    elif scorer.find("City") != -1:
        man_city = man_city + 1
    else: 
        pass
    
    print("In minute " + str(minute) +", the score was: " + "MUN " + str(man_utd) + "-" + str(man_city) + " MNC")
    minute = minute + 1



# 15. For loops 

for i in [1,2,3,4,5]:
    print(i)


names = ["ahmed", "bob", "chris"]
for i in range(len(names)):
    name = names[i] # indexing
    print("The name at position " + str(i) + " in the list is " + name)


for i,name in enumerate(names):
    print("The name at position " + str(i) + " in the list is " + name)


# 16. Exercise: Use a for loop to reconstruct the score code 

man_utd = 0
man_city = 0

minutes = range(9)

for i in range(10):
    minute = i + 1
    scorer = input("Which team scored in minute " + str(minute) + "? Was it Manchester United or Manchester City or Neither? ")

    if scorer.find("United") != -1:
        print(scorer.find("United"))
        man_utd = man_utd + 1
    elif scorer.find ("City") != -1:
        man_city = man_city + 1
    else: 
        pass
    
    print("In minute " + str(minute) +", the score was: " + "MUN " + str(man_utd) + "-" + str(man_city) + " MNC")
