from random import choice
moznosti=["kamen","nuzky","papir"]
pocitac=(choice(moznosti))
hrac=input("kamen, nuzky, papir, ted! ")
if hrac=="kamen" or "nuzky" or "papir":
    if (pocitac=="kamen" and hrac=="nuzky") or (pocitac=="nuzky" and hrac=="papir") or (pocitac=="papir" and hrac=="kamen"):
        print(pocitac," - vyhral jsem")
    elif pocitac==hrac:
        print(pocitac," - remiza")
    else:
        print(pocitac," - vyhral jsi")
else:
    print("napis to poradne priste")
