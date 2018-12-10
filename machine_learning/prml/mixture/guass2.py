import matplotlib.pyplot as plt
import numpy as np
import math


def gaussian(sigma, x, u):
    y = np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
    return y


# x = np.linspace(220, 230, 10000)
x = np.linspace(-200, 200, 10000)

plt.title('PDF in Horizontal Direction', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# axes = plt.subplot(111)
# axes.set_xticks([-800, -400, 0, 400, 800])
# axes.set_yticks([0, 0.001, 0.002, 0.0030])

compguass = 0.3 * gaussian(100, x, 100) + 0.7 * gaussian(50, x, 20)
plt.plot(x, compguass, "b-", linewidth=3)
plt.show()
