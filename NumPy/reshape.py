import numpy as np

data = np.array([
    230, 120,
    235, 150,
    255, 210,
    260, 220
])

# ukol 1 + 2
print("Úkol 1 + 2")
print(np.shape(data))

tabulka = data.reshape(-1, 2)

print(np.shape(tabulka))

# ukol 3
print("\nÚkol 3")
napeti = tabulka[:, 0]
proud = tabulka[:, 1]

vykon = napeti * proud
print(vykon)
vykon_maska = vykon > 50000
vykon_over = vykon[vykon_maska]
print(vykon_over)
