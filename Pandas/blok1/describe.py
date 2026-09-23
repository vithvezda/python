import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00"],
    "napeti": [230, 255, 231, 260, 240],
    "proud": [120, 210, 180, 220, 195]
}

df = pd.DataFrame(data)

print("Statistický přehled")
print(df.describe()) # count = pocet hodnot, mean = prumer, std = smerodatna odchylka (jak moc jsou hodnoty rozptylene kolem prumeru) 50 % = median, polovina hodnotr je pod nim a polovina nad nim

df["vykon"] = df["napeti"] * df["proud"]
print("\nStatistický přehled")
print(df.describe())

med_napeti = df["napeti"].median()
std_napeti = df["napeti"].std()
print(f"\nMedián napětí: {med_napeti} V")
print(f"Směrodatná odchylka napětí: {std_napeti} V")