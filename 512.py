print("Makarész Dominik")
print:("10B")
print("2024.01.13")

import math

while True:
    try:
        szam = float(input("Adjon meg egy számot (0 végjelig): "))
    except ValueError:
        print("Érvénytelen bemenet. Csak számokat adjon meg.")
        continue
    if szam ==0:
        print("Miért adnád meg ezt a számot? Adj meg másikat ami nem 0-val kezdődik!!")
        break
    if szam > 0:
        negyzetgyok = math.sqrt(szam)
        print(f"A(z) {szam} négyzetgyöke: {negyzetgyok}")
    else:
        print("Helytelen szám a számnak pozitívnak kell lennie.")

