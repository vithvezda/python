vykony = [850, 1200, 3100, 950, 4200]

for index, hodnota in enumerate(vykony):
    if hodnota > 3000:
        print(f"Měření {index}: {hodnota} W - POZOR!")
    else:
        print(f"Měření {index}: {hodnota} W")
    
