import numpy as np

a = np.ones(10)
b = np.array([1] + [0] * 8 + [1])

X = np.array([a, b, b, b, b, b, b, b, b, a])
print(X)