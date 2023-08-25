# 15. Exercise: Use a for loop to reconstruct the score code 

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
