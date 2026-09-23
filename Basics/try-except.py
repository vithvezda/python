try:
    proud = float(input("Zadej proud (A): "))
    print(f"Zadaný proud je {proud} A")

except ValueError:
    print("Chyba: nezadal jsi číslo")