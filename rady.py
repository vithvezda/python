from math import log10
def aritrada(poc,krok,mez):
    pocatek=poc
    s=poc
    m=mez
    k=krok
    while mez>poc:
        poc=poc+krok
        s=s+poc
    if poc>mez:
        s=s-poc
    else:
        s=s
    print(f"soucet je {s}, pocatek je {pocatek}, mez je {m}, krok je {k}")
    return(s)
aritrada(1,2,6)



# x=log10((aritrada(3,4,303))/aritrada(2,7,212))
# print(x)