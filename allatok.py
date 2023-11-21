def legkonnyebb():
    legkisebb=tomegek[0]
    for t in tomegek:
        if legkisebb>t:
            legkisebb=t

        return legkisebb

allatok=["majom","kenguru","csincsilla","elefant","vaddisznó","kutya","ló","macska","cápa","gepárd"]

tomegek=[]

tomegek=[12,2,3,4,5,6,7,8,9,10]

for allat in allatok:
   tomegek.append(float(input("Milyen nehéz a "+allat+"(kg):")))

print(legkonnyebb())

if legkonnyebb() in tomegek:
    id=tomegek.index(legkonnyebb())
    print(allatok[id])

nehezek=[]

for i in range(tomegek)):
    

