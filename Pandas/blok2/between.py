import pandas as pd

data = {
    "cas": ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00"],
    "napeti": [230, 255, 231, 260, 240, 248],
    "proud": [120, 210, 180, 220, 195, 205]
}

df = pd.DataFrame(data)

print("Měření s napětím od 230 do 250 V:\n", df[df["napeti"].between(230, 250)])
print("\nMěření s proudem od 180 do 210 A:\n", df[df["proud"].between(180, 210)])

maska_podminky = (df["napeti"].between(230, 250)) & df["proud"].between(180, 210)

print("\nMěření s napětím od 230 do 250 V a proudem od 180 do 210 A:\n", df[maska_podminky])