szam = int(input("Adj meg egy egész számot: "))

oszthatoketto = szam % 2 == 0
oszthatoharom = szam % 3 == 0

if oszthatoketto and oszthatoharom:
    print(f"A {szam} osztható 2-vel és 3-mal.")
elif oszthatoketto:
    print(f"A {szam} osztható 2-vel.")
elif oszthatoharom:
    print(f"A {szam} osztható 3-mal.")
else:
    print(f"A {szam} nem osztható semelyikkel")
