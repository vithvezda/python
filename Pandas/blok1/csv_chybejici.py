import pandas as pd

df = pd.read_csv("blok1\\mereni_chybejici.csv")

print(df.head())
print("\n")

print(df.isna().sum()) # spocita pocet chybejicich hodnot v kazdem sloupci

df_ciste = df.dropna()

print(f"Původní shape: {df.shape}")
print(f"Nový shape: {df_ciste.shape}")
print("\n")

df_ciste["vykon"] = df_ciste["napeti"] * df_ciste["proud"]
maska_problem = (df_ciste["napeti"] > 253) | (df_ciste["proud"] > 200)

print(df_ciste[maska_problem])