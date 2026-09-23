import numpy as np

data = np.array([
    [230, 120],
    [235, 150],
    [255, 210],
    [260, 220],
    [240, 180]
])

prumery = np.mean(data, axis=0) # axis=0 -> prumery se pocitaji z kazdeho sloupce zvlast
maxima = np.max(data, axis=0) # axis=1 -> prumery se pocitaji pro kazdy radek zvlast
minima = np.min(data, axis=0)

print(prumery)
print(maxima)
print(minima)