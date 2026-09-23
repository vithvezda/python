import pandas as pd

data = {
    "stanice": ["TS1", "TS1", "TS2", "TS3", "TS2", "TS4", "TS1"],
    "stav": ["OK", "OK", "PŘETÍŽENÍ", "OK", "PŘETÍŽENÍ", "PORUCHA", "OK"]
}

df = pd.DataFrame(data)

typy_stanic = df["stanice"].unique()        # vypise kazdou unikatni hodnotu
pocet_typu_stanic = df["stanice"].nunique()    # spocita pocet unikatnich hodnot 

print(typy_stanic)
print(f"\nPočet typů stanic: {pocet_typu_stanic}")

typy_stavu = df["stav"].unique()
pocet_typu_stavu = df["stav"].nunique()

print(typy_stavu)
print(f"\nPočet typů stavů: {pocet_typu_stavu}")

pocet_stavu = df["stav"].value_counts()
print(pocet_stavu)