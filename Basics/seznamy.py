napeti = [229, 255, 231, 260, 240, 256]

for i in range(len(napeti)):
    if napeti[i]>253:
        print(f"Přepětí v měření {i}: {napeti[i]}")