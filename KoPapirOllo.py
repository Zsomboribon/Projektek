import random
 
def ko_papir_ollo():
    print("--- Üdv a Kő-papír-olló játékban! ---")
    valasztasok = ["kő", "papír", "olló"]
    gep_valasztasa = random.choice(valasztasok)
    jatekos_valasztasa = input("Válassz (kő, papír, olló): ").lower()
    if jatekos_valasztasa not in valasztasok:
        print("Érvénytelen választás! Kérlek, a kő, papír vagy olló szavak egyikét add meg.")
        return
 
    print(f"A gép ezt választotta: {gep_valasztasa}")
    if jatekos_valasztasa == gep_valasztasa:
        print("Döntetlen!")
    elif (
        (jatekos_valasztasa == "kő" and gep_valasztasa == "olló") or
        (jatekos_valasztasa == "papír" and gep_valasztasa == "kő") or
        (jatekos_valasztasa == "olló" and gep_valasztasa == "papír")
    ):
        print("Nyertél!")
    else:
        print("A gép nyert!")
 
if __name__ == "__main__":
    ko_papir_ollo()
