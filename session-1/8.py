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