import pandas as pd

data = {
    "cas": [
        "2026-09-08 00:00",
        "2026-09-08 00:15",
        "2026-09-08 00:30",
        "2026-09-08 00:45",
        "2026-09-08 01:00",
        "2026-09-08 01:15",
        "2026-09-08 01:30",
        "2026-09-08 01:45"
    ],
    "napeti": [230, 232, 231, 233, 235, 234, 236, 233],
    "proud": [120, 125, 130, 135, 150, 145, 155, 140]
}

df = pd.DataFrame(data)

print("Úkol 1")
df["cas"] = pd.to_datetime(df["cas"]) 

df = df.set_index("cas") # nastavi cas jako index tabulky

print(df)

print("\nÚkol 2")
hodinove_prumery = df.resample("1h").mean()
print(hodinove_prumery)

print("\nÚkol 3")
hodinove_maxima = df.resample("1h").max()
print(hodinove_maxima)
