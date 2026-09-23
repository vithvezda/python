import elektro

R = elektro.odpor(230, 5)

P = elektro.vykon(230, 10, 0.92)

print(f"Odpor je {R} ohm.")
print(f"Výkon je {P} W")