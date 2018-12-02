import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph


def perform_clustering(X, connectivity, title, num_clusters, linkage='ward'):
    plt.figure()
    model = AgglomerativeClustering(linkage=linkage, connectivity=connectivity, n_clusters=num_clusters)
    model.fit(X)

    labels = model.labels_
    markers = '.vx'
    for i, marker in zip(range(num_clusters), markers):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], s=50, marker=marker, color='k', facecolors='none')
    plt.title(title)


def get_spiral(t, noise_amplitude=0.5):
    r = t
    x = r * np.cos(t)
    y = r * np.sin(t)

    return add_noise(x, y, noise_amplitude)
    # return x, y
    pass


def add_noise(x, y, amplitude):
    X = np.concatenate((x, y))
    X += amplitude * np.random.randn(2, X.shape[1])
    return X.T


def get_hypotrochoid(t, noise_amplitude=0):
    a, b, h = 10.0, 2.0, 4.0
    
    pass


if __name__ == '__main__':
    t = np.linspace(0, 10, 100)
    x = get_spiral(t)
    # plt.plot(*get_spiral(t))
    # plt.xlim(-10,10)
    # plt.ylim(-10,10)
    # plt.show()
    pass
