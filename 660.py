karaktersorozat = input("Adjon meg egy karaktersorozatot: ")

szamokdarabja = sum(1 for karakter in karaktersorozat if karakter.isdigit())

print(f"A megadott karaktersorozatban {szamokdarabja} db szám karakter van.")

print(70*"-")

karakterek = input("Adjon meg egy karaktersorozatot: ")

szamdarab = 0
for karakter in karakterek:
    if karakter >= '0' and karakter <= '9':
        szamdarab += 1

print(f"A megadott karaktersorozatban {szamdarab} db szám karakter van.")




