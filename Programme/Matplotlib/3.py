from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = Symbol("x")
y = x**3 + 8*x**2 + 5*x + 8
y1 = y.diff(x)
y2 = y1.diff(x)

f = lambdify(x, y, "numpy")
f1 = lambdify(x, y1, "numpy")
f2 = lambdify(x, y2, "numpy")

x_a = np.arange(-2, 8, 0.1)

plt.plot(x_a, f(x_a), "k", label="f")
plt.plot(x_a, f1(x_a), "r", label="f'")
plt.plot(x_a, f2(x_a), "g", label="f''")
plt.legend(loc="best")
plt.show()