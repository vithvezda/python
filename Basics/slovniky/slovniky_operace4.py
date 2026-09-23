mereni = [
    {"cas": "00:00", "napeti": 229},
    {"cas": "01:00", "napeti": 255},
    {"cas": "02:00", "napeti": 231}
]

for slovnik in mereni:
    if slovnik["napeti"] > 253:
        slovnik["stav"] = "PŘEPĚTÍ"
    else:
        slovnik["stav"] = "OK"
    print(slovnik)
