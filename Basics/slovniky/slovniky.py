napeti = {
    "00:00": 229,
    "01:00": 231,
    "02:00": 255,
    "03:00": 260
}

print(napeti["02:00"])
print(napeti["03:00"])

for cas, hodnota in napeti.items():
    if hodnota > 253:
        print(cas)