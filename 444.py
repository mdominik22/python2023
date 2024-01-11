import random

csoportok = ["írók", "olvasók", "szerelők", "kapcsolók", "rendelők"]

valasztott_csoport = random.choice(csoportok)

if valasztott_csoport == "írók":
    print("Te az írók csoportba tartozol.")
elif valasztott_csoport == "olvasók":
    print("Te az olvasók csoportba tartozol.")
elif valasztott_csoport == "szerelők":
    print("Te a szerelők csoportba tartozol.")
elif valasztott_csoport == "kapcsolók":
    print("Te a kapcsolók csoportba tartozol.")
elif valasztott_csoport == "rendelők":
    print("Te a rendelők csoportba tartozol.")
