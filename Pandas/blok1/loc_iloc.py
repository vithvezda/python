import pandas as pd
import numpy as np

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00"],
    "napeti": [230, 235, 255, 260, 240],
    "proud": [120, 150, 210, 220, 180]
}

df = pd.DataFrame(data)
df["stav"] = np.where(df["napeti"] > 253, "PŘEPĚTÍ", "OK")

print(df.loc[:, ["cas", "napeti"]]) # vybira pouze dane sloupce
print("\n")

print(df.iloc[0:3, 0:2]) # vybira presne pozice
print("\n")

print(df.loc[df["napeti"] > 253, ["cas", "napeti", "stav"]])