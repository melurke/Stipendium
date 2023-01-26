import numpy as np

X = np.array([[1, 2, 3], [4, 5, 6]])
shape = X.shape

X = X.reshape((np.prod(shape)))
X = np.flipud(X)
X = X.reshape(shape)

print(X)