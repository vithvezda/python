import pandas as pd

data = {
    "napeti": ["230", "255", "231", "260"],
    "proud": ["120.5", "210.0", "180.5", "220.0"]
}

df = pd.DataFrame(data)

print(df.dtypes)

df["napeti"] = df["napeti"].astype(int)     # prevod str na int
df["proud"] = df["proud"].astype(float)     # prevod str na float

df["vykon_W"] = df["napeti"] * df["proud"]

print(df.dtypes)
print(df)