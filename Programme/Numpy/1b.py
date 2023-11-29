liste = [3, 1, 4, 1, 5, 9, 2]

def Summe(liste):
    summe = 0
    for i in liste:
        summe += i
    return summe

def Produkt(liste):
    produkt = 1
    for i in liste:
        produkt *= i
    return produkt

summe = Summe(liste)
produkt = Produkt(liste)

print("Summe:", summe)
print("Produkt:", produkt)