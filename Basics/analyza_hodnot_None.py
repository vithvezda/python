def analyza_hodnot(seznam, limit):
    if not seznam:
        return None

    suma = sum(seznam)
    max_hodnota = max(seznam)
    pocet_pres_limit = 0
    for hodnota in seznam:
        if hodnota > limit:
            pocet_pres_limit += 1
    prumer = round(suma/len(seznam), 2)
    return prumer, max_hodnota, pocet_pres_limit

vysledek = analyza_hodnot([], 200)

print(vysledek)