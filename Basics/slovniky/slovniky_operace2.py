trafostanice = {
    "nazev": "TR Ostrava",
    "napeti": 110,
    "vykon": 250,
    "v_provozu": True
}

trafostanice["frekvence"] = 50
trafostanice["vykon"] = 300

for klic, hodnota in trafostanice.items():
    print(f"{klic}: {hodnota}")