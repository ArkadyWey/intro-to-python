# Write a Python program that accepts an integer n and computes the value of n+n^2+n^3.
# Example: 
# Sample value of n is 5
# Expected Result : 155

number_str = input("Please input an integer ")
number_int = int(number_str)
n = number_int # Make it easier to work with the number
result = n+n**2+n**3

print("When n={}, the result is n+n^2+n^3={}".format(n,result))