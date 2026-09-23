import pandas as pd
import numpy as np

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00"],
    "napeti": [230, 255, 231, 260, 240, 248],
    "proud": [120, 210, 180, 220, 195, 205]
}

df = pd.DataFrame(data)

df["stav_napeti"] = np.where(df["napeti"] > 253, "PŘEPĚTÍ", "OK")
df["stav_proudu"] = np.where(df["proud"] > 200, "PŘETÍŽENÍ", "OK")

stavy_napeti = df["stav_napeti"].value_counts()
stavy_proudu = df["stav_proudu"].value_counts()

stavy_napeti_podil = df["stav_napeti"].value_counts(normalize=True)
stavy_proudu_podil = df["stav_proudu"].value_counts(normalize=True)

print(stavy_napeti)
print(stavy_napeti_podil)
print(stavy_proudu)
print(stavy_proudu_podil)