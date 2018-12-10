import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = (100 * np.random.rand(10)).astype(np.int16)
    y = x * x
    plt.scatter(x, y)

    xa = np.average(x)
    ya = np.average(y)
    plt.scatter(xa, ya, color='r')

    sizex = np.size(x)

    group = [np.tile(xa, np.size(x)), np.tile(ya, np.size(x))]
    groupx = [[i, j] for i, j in zip(group[0], x)]
    groupy = [[i, j] for i, j in zip(group[1], y)]

    for i in range(np.size(x)):
        plt.plot(groupx[i], groupy[i])
    print(group)
    plt.show()
    # print(x)
