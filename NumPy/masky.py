import numpy as np

data = np.array([
    [230, 120],
    [235, 150],
    [255, 210],
    [260, 220],
    [240, 180],
    [250, 205]
])

napeti = data[:, 0]
proud = data[:, 1]

# ukol 1
print("Úkol 1")
maska_pretizeni = proud > 200
print(maska_pretizeni)
print(data[maska_pretizeni, :])

#ukol 2
print("\nÚkol 2")
maska_problem = (napeti > 253) & (proud > 200)
print(data[maska_problem, :])

#ukol 3
print("\nÚkol 3")
maska_oboji = (napeti > 253) | (proud > 200)
print(data[maska_oboji, :])

#ukol 4
print("\nÚkol 4")
maska_prepeti = napeti > 253
pocet_prepeti = np.sum(maska_prepeti)
pocet_pretizeni = np.sum(maska_pretizeni)
bylo_prepeti = np.any(napeti > 253)
napeti_v_norme = np.all(napeti <= 253)

print(pocet_prepeti)
print(pocet_pretizeni)
print(bylo_prepeti)
print(napeti_v_norme)