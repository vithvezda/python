mereni = {
    "cas": "12:00",
    "napeti": 231,
    "proud": 180
}

if "frekvence" in mereni:
    print(f"Frekvence: {mereni['frekvence']}")
else:
    print("Frekvence není k dispozici.")