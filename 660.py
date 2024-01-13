karakterek = input("Adjon meg egy karaktersorozatot: ")

szamdarab = 0
for karakter in karakterek:
    if karakter >= '0' and karakter <= '9':
        szamdarab += 1

print(f"A megadott karaktersorozatban {szamdarab} db szám karakter van.")

