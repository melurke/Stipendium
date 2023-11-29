import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-2 * np.pi, 2 * np.pi, 256, endpoint=True)
F1 = np.sin(X**2)
F2 = X * np.sin(X)
# aktuelle Achsen werden zurückgeliefert,
# falls notwendig, werden sie erzeugt:
ax = plt.gca()
# der obere rechte Spine wird unsichtbar gemacht:
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# der untere Spine wird in Position y=0  gebracht:
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
# der linke Spine wird nach rechts zu x = 0 bewegt:
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
            [r"$-2\pi$", r"$-\pi$", r"$+\pi$", r"$+2\pi$"])
plt.yticks([-3, -1, 0, +1, 3])
plt.plot(X, F1)
plt.plot(X, F2)
plt.show()