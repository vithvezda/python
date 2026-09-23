import numpy as np

data = np.array([
    [230, 120],
    [235, 150],
    [255, 210],
    [260, 220],
    [240, 180]
])

print("Úkol 1")
print(np.shape(data)) # rozmer radky x sloupce
print(np.ndim(data)) # kolikarozmerne je to pole

print("\nÚkol 2")
napeti = data[:, 0]
proud = data[:, 1]

print(napeti)
print(proud)

print("\nÚkol 3")
vykon = napeti * proud
prumerny_vykon = np.mean(vykon)
max_vykon = np.max(vykon)

print(f"Průměrný výkon je {prumerny_vykon / 1000} kW")
print(f"Maximální výkon je {max_vykon / 1000} kW")

print("\nÚkol 4")

prepeti = data[napeti > 253, :]
print(prepeti)