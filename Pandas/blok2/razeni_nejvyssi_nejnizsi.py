import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00"],
    "napeti": [230, 255, 231, 260, 240, 248],
    "proud": [120, 210, 180, 220, 195, 205]
}

df = pd.DataFrame(data)

df["vykon"] = df["napeti"] * df["proud"]

serazene_vykon = df.sort_values("vykon", ascending=False)

print("3 nejvyšší výkony:") 
print(df.nlargest(3, "vykon"))

print("\n2 nejnižší napětí:")
print(df.nsmallest(2, "napeti"))