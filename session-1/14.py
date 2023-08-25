# 14. For loops 

for i in [1,2,3,4,5]:
    print(i)


names = ["ahmed", "bob", "chris"]
for i in range(len(names)):
    name = names[i] # indexing
    print("The name at position " + str(i) + " in the list is " + name)


for i,name in enumerate(names):
    print("The name at position " + str(i) + " in the list is " + name)