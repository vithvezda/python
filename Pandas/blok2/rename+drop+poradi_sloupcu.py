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

df = df.rename(columns={        # prejmenuje sloupce stary : novy
    "napeti" : "napeti_V",
    "proud" : "proud_A"
})

df["vykon_W"] = df["napeti_V"] * df["proud_A"]

df = df.drop(columns=["stav_proudu"])       # smaze sloupec

df = df[["cas", "napeti_V", "proud_A", "vykon_W", "stav_napeti"]]       # zmena poradi sloupcu

print(df)
print(df.columns)