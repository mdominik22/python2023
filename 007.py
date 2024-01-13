print("Makarész Dominik")

print("2024.01.11")

a = 37
b = 42
c = 23
d = 76
e = 14
f = 98

print("  -----------")
print(f"  | {a} | {b} |")
print("  -----------")
print(f"  | {c} | {d} |")
print("  -----------")
print(f"  | {e} | {f} |")
print("  -----------")


#VAGY
print("Makarész Dominik")

print("2024.01.11")

tablazat= [
    [37, 42],
    [23, 76],
    [14, 98]
]

print("  -----------")
for row in tablazat:
    print(f"  | {row[0]:2} | {row[1]:2} |")
    print("  -----------")
