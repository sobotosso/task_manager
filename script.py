# Seznam ukolu
ukoly = []

# Funkce pro pridani noveho ukolu
def pridat_ukol():
    while True:
        nazev_ukolu = input("Zadejte název úkolu: ").strip()
        if nazev_ukolu == "":
            print("Zadal(a) jste prázdný název, zkuste to znovu.")
            continue

        popis_ukolu = input("Zadejte popis úkolu: ").strip()
        if popis_ukolu == "":
            print("Zadal(a) jste prázdný popis, zkuste to znovu.")
            continue

        ukoly.append({"nazev": nazev_ukolu, "popis": popis_ukolu})
        print(f"Úkol '{nazev_ukolu}' byl přidán.")
        break

# Funkce pro zobrazeni ulozenych ukolu
def zobrazit_ukoly():
    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for i in range(len(ukoly)):
            print(f"{i+1}. {ukoly[i]['nazev']} – {ukoly[i]['popis']}")

# Funkce pro odstraneni ulozeneho ukolu
def odstranit_ukol():
    if len(ukoly) == 0:
        print("Není co mazat – seznam je prázdný.")
        return

    zobrazit_ukoly()
    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if cislo < 1 or cislo > len(ukoly):
            print("Neplatné číslo úkolu.")
        else:
            odebrany = ukoly.pop(cislo - 1)
            print(f"Úkol '{odebrany['nazev']}' byl odstraněn.")
    except ValueError:
        print("Musíte zadat číslo.")

def hlavni_menu():
    while True:
        print("\nSprávce úkolů")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1–4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

# Spuštění programu
hlavni_menu()
