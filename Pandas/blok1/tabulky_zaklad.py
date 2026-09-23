import pandas as pd
import numpy as np

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00"],
    "napeti": [230, 235, 255, 260, 240],
    "proud": [120, 150, 210, 220, 180]
}

df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns)

df["vykon"] = df["napeti"] * df["proud"]

prumer_vykon = df["vykon"].mean()
max_vykon = df["vykon"].max()
print(f"Průměrný výkon: {prumer_vykon} W")
print(f"Maximální výkon: {max_vykon} W")

print("\nPřepětí")
print(df[df["napeti"] > 253])
print("\nPřetížení")
print(df[df["proud"] > 200])

print("\nTabulka se stavem")
df["stav"] = np.where(df["napeti"] > 253, "PŘEPĚTÍ", "OK")
print(df)