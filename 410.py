szam1 = float(input("Adj meg egy számot: "))

szam2 = float(input("Adj meg még egy számot: "))

if szam1 > szam2:
    nagyszam = szam1
    kisszam = szam2
else:
    nagyszam = szam2
    kisszam = szam1

if kisszam != 0:
    hanyados = nagyszam / kisszam
    print(f"{hanyados}")

