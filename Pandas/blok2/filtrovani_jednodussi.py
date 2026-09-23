import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00"],
    "napeti": [230, 255, 231, 260, 240, 248],
    "proud": [120, 210, 180, 220, 195, 205]
}

df = pd.DataFrame(data)

filtr_napeti = df.query("napeti > 253")     # filtruje napeti jednoduchým zápisem

print("Měření s napětím nad 253 V:\n", df.query("napeti > 253"))
print("\nMěření s napětím nad 253 V a zároveň porudem nad 200:\n", df.query("napeti > 253 and proud > 200"))
print("\nMěření s napětím nad 253 V nebo porudem nad 200:\n", df.query("napeti > 253 or proud > 200"))
print("\nMěření s porudem od 180 do 210 včetně:\n", df.query("180 <= proud <= 210"))