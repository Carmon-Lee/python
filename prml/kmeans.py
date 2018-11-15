import numpy as np
import matplotlib.pyplot as plt


class KMeans():

    def __init__(self, num_pts, pt1, pt2):
        self.num_pts = num_pts
        pt1, pt2 = np.array(pt1).reshape(2, 1), np.array(pt2).reshape(2, 1)
        print('Number of points:', num_pts)
        print('point 1:', pt1)
        print('point 2:', pt2)

        rad1 = np.random.randn(self.num_pts)
        rad2 = np.random.randn(self.num_pts)
        theta1 = np.random.randn(self.num_pts) * 2 * np.pi
        theta2 = np.random.randn(self.num_pts) * 2 * np.pi

        [x1, y1] = pt1 + [rad1 * np.cos(theta1), rad1 * np.sin(theta1)]
        [x2, y2] = pt2 + [rad2 * np.cos(theta2), rad2 * np.sin(theta2)]
        self.coordinate = np.array([np.append(x1, x2), np.append(y1, y2)])

    def gen_uk(self, k=2):
        np.random.shuffle(self.coordinate.T)
        cols=self.coordinate.shape[1]
        len_div = cols // k
        self.uk = np.empty((2, k))
        self.pt_labels = np.zeros(self.coordinate.shape, dtype=np.int8)
        for i in range(k):
            self.uk[:, i] = np.average(self.coordinate[:, i * len_div:(i + 1) * len_div], axis=1).T
            self.pt_labels[i, i * len_div:(i + 1) * len_div] = 1
        print('uk', self.uk)
        print('labels:', self.pt_labels)

    def plot_pts(self):
        print('plot the random data...')
        plt.scatter(*self.coordinate)
        plt.scatter(*self.uk)
        plt.show()

    def startEM(self):
        self.plot_pts()
        self.doMaginalization()
        self.doExpectation()

    def doMaginalization(self):
        num_clusters = self.uk.shape[0]
        dist = np.zeros((num_clusters, self.num_pts))

        pass

    def doExpectation(self):
        pass


if __name__ == '__main__':
    kmeans = KMeans(100, (0, 0), (20, 6))
    kmeans.gen_uk(2)
    kmeans.plot_pts()
    # kmeans.startEM()
    # kmeans.startEM()
