import json

with open("json\\mereni.json", "r") as f:
    mereni = json.load(f)

#ukol_1:

print(mereni)

soucet_napeti = 0
for slovnik in mereni:
    if slovnik['napeti'] > 253:
        print(f"Přepětí v čase {slovnik['cas']} - hodnota {slovnik['napeti']} V")
    soucet_napeti += slovnik['napeti']
prumer_napeti = soucet_napeti/len(mereni)

print(f"Průměrné napětí: {prumer_napeti} V")

#ukol_2 + ukol_3:

for slovnik in mereni:
    slovnik['vykon'] = slovnik['napeti'] * slovnik['proud']
    if slovnik['napeti'] > 253:
        slovnik['stav'] = "PŘEPĚTÍ"
    else:
        slovnik['stav'] = "OK"

print(mereni)