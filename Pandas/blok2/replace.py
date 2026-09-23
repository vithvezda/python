import pandas as pd

data = {
    "stanice": ["TS1", "TS2", "TS3", "TS4", "TS5", "TS6"],
    "stav": ["OK", "ok", "Porucha", "PORUCHA", "Ok", "chyba"]
}

df = pd.DataFrame(data)

df["stav"] = df["stav"].replace({
    "ok" : "OK",
    "Ok" : "OK",
    "Porucha" : "PORUCHA",
    "chyba" : "PORUCHA"
})

print(df)

print("\nPočet stavů:")
print(df["stav"].value_counts())