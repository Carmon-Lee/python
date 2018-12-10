import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    theta = np.linspace(np.pi, 1.5 * np.pi, 1000000)
    x1 = 4 + 4 * np.cos(theta)
    y1 = 4 * np.sin(theta)

    y2 = 0.5 * x1 - 4

    y3 = np.hstack((y2[y2 < y1], y1[y1 < y2]))
    y4 = np.zeros(x1.shape) - 4

    area = np.dot((y3 - y4)[1:], x1[1:] - x1[:-1])
    print(area)
    plt.figure()
    plt.plot(x1, y3, x1, y4)
    plt.show()
