import pandas as pd

data = {
    "stanice": ["TS1", "TS2", "TS3", "TS4", "TS1", "TS3", "TS5"],
    "napeti": [230, 255, 240, 260, 235, 250, 245],
    "stav": ["OK", "PŘETÍŽENÍ", "OK", "PORUCHA", "OK", "PŘETÍŽENÍ", "OK"]
}

df = pd.DataFrame(data)

maska_stanice = df["stanice"].isin(["TS1", "TS3", "TS5"])
print(df[maska_stanice])
print("\n")

maska_stav = df["stav"].isin(["PŘETÍŽENÍ", "PORUCHA"])
print(df[maska_stav])
print("\n")

maska_stanice_napeti = (df["stanice"].isin(["TS1","TS2", "TS3"])) & (df["napeti"] > 240)
print(df[maska_stanice_napeti])