import numpy as np

def analyza_pole(pole):
    prumer = np.mean(pole)
    minimum = np.min(pole)
    maximum = np.max(pole)
    return prumer, minimum, maximum

data = np.array([
    [230, 120],
    [235, 150],
    [255, 210],
    [260, 220],
    [240, 180],
    [250, 205],
    [228, 130],
    [256, 215]
])

# 1 
print(f"Tvar pole je: {np.shape(data)}")
print(f"Pole má {np.ndim(data)} dimenze")

# 1 - 6
napeti = data[:, 0]
proud = data[:, 1]
vykon = napeti * proud

prumer_napeti, min_napeti, max_napeti = analyza_pole(napeti)
prumer_proud, min_proud, max_proud = analyza_pole(proud)
prumer_vykon, min_vykon, max_vykon = analyza_pole(vykon)

print("\nNAPĚTÍ")
print(f"Průměr: {prumer_napeti} V\nMinimum: {min_napeti} V\nMaximum: {max_napeti} V")

print("\nPROUD")
print(f"Průměr: {prumer_proud} A\nMinimum: {min_proud} A\nMaximum: {max_proud} A")

print("\nVÝKON")
print(f"Průměr: {round(prumer_vykon / 1000, 2)} kW\nMinimum: {min_vykon / 1000} kW\nMaximum: {max_vykon / 1000} kW")

# 7 - 9
maska_prepeti = napeti > 253
maska_pretizeni = proud > 200

pocet_prepeti = np.sum(maska_prepeti)
pocet_pretizeni = np.sum(maska_pretizeni)

# 10 - 13
problematicka_mereni_or = maska_prepeti | pocet_pretizeni
problematicka_mereni_and = maska_prepeti & pocet_pretizeni

print("\nPřepětí nebo přetížení:")
print(data[problematicka_mereni_or, :])
print("\nPřepětí a přetížení:")
print(data[problematicka_mereni_and, :])

is_problem = np.any(maska_prepeti | pocet_pretizeni)
napeti_ok = np.all(napeti <= 253)
print(f"\nBylo problematické měření: {is_problem}")
print(f"Byla všechna napětí v normě: {napeti_ok}")