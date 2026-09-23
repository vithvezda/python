casy = ["00:00", "01:00", "02:00", "03:00"]
vykony = [850, 1200, 3100, 4200]

for cas_hodnota, vykon_hodnota in zip(casy, vykony):
    if vykon_hodnota > 3000:
        print(f"Překročení výkonu v čase {cas_hodnota}")