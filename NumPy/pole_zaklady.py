import numpy as np

proudy = np.array([120, 145, 210, 95, 220, 180, 205])
# ukol 1
print("úkol 1")
prumerny_proud = round(np.mean(proudy), 2)
min_proud = np.min(proudy)
max_proud = np.max(proudy)


print(f"Průměrný proud: {prumerny_proud} A")
print(f"Minimální proud: {min_proud} A")
print(f"Maximální proud: {max_proud} A")

# ukol 2
print("\núkol 2")

pretizeni = proudy[proudy > 200]
print(pretizeni)

# ukol 3
print("\núkol 3")

U = np.array([229, 231, 255, 260])
I = np.array([120, 140, 210, 220])

P = U * I
print(P)
prumerny_vykon = np.mean(P)
max_vykon = np.max(P)

print(f"Průměrný výkon je: {prumerny_vykon * 0.001} kW")
print(f"Maximální výkon je {max_vykon * 0.001} kW")