parosszamok = []

szam = 2  
while len(parosszamok) < 10:
    parosszamok.append(szam)
    szam += 2

print(f"Az első 10 páros szám: {parosszamok}")

#VAGY MÁS MEGOLDAS

paros_szam = list(range(2, 21, 2))

print(f"Az első 10 páros szám: {paros_szam}")





