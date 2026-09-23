proudy = [120, 135, 210, 180, 95, 220, 160]

suma = 0
max_proud = 0
pocet_pretizeni=0

for hodnota in proudy:
    suma += hodnota

    if hodnota > max_proud:
            max_proud = hodnota
    
    if hodnota > 200:
            pocet_pretizeni += 1

prumer=suma/len(proudy)

    
print(f"Maximální proud: {max_proud} A")
print(f"Průměrný proud: {prumer} A")
print(f"Počet přetížení: {pocet_pretizeni}")
