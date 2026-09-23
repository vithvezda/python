import pandas as pd

data = {
    "cas": ["00:00", "00:15", "00:15", "00:30", "00:45", "00:45"],
    "napeti": [230, 232, 232, 235, 240, 241],
    "proud": [120, 125, 125, 130, 140, 142]
}

df = pd.DataFrame(data)

duplicitni_radky_maska = df.duplicated()
pocet_duplicit = duplicitni_radky_maska.sum()

print(f"Počet zcela duplicitních řádků: {pocet_duplicit}")
print("\nDuplicitní řádky:")
print(df[duplicitni_radky_maska])

df_ciste = df.drop_duplicates()
print("\nDataFrame bez duplicit:")
print(df_ciste)

pocet_duplicit_cas = df.duplicated("cas").sum()
print(f"\nPočet duplicit podle času: {pocet_duplicit_cas}")