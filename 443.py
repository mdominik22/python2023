import random

gondoltszam = random.randint(0, 9)

while True:
    tippelj = int(input("Tippelj egy szamra 0 és 9 között: "))

    if tippelj == gondoltszam:
        print("Helyes")
        break
    else:
        print("Próbáld újra.")
