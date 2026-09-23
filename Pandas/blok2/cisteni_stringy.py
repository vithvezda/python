import pandas as pd

data = {
    "stanice": [" ts1", "TS2 ", " ts3 ", "TS4", "ts5 "],
    "stav": [" ok ", "PORUCHA ", " prepeti", "OK", " porucha "]
}

df = pd.DataFrame(data)

df["stanice"] = df["stanice"].str.strip()
df["stanice"] = df["stanice"].str.upper()

df["stav"] = df["stav"].str.strip()
df["stav"] = df["stav"].str.upper()

print(df)

print(df["stanice"].value_counts())
print(df["stav"].value_counts())