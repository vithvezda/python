mereni = [
    {"cas": "00:00", "napeti": 229, "proud": 120},
    {"cas": "01:00", "napeti": 255, "proud": 210},
    {"cas": "02:00", "napeti": 231, "proud": 180},
    {"cas": "03:00", "napeti": 260, "proud": 220}
]

soucet_napeti = 0
for zaznam in mereni:
    print(f"{zaznam["cas"]} - {zaznam["napeti"]} V")
    soucet_napeti += zaznam["napeti"]
for zaznam in mereni:
    if zaznam["napeti"] > 253:
        print(f"Přepětí v čase {zaznam["cas"]}: {zaznam["napeti"]} V")

prumer_napeti = soucet_napeti/len(mereni)
print(f"Průměrné napětí: {prumer_napeti} V")