from random import randint
body=0
while body<21:
    print("mas ",body," bodu")
    souhlas=input("chces vytahnout dalsi kartu? ano/ne ")
    if souhlas=="ne":
        break
    elif souhlas=="ano":
        karta=randint(2,10)
        body=body+karta
        print("vytahl jsi ",karta)
    else:
        print("neumis psat, s tebou nehraju")
if body==21:
    print("OKO\nmas 21 bodu")
elif body<=21:
    print("zbyvalo ",21-body," bodu")
else:
    print("mas ",body," bodu\nprohraaaaal")