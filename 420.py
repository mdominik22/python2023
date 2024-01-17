osztando = int(input("Irja be az osztandót:"))
oszto = int(input("Irja be az osztót:"))

hanyados = osztando // oszto
maradek = osztando % oszto

print("Hányados:", hanyados)

if maradek > 1:
    print("Maradék: Nagyobb mint 1")
else:
    print("Maradék:", maradek)


