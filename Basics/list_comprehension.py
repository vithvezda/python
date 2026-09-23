vykony = [850, 1200, 3100, 950, 4200]

pretizeni = [
    hodnota # co se ma ulozit
    for hodnota in vykony # prochazeni seznamu
    if hodnota > 1000 # podminka ulozeni
    ]
print(pretizeni)

odpory = [5, 12, 18, 24]

druha_mocnina = [
    hodnota ** 2 
    for hodnota in odpory
    ]
print(druha_mocnina)

casy = ["00:00", "01:00", "02:00", "03:00"]
napeti = [229, 255, 231, 260]

casy_prepeti = [
    cas_hodnota 
    for cas_hodnota, napeti_hodnota in zip(casy, napeti) 
    if napeti_hodnota > 253
    ]
print(casy_prepeti)