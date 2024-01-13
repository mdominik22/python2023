print("Makarész Dominik")
print:("10B")
print("2024.01.13")

import math

while True:
    try:
        szam = float(input("Adjon meg egy számot (0 végjelig): "))
    except ValueError:
        print("Ez nem szám, Csak számokat adjon meg.")
    if szam > 0:
        negyzetgyok = math.sqrt(szam)
        print(f"A(z) {szam} négyzetgyöke: {negyzetgyok}")
    else:
        print("Helytelen szám, a számnak pozitívnak kell lennie.")

