import pandas as pd

data = {
    "zarizeni": [
        "Transformator T1",
        "Vedeni V1",
        "transformator T2",
        "Rozvodna R1",
        "TRANSFORMATOR T3",
        "Vedeni V2"
    ],
    "napeti_kV": [22, 110, 22, 110, 35, 400]
}

df = pd.DataFrame(data)

maska_trafo = df["zarizeni"].str.contains("transformator", case=False)

maska_vedeni = df["zarizeni"].str.contains("Vedeni")

maska_trafo_napeti = (maska_trafo) & (df["napeti_kV"] >= 22)

print(df[maska_trafo_napeti])