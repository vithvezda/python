import pandas as pd

data = {
    "den": ["Po", "Po", "Út", "Út", "St", "St"],
    "napeti": [231, 234, 238, 236, 252, 256],
    "proud": [130, 145, 160, 155, 205, 215]
}

df = pd.DataFrame(data)

df["vykon"] = df["napeti"] * df["proud"]

prumerny_vykon_den = df.groupby("den")["vykon"].mean()
print("Průměrný výkon každý den")
print(prumerny_vykon_den)

statistiky_napeti_den = df.groupby("den")["napeti"].agg(["min", "max"])
print("\nMinimální a maximální napětí každý den")
print(statistiky_napeti_den)

prumerny_proud_den = df.groupby("den")["proud"].mean()
max_proud_index = prumerny_proud_den.idxmax()

print(f"\nNejvyšší průměrný proud byl v den {max_proud_index} s hodnotou {prumerny_proud_den.loc[max_proud_index]} A")

maska_problem = (df["napeti"] > 253) | (df["proud"] > 200)
print("\nProblematická měření")
print(df[maska_problem])