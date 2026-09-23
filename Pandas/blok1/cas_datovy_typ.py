import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00"],
    "napeti": [230, 255, 231, 260, 240],
    "proud": [120, 210, 180, 220, 195]
}

df = pd.DataFrame(data)

df["cas"] = pd.to_datetime(df["cas"]) # zmeni cas ze stringu na datovy typ time

print(df.dtypes)

df["hodina"] = df["cas"].dt.hour

maska_cas = df["hodina"] >= 2
print(df.loc[maska_cas, ["cas", "napeti", "proud"]])