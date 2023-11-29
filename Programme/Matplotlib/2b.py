import numpy as np
import matplotlib.pyplot as plt

x = range(0, 100)
y = np.random.randint(0, 100, 100)

mean = np.mean(y)
median = np.median(y)
std = np.std(y)

print(mean, median, std)

plt.plot(x, y, "k-", label="random numbers")
plt.plot(x, [mean] * 100, "b-", label="mean")
plt.plot(x, [median] * 100, "g-", label="median")
plt.plot(x, [mean + std] * 100, "r-", label="standard deviation")
plt.plot(x, [mean - std] * 100, "r-")
plt.legend(loc="best")

plt.show()