def oldal(hazszam):
    if hazszam%2:
        return True
    else:
        return False

while True:
    hazszam = int(input("Kérlek add meg a házszámot! "))
    if hazszam == "":
        break
    if oldal(hazszam):
        print(f"{hazszam} házszámú ház a jobb oldalon van.")
    else:
        print(f"{hazszam} házszámú ház a ball oldalon van.")  