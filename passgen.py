import secrets
import string

print("Passgen by Codestube\n©2023-2026 Codestube, @clarigeclara\nVersion 2.0.0\nhttps://github.com/ClarigeClara/Passgen \n")
print("Hier ist eine Liste mit 50 Passwort-Vorschlägen, die du verwenden kannst.\n")

us_chars = string.ascii_letters + string.digits + "!@#$%&*()_+=-[]{};:<>,./?" 
de_chars = us_chars + "äöüÄÖÜß§€"

def generate_list(name, char_set, length, count=50):
    print(f"\n{name} {length} Zeichen")
    print("-" * 75)
    for i in range(1, count + 1):
        # secrets.choice ist der Goldstandard für Krypto-Zufall
        passwd = "".join(secrets.choice(char_set) for _ in range(length))
        print(f"# {i:5}         {passwd}")


generate_list("Vorschlag Nr.   Passwörter mit", de_chars, 50)
generate_list("Vorschlag Nr.   Passwörter (US-ASCII) mit", us_chars, 50)
generate_list("Vorschlag Nr.   Passwörter mit", de_chars, 30)
generate_list("Vorschlag Nr.   Passwörter (US-ASCII) mit", us_chars, 30)
generate_list("Vorschlag Nr.   Passwörter mit", de_chars, 20)
generate_list("Vorschlag Nr.   Passwörter (US-ASCII) mit", us_chars, 20)