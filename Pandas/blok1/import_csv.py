import pandas as pd

df = pd.read_csv("blok1\\mereni.csv")

print(df.head()) # vypise prvnich 5 radku
print(df.shape) # vypise rozmery
print(df.dtypes) # vypise formaty sloupcu
print("\n")
df.info()
print("\n")

df["vykon"] = df["napeti"] * df["proud"]
maska_problem = (df["napeti"] > 253) | (df["proud"] > 200)
print(df.loc[maska_problem, ["cas", "napeti", "proud", "vykon"]])