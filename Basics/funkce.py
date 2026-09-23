def analyza_proudu(proudy):
    suma = 0
    max_proud = proudy[0]
    for hodnota in proudy:
        suma += hodnota

        if hodnota > max_proud:
            max_proud = hodnota
    
    prumer=suma/len(proudy)
    return prumer, max_proud

proudy = [120, 135, 210, 180, 95, 220, 160]

prumer, maximum = analyza_proudu(proudy)

print(prumer)
print(maximum)