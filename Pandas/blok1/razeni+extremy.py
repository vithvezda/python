import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00"],
    "napeti": [230, 255, 231, 260, 240],
    "proud": [120, 210, 180, 220, 195]
}

df = pd.DataFrame(data)

df_serazene = df.sort_values("napeti", ascending=False)
print(df_serazene)

index_max = df["napeti"].idxmax()
print("\nMaximální napětí:")
print(df.loc[index_max, ["cas", "napeti"]])

index_min = df["napeti"].idxmin()
print("\nMinimální napětí:")
print(df.loc[index_min, ["cas", "napeti"]])