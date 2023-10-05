hosszúság=["mm","cm","dm","m","km"]
#a kövekezőbe (jobbra lévőbe) mennyi a váltószám
hosszváltás=[10,10,10,1000,1]

terület=["mm2","cm2","dm2","m2","km2"]
#a következőbe (jobbra lévőbe) mennyi a váltószám
területváltás=[100,100,100,1000000,1]
repeat="Igen"
while(repeat=="Igen"):
    #szam bekérés
    #szám ellenőrzés
    rossz=True
    while rossz:
        try:
            szam=float(input("Írj be egy számot:"))
            print(szam)
            rossz=False
        except:
            print("Ez nem jó!")
     


    #mértékegység bekérés
    rossz=True
    while rossz:
            mertekEgyseg=input("Kérem a mértékegységet: ")
            #mértékegység ellenőrzés, típus kiderítés
            if mertekEgyseg in hosszúság:
                rossz=False
            else:
                print("ismeretlen mértékegység: "+mertekEgyseg)
            
    #mértékegység2 bekérés
    rossz=True
    while rossz:
            mertekEgyseg2=input("Kérem a cél mértékegységet!: ")
            #mértékegység2 ellenőrzés, az 1. típusbol
            if mertekEgyseg2 in hosszúság:
                rossz=False
            else:
                print("ismeretlen mértékegység: "+mertekEgyseg2)

    #kiszámítás
    me1Index = hosszúság.index(mertekEgyseg)
    me2Index = hosszúság.index(mertekEgyseg2)
    #print(me1Index,me2Index)

    #print(hosszváltás[me1Index:me2Index])

    if me1Index<me2Index:
        szorzo=1
        for valto in (hosszváltás[me1Index:me2Index]):
            szorzo*=valto

        szam=szam/szorzo
    else:
        szorzo=1
        for valto in (hosszváltás[me2Index:me1Index]):
            szorzo*=valto

        szam=szam*szorzo

    #kiirás
    print(szam,mertekEgyseg2)
    #újra?

    repeat=input("Újra? (Igen/Nem)")




