# Write a Python program to display the first and last colors from a list of colours.
# Example: 
# Input: color_list = "Red","Green","White" ,"Black"
# Output: Red, Black

colors = input("Input a set of colours (separated with a comma) please!")
colors_list = colors.split(",")

print("The list of colours that you have inputted is: ", colors_list)

color_first = colors_list[0] # indexing starts from zero in python - so the first element is indexed by zero
                             # which means that the ith element is indexed by i-1
color_last  = colors_list[-1] # we use -1 to index the  last item in a list

print("The first and last colours are: ", color_first, "and", color_last)

