import math

a=int(input("a:"))
b=int(input("b:"))

c=math.sqrt (a*b+b*b)
print(c)

for a in range(1,100):
    for b in range(a,100):
        c=math.sqrt (a*b+b*b)
        if c%1==0:
            if b-a>=10:
                print(a,b,int(c))

