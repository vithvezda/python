import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00"],
    "napeti": [230, 235, 255, 260, 240, 250],
    "proud": [120, 150, 210, 220, 180, 205]
}

df = pd.DataFrame(data)

print("Úkol D")
max_napeti_index = df["napeti"].idxmax()
print(f"Maximum napětí nastalo v čase {df.loc[max_napeti_index, 'cas']} a mělo hodnotu {df.loc[max_napeti_index, 'napeti']} V")

min_napeti_index = df["napeti"].idxmin()
print(f"Minimum napětí nastalo v čase {df.loc[min_napeti_index, 'cas']} a mělo hodnotu {df.loc[min_napeti_index, 'napeti']} V")

print("\nÚkol E")
print(df.describe()) # count = pocet hodnot, mean = prumer, std = smerodatna odchylka, 50% = median