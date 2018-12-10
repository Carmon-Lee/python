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
        self.num_pts *= 2

    def gen_uk(self, k=2):
        # np.random.shuffle(self.coordinate.T)
        cols = self.coordinate.shape[1]
        len_div = cols // k
        self.uk = np.empty((2, k))
        self.pt_labels = np.zeros(self.coordinate.shape, dtype=np.int8)
        for i in range(k):
            self.uk[:, i] = np.average(self.coordinate[:, i * len_div:(i + 1) * len_div], axis=1).T
            self.pt_labels[i, i * len_div:(i + 1) * len_div] = 1
        print('uk', self.uk)
        self.uk = np.array([[0, 8], [8, 0]])
        print('labels:', self.pt_labels)

    def plot_pts(self):
        print('plot the random data...')
        plt.scatter(self.coordinate[0][self.pt_labels[0]==1],self.coordinate[1][self.pt_labels[1]==0],color='y',marker=',')
        plt.scatter(self.coordinate[0][self.pt_labels[0]==0],self.coordinate[1][self.pt_labels[1]==1],color='g',marker=',')

        plt.scatter(self.uk[0][0],self.uk[1][0],color='r',marker='^')
        plt.scatter(self.uk[0][1],self.uk[1][1],color='b',marker='^')
        plt.show()

    def startEM(self):
        self.plot_pts()
        self.doMaginalization()
        self.doExpectation()

    def doMaginalization(self):
        num_clusters = self.uk.shape[0]

        self.pt_labels = np.zeros((num_clusters, self.num_pts), dtype=np.int8)
        pts = np.tile(self.coordinate, (num_clusters, 1))
        uks = np.tile(self.uk.T.reshape((1, num_clusters * 2)), (self.num_pts, 1)).T
        square = (pts - uks) ** 2
        sum_square = np.array([square[0, :] + square[1, :], square[2, :] + square[3, :]])
        self.pt_labels[sum_square < np.mean(sum_square, axis=0)] = 1
        print()

    def doExpectation(self):
        self.uk[:, 0] = [np.average(self.coordinate[0][self.pt_labels[0] == 1]),
                         np.average(self.coordinate[1][self.pt_labels[1] == 0])]
        self.uk[:, 1] = [np.average(self.coordinate[0][self.pt_labels[0] == 0]),
                         np.average(self.coordinate[1][self.pt_labels[1] == 1])]
        print()


if __name__ == '__main__':
    kmeans = KMeans(20, (0, 0), (5, 5))
    kmeans.gen_uk(2)
    # kmeans.plot_pts()
    kmeans.startEM()
    kmeans.startEM()
    kmeans.startEM()
    kmeans.startEM()
    kmeans.startEM()
    kmeans.startEM()
    kmeans.startEM()
