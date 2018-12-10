import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans


def gen_data(num_pts, pt1, pt2):
    pt1, pt2 = np.array(pt1).reshape(2, 1), np.array(pt2).reshape(2, 1)
    print('Number of points:', num_pts)
    print('point 1:', pt1)
    print('point 2:', pt2)

    rad1 = np.random.randn(num_pts)
    rad2 = np.random.randn(num_pts)
    theta1 = np.random.randn(num_pts) * 2 * np.pi
    theta2 = np.random.randn(num_pts) * 2 * np.pi

    [x1, y1] = pt1 + [rad1 * np.cos(theta1), rad1 * np.sin(theta1)]
    [x2, y2] = pt2 + [rad2 * np.cos(theta2), rad2 * np.sin(theta2)]
    return np.array([np.append(x1, x2), np.append(y1, y2)])
    # self.num_pts *= 2


if __name__ == '__main__':
    data = gen_data(40, (1, 2), (6, 5))
    plt.figure()
    plt.scatter(data[0], data[1], marker='o', edgecolors='k', s=30)
    xmin, xmax = min(data[0]) - 1, max(data[0]) + 1
    ymin, ymax = min(data[1]) - 1, max(data[1]) + 1
    # plt.xlim(xmin,xmax)
    # plt.ylim(ymin,ymax)
    # plt.show()
    x_ct, y_ct = np.meshgrid(np.arange(xmin, xmax, 0.01), np.arange(ymin, ymax, 0.01))

    kmeans = KMeans(init='k-means++', n_clusters=2, n_init=10)
    kmeans.fit(data.T)
    predicted_labels = kmeans.predict(np.c_[x_ct.ravel(), y_ct.ravel()])
    predicted_labels=predicted_labels.reshape(x_ct.shape)
    # plt.figure()
    plt.imshow(predicted_labels, interpolation='nearest', extent=(x_ct.min(),x_ct.max(),y_ct.min(),y_ct.max()),
               aspect='auto', origin='lower')

    centroids=kmeans.cluster_centers_
    plt.scatter(centroids[:,0],centroids[:,1],linewidths=10)
    plt.show()

    print(predicted_labels)
    pass
