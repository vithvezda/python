def vytvor_report(prumer_napeti, max_napeti, prumer_proud, max_proud, pocet_prepeti, pocet_pretizeni, casy_prepeti, casy_pretizeni):
    print("=====REPORT=====\n")
    print(f"Průměrné napětí: {prumer_napeti} V")
    print(f"Maximální napětí: {max_napeti} V")
    print(f"\nPrůměrný proud: {prumer_proud} A")
    print(f"Maximální proud: {max_proud} A")
    print(f"\nPočet přepětí: {pocet_prepeti}")
    print(f"Počet přetížení: {pocet_pretizeni}")

    print("\nPřepětí:")
    for cas_prepeti in casy_prepeti:
        print(cas_prepeti)
    print("\nPřetížení:")
    for cas_pretizeni in casy_pretizeni:
        print(cas_pretizeni)

def analyza_hodnot(seznam, limit):
    suma = sum(seznam)
    max_hodnota = max(seznam)
    pocet_pres_limit = 0
    for hodnota in seznam:
        if hodnota > limit:
            pocet_pres_limit += 1
    prumer = round(suma/len(seznam), 2)
    return prumer, max_hodnota, pocet_pres_limit

def analyza_casu(cas, hodnoty, limit):
    casy_pres_limit = []
    for i in range(len(hodnoty)):
        if hodnoty[i] > limit:
            casy_pres_limit.append(cas[i]) 
    return casy_pres_limit


cas = []
napeti = []
proud = []

with open("trafostanice.txt", "r") as f:
    for radek in f:
        radek = radek.strip()
        cas_hodnota, napeti_hodnota, proud_hodnota = radek.split(",")

        if cas_hodnota != "cas":
            cas.append(cas_hodnota)
            napeti.append(int(napeti_hodnota))
            proud.append(int(proud_hodnota))

prumer_napeti, max_napeti, pocet_prepeti = analyza_hodnot(napeti, 253)
prumer_proud, max_proud, pocet_pretizeni = analyza_hodnot(proud, 200)

casy_prepeti = analyza_casu(cas, napeti, 253)
casy_pretizeni = analyza_casu(cas, proud, 200)


vytvor_report(prumer_napeti, max_napeti, prumer_proud, max_proud, pocet_prepeti, pocet_pretizeni, casy_prepeti, casy_pretizeni)