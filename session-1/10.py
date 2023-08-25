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
