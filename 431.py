nev = input("Dolgozó neve: ")
alapber = float(input("Alapbér: "))
juttatasok = float(input("Juttatás összege: "))
potlek = float(input("Nyelvi pótlék összege: "))

jovedelem = alapber + juttatasok + potlek

if jovedelem > 1000000:
    ado = 0.36
else:
    ado = 0.16

ado = jovedelem * ado

print(f"{nev} dolgozónak éves jövedelme: {jovedelem} Ft")
print(f"{nev} dolgozónak fizetendő adó: {ado} Ft")
