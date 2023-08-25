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