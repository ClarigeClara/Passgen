import random

keygen = ["A", "a", "Ä", "ä", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "M", "m", "N", "n", "O", "o", "Ö", "ö", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "Ü", "ü", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "?", "$", "€", "%", "&"]
print("Passgen by Codestube\n©2023-2025 Codestube, @clarigeclara\nVersion 1.1.0\nhttps://github.com/ClarigeClara/Passgen \n")
print("Hier ist eine Liste mit 20 Passwort-Vorschlägen, die du verwenden kannst.\n")

print('''
Vorschlag Nr.   Passwörter mit 50 Zeichen
-------------------------------------------------------------------------''')
for i in range(1, 51):
    passwd = "".join(random.choices(keygen, k=50))
    print(f"# {i:5}         {passwd}")

print('''
Vorschlag Nr.   Passwörter mit 30 Zeichen
-------------------------------------------------------------------------''')
for i in range(1, 51):
    passwd = "".join(random.choices(keygen, k=30))
    print(f"# {i:5}         {passwd}")

print('''
Vorschlag Nr.   Passwörter mit 20 Zeichen
-------------------------------------------------------------------------''')
for i in range(1, 51):
    passwd = "".join(random.choices(keygen, k=20))
    print(f"# {i:5}         {passwd}")