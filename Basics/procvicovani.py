def analyza_proudu(proudy):
    suma = 0
    pocet_pretizeni = 0
    max_proud = proudy[0]
    
    for hodnota in proudy:
        suma += hodnota
        if hodnota > 200:
            pocet_pretizeni += 1
        if hodnota > max_proud:
            max_proud = hodnota
    prumer_proud = round(suma/len(proudy), 2)
    
    return prumer_proud, max_proud, pocet_pretizeni

proudy = [120, 145, 210, 95, 220, 180, 205]

prumerny, maximalni, pocet_pret = analyza_proudu(proudy)

print(f"Průměrný proud: {prumerny} A")
print(f"Maximální proud: {maximalni} A")
print(f"Počet přetížení: {pocet_pret}")

if pocet_pret > 1:
    print("VAROVÁNÍ: počet přetížení je větší než 1")