import pandas as pd

data = {
    "hodina": [0, 0, 1, 1, 2, 2, 3, 3],
    "napeti": [230, 232, 235, 233, 255, 250, 260, 258],
    "proud": [120, 130, 150, 140, 210, 200, 220, 215]
}

df = pd.DataFrame(data)

prumery = df.groupby("hodina")["napeti"].mean()
maxima = df.groupby("hodina")["proud"].max()
print(prumery)
print("\n")
print(maxima)
print("\n")

statistiky_napeti = df.groupby("hodina")["napeti"].agg(["mean", "min", "max"])
print(statistiky_napeti)
print("\n")

df["vykon"] = df["napeti"] * df["proud"]
statistiky_vykon = df.groupby("hodina")["vykon"].agg(["mean", "max"])
print(statistiky_vykon)