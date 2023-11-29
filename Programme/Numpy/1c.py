liste = []

numOfElements = int(input("Wie viele Elemente soll die Liste haben? "))

for i in range(numOfElements):
    liste.append(int(input(f"Was soll das {i+1}. Element sein? ")))

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