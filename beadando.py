import random

szamok = [random.randint(10000, 99999) for i in range(500)]
print(szamok)

print("-"*50)


paros= len([szam for szam in szamok if szam % 2 == 0])
print("Ennyi páros szám van a listában:",paros)

print("-"*50)

paratlan= 0
for szam in szamok:
    if szam % 2 != 0:
        paratlan+= szam

        
print("A páratlan számok összege:", paratlan)

print("-"*50)
egykezdobetu=len([szam for szam in szamok if 10000< szam <19999])
print("A számok közül ennyi kezdődik Egyessel:",egykezdobetu)

kettokezdobetu=len([szam for szam in szamok if 20000< szam <29999])
print("A számok közül ennyi kezdődik Ketessel:",kettokezdobetu)

haromkezdobetu=len([szam for szam in szamok if 30000< szam <39999])
print("A számok közül ennyi kezdődik Hármassal:",haromkezdobetu)

negykezdobetu=len([szam for szam in szamok if 40000< szam <49999])
print("A számok közül ennyi kezdődik Négyessel:",negykezdobetu)

otkezdobetu=len([szam for szam in szamok if 50000< szam <59999])
print("A számok közül ennyi kezdődik Ötössel:",otkezdobetu)

hatkezdobetu=len([szam for szam in szamok if 60000< szam <69999])
print("A számok közül ennyi kezdődik Hatossal:",hatkezdobetu)

hetkezdobetu=len([szam for szam in szamok if 70000< szam <79999])
print("A számok közül ennyi kezdődik Hetessel:",hetkezdobetu)

nyolckezdobetu=len([szam for szam in szamok if 80000< szam <89999])
print("A számok közül ennyi kezdődik Nyolcassal:",nyolckezdobetu)

kilenckezdobetu=len([szam for szam in szamok if 90000< szam <99999])
print("A számok közül ennyi kezdődik Kilencessel:",kilenckezdobetu)


















#for szam in szamok:
 #   if 30000< szam <39999:
  #       print(szam)

#import random

#a=[random.randrange(10000,10500)for a in range ]

#print(a)
#szamok=list(range(999,100000))
 #random.shuffle[lista]
#print(lista[:500])

#for szamok in lista:
 #   if szamok % 2 == 0:
  #     print(szamok)



      
