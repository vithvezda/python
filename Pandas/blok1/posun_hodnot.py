import pandas as pd

data = {
    "napeti": [230, 231, 240, 238, 255]
}

df = pd.DataFrame(data)

df["zmena napeti"] = df["napeti"] - df["napeti"].shift(1) # df["napeti"].shift(1) vytvori hodnoty posunute o 1
print(df)
print("\n")

maska_zmena = df["zmena napeti"].abs() > 5
print(df[maska_zmena])