import pandas as pd
import numpy as np

df = pd.read_csv("provozni_data_opakovani.csv")

print("Úkol 2")
print(df.head())
print(df.dtypes)

# Ukol 3
df = df.rename(columns={
    "Time" : "cas",
    "Station" : "stanice",
    "Voltage" : "napeti_V",
    "Current" : "proud_A",
    "Status" : "stav"
})

# Ukol 4
df["stanice"] = df["stanice"].str.strip()
df["stanice"] = df["stanice"].str.upper()

# Ukol 5
df["stav"] = df["stav"].str.strip()
df["stav"] = df["stav"].str.upper()

# Ukol 6
df["napeti_V"] = pd.to_numeric(df["napeti_V"], errors="coerce")
df["proud_A"] = pd.to_numeric(df["proud_A"], errors="coerce")

# Ukol 7
print("\nÚkol 7")
pocet_NaN = df.isna().sum().sum()
print(f"Počet NaN: {pocet_NaN}")

# Ukol 8
df_ciste = df.dropna().copy()

# Ukol 9
df_ciste["cas"] = pd.to_datetime(df_ciste["cas"])

# Ukol 10
df_ciste["vykon_W"] = df_ciste["napeti_V"] * df_ciste["proud_A"]

# Ukol 11
df_ciste["stav_napeti"] = np.where(df_ciste["napeti_V"] > 253, "PŘEPĚTÍ", "OK")
df_ciste["stav_proudu"] = np.where(df_ciste["proud_A"] > 200, "PŘETÍŽENÍ", "OK")

# Ukol 12
print("\nÚkol 12")
print("Počty stavů napětí:")
print(df_ciste["stav_napeti"].value_counts())
print("\nPočty stavů proudu:")
print(df_ciste["stav_proudu"].value_counts())

# Ukol 13
print("\nÚkol 13")
print("Měření s napětím > 253 V nebo proudem > 200 A:")
print(df_ciste.query("napeti_V > 253 or proud_A > 200"))

# Ukol 14
print("\nÚkol 14")
print("Stanice TS1 a TS3")

maska_stanice = df_ciste["stanice"].isin(["TS1", "TS3"])
print(df_ciste[maska_stanice])

# Ukol 15
print("\nÚkol 15")
print("3 nejvyšší výkony:")
print(df_ciste.nlargest(3, "vykon_W"))

print("\n2 nejnižší napětí:")
print(df_ciste.nsmallest(2, "napeti_V"))

# Ukol 16
print("\nÚkol 16")
print("Průměrný výkon každé stanice:")
prumery_stanic = df_ciste.groupby("stanice")["vykon_W"].mean()
print(prumery_stanic)

# Ukol 17
print("\nÚkol 17")
max_vykon_stanice_index = prumery_stanic.idxmax()
print(f"Nejvyšší průměrný výkon má stanice {max_vykon_stanice_index}, " 
      f"hodnota: {prumery_stanic.loc[max_vykon_stanice_index]} W")

# Ukol 18
print("\nÚkol 18")
df_ciste = df_ciste.set_index("cas")
hodinove_prumery = df_ciste[["napeti_V", "proud_A", "vykon_W"]].resample("1h").mean()
print("Hodinové průměry:")
print(hodinove_prumery)

#Ukol 19
print("\nÚkol 19")
maska_stanice_nazev = df_ciste["stanice"].str.startswith("TS")
print(f"Všechny stanice začínají písmeny TS: {np.all(maska_stanice_nazev)}")