import random

def vel(mettol, meddig,lepes=1):
    darab=((meddig-mettol)/lepes)//1 +1 +1
    if((meddig-mettol)/lepes)%1!=0:
        darab+=1

    eltolas=mettol


    szam=lepes*((random.random()*darab)//1)+eltolas

    return szam 

print(vel(0,10,0.1))

szamok=[]
for i range(10):
    szamok.append(vel(10 ,99))
