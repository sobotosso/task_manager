# Seznam pro ukládání úkolů
ukoly = []

def pridat_ukol():
    # Funkce umožní přidat nový úkol
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if nazev == "":
            print("Zadal(a) jste prázdný název, zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu: ").strip()
        if popis == "":
            print("Zadal(a) jste prázdný popis, zkuste to znovu.")
            continue

        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

def zobrazit_ukoly():
    # Funkce vypíše všechny uložené úkoly
    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for i in range(len(ukoly)):
            print(f"{i+1}. {ukoly[i]['nazev']} – {ukoly[i]['popis']}")

def odstranit_ukol():
    # Funkce odstraní úkol dle čísla
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
    # Hlavní řídicí nabídka celého programu
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
