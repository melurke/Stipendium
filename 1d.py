import numpy as np

X = np.random.randint(-10, 10, (5, 3))

print(X)
print("Summe gesamt:", X.sum())
print("Produkt gesamt:", X.prod())

for i in range(5):
    print(f"Summe der {i+1}. Zeile:", X[i].sum())
    print(f"Produkt der {i+1}. Zeile:", X[i].prod())

for i in range(3):
    print(f"Summe der {i+1}. Spalte:", X[:, i].sum())
    print(f"Produkt der {i+1}. Spalte:", X[:, i].prod())
