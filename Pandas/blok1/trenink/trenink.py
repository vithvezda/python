import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00"],
    "napeti": [230, 235, 255, 260, 240, 250],
    "proud": [120, 150, 210, 220, 180, 205]
}

df = pd.DataFrame(data)

print("Úkol A")
print(f"Rozměry tabulky: {df.shape}")
print("Datové typy:")
print(df.dtypes)

df["vykon"] = df["napeti"] * df["proud"]

print(f"\nPrůměrné napětí: {df['napeti'].mean()} V")
print(f"Maximální proud: {df['proud'].max()} A")
print(f"Medián výkonu: {df['vykon'].median()} W")

print("\nÚkol B")
maska_prepeti = df["napeti"] > 253
maska_pretizeni = df["proud"] > 200

maska_problem = maska_prepeti | maska_pretizeni
maska_dva_problemy = maska_prepeti & maska_pretizeni

print("Přepětí:")
print(df[maska_prepeti])
print("\nPřetížení:")
print(df[maska_pretizeni])

print("\nProblematická měření:")
print(df[maska_problem])
print("\nPřepětí i přetížení:")
print(df[maska_dva_problemy])

print("\nÚkol C")
print(df.loc[maska_problem, ["cas", "napeti", "proud"]])
print(df.iloc[0:3, 0:2])