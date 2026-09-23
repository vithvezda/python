napeti = []
time = []

with open("mereni.txt","r") as f:
   for radek in f:
      radek=radek.strip()
      cas, hodnota = radek.split(",")

      if cas != "cas":
         napeti.append(int(hodnota))
         time.append(cas)

print("Seznam napětí:")
print(napeti)
print("---------------------")

print("Seznam časů:")
print(time)
print("---------------------")

suma = 0
max_napeti = napeti[0]
pocet_prepeti = 0

for hodnota_napeti in napeti:
    suma += hodnota_napeti

    if hodnota_napeti > max_napeti:
        max_napeti = hodnota_napeti
    
    if hodnota_napeti > 253:
       pocet_prepeti += 1
prumer=round(suma/len(napeti), 2)

print(f"Průměr: {prumer}")
print(f"Maximum: {max_napeti}")
print(f"Počet přepětí: {pocet_prepeti}")
print("----------------------")

for i in range(len(napeti)):
   if napeti[i] > 253:
      print(f"Přepětí nastalo v čase: {time[i]}")