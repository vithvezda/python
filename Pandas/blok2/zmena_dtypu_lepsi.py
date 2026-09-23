import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00"],
    "napeti": ["230", "255", "chyba", "260", "240"],
    "proud": ["120.5", "210", "180", "-", "195"]
}

df = pd.DataFrame(data)

print(df.dtypes)

df["napeti"] = pd.to_numeric(df["napeti"], errors="coerce")     # prevede jiny datovy typ na cislo, chyby nahradí NaN
df["proud"] = pd.to_numeric(df["proud"], errors="coerce")

pocet_chybejicich = df.isna().sum()
df_ciste = df.dropna()

print(pocet_chybejicich)

df_ciste["vykon"] = df_ciste["napeti"] * df_ciste["proud"]

print(df_ciste)