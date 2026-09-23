import numpy as np

# ukol 1
print("Úkol 1")
napeti = np.array([229, 231, 255, 260, 240])
napeti_kv = napeti / 1000
napeti_zvysene = napeti + 5
napeti_mocnina = napeti ** 2

print(napeti_kv)
print(napeti_zvysene)
print(napeti_mocnina)

# ukol 2
print("\nÚkol 2")
U = np.array([230, 231, 229, 232])
I = np.array([10, 12, 8, 15])
cosfi = np.array([0.92, 0.95, 0.88, 0.97])

vykony = U * I * cosfi
prumerny_vykon = np.mean(vykony)
max_vykon = np.max(vykony)
print(vykony)
print(f"Průměrný výkon je {prumerny_vykon} W")
print(f"Maximální výkon je {max_vykon} W")

# ukol 3
print("\nÚkol 3")
zdanlive_vykony = U * I
cosfi_vyp = vykony / zdanlive_vykony
print(cosfi_vyp) # rovnají se