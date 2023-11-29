import numpy as np
import matplotlib.pyplot as plt

def Mean(arr):
    mean = 0
    for x in arr:
        mean += x
    mean /= len(arr)
    return mean

def Median(arr):
    mArr = arr.copy()
    mArr.sort()
    if len(mArr) % 2 == 0:
        median = Mean([mArr[int(len(mArr)/2-1)], arr[int(len(mArr)/2)]])
    else:
        median = mArr[len(mArr)/2]
    return median

def StD(arr):
    mean = Mean(arr)
    s = 0
    for x in arr:
        s += (x - mean)**2
    s /= len(arr) - 1
    s = s**0.5
    return s

x = range(0, 100)
y = np.random.randint(0, 100, 100)

mean = Mean(y)
median = Median(y)
std = StD(y)

print(mean, median, std)

plt.plot(x, y, "k-", label="random numbers")
plt.plot(x, [mean] * 100, "b-", label="mean")
plt.plot(x, [median] * 100, "g-", label="median")
plt.plot(x, [mean + std] * 100, "r-", label="standard deviation")
plt.plot(x, [mean - std] * 100, "r-")
plt.legend(loc="best")

plt.show()