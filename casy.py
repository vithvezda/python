print("zadej první čas")
h1=int(input("zadej hodiny: "))
m1=int(input("zadej minuty: "))
s1=int(input("zadej sekundy: "))
print("zadej druhy čas")
h2=int(input("zadej hodiny: "))
m2=int(input("zadej minuty: "))
s2=int(input("zadej sekundy: "))
print("zadej třetí čas")
h3=int(input("zadej hodiny: "))
m3=int(input("zadej minuty: "))
s3=int(input("zadej sekundy: "))
print("zadej čtvrtý čas")
h4=int(input("zadej hodiny: "))
m4=int(input("zadej minuty: "))
s4=int(input("zadej sekundy: "))
h=h1+h2+h3+h4
m=m1+m2+m3+m4
s=s1+s2+s3+s4
while s>=60:
    m=m+1
    s=s-60
while m>=60:
    h=h+1
    m=m-60
print(f"{h} h {m} m {s} s")