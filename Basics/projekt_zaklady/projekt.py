import json

with open("projekt_zaklady\\mereni.json", "r") as f:
    mereni = json.load(f)

#doplneni sloupcu + vytvoreni pomocnych seznamu a seznamu problemu
napeti = []
proudy = []
vykony = []

casy_prepeti = []
hodnoty_prepeti = []
casy_pretizeni = []
hodnoty_pretizeni = []

for slovnik in mereni:
    slovnik['vykon'] = slovnik['napeti'] * slovnik['proud']

    if slovnik['napeti'] > 253:
        slovnik['stav_napeti'] = "PŘEPĚTÍ"
        casy_prepeti.append(slovnik['cas'])
        hodnoty_prepeti.append(slovnik['napeti'])
    else:
        slovnik['stav_napeti'] = "OK"

    if slovnik['proud'] > 200:
        slovnik['stav_proudu'] = "PŘETÍŽENÍ"
        casy_pretizeni.append(slovnik['cas'])
        hodnoty_pretizeni.append(slovnik['proud'])
    else:
        slovnik['stav_proudu'] = "OK"

    #pomocne seznamy
    napeti.append(slovnik['napeti'])
    proudy.append(slovnik['proud'])
    vykony.append(slovnik['vykon'])

#statistiky
prumerne_napeti = round(sum(napeti)/len(napeti), 2)
minimalni_napeti = min(napeti)
maximalni_napeti = max(napeti)
prumerny_proud = round(sum(proudy)/len(proudy), 2)
maximalni_proud = max(proudy)
prumerny_vykon = round(sum(vykony)/len(vykony), 2)


#vytvoreni reportu
print("================================")
print("REPORT TRAFOSTANICE")
print("================================")

print("\nNAPĚTÍ")
print(f"Průměr: {prumerne_napeti} V")
print(f"Minimum: {minimalni_napeti} V")
print(f"Maximux: {maximalni_napeti} V")
print(f"Přepětí: {len(casy_prepeti)}x")

print("\nPROUD")
print(f"Průměr: {prumerny_proud} A")
print(f"Maximux: {maximalni_proud} A")
print(f"Přetížení: {len(casy_pretizeni)}x")

print("\nVÝKON")
print(f"Průměr: {prumerny_vykon} W")
print("\n================================")

print("PROBLEMATICKÁ MĚŘENÍ")
print("\nPřepětí")
for cas,hodnota in zip(casy_prepeti, hodnoty_prepeti):
    print(f"{cas} - {hodnota} V")

print("\nPřetížení")
for cas,hodnota in zip(casy_pretizeni, hodnoty_pretizeni):
    print(f"{cas} - {hodnota} A")
