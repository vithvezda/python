import pandas as pd

data = {
    "kod": ["TS1_A", "TS2_B", "VED1_A", "TS3_C", "ROZ1_B", "TS4_A"],
    "vykon_kW": [120, 180, 250, 160, 300, 140]
}

df = pd.DataFrame(data)

maska_zacatek = df["kod"].str.startswith("TS")
maska_konec = df["kod"].str.endswith("_A")

maska_kombo = maska_zacatek & maska_konec
print(df[maska_kombo])