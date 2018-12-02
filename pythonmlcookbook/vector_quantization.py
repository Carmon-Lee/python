import argparse

import numpy as np
from scipy import misc
from sklearn import cluster
import matplotlib.pyplot as plt


def build_parser():
    parser = argparse.ArgumentParser(description='compress the image using clustering')
    parser.add_argument('--input-file', dest='input_file', required=True, help='input image')
    parser.add_argument('--num-bits', dest='num_bits', required=False, type=int,
                        help='input the number of bits used to represent each pixel')
    return parser


def compress_img(img, num_clusters):
    X = img.reshape((-1, 1))
    k_means = cluster.KMeans(n_clusters=num_clusters, n_init=4, random_state=5).fit(X)
    centroids, labels = k_means.cluster_centers_.squeeze(), k_means.labels_

    print('compressing image:')
    print('label shape', labels.shape)
    print('label max,min', np.max(labels), np.min(labels))
    print('centroids shape', centroids.shape)
    print(labels, centroids)

    # return np.choose(labels, centroids).reshape(img.shape)
    return np.array([centroids[i] for i in labels]).astype(np.int8).reshape(img.shape)


def plot_img(img, title):
    vmin = img.min()
    vmax = img.max()
    print(vmin, vmax)
    plt.figure()
    plt.title(title)
    plt.imshow(img, cmap='gray_r', vmin=vmin, vmax=vmax)
    plt.show()


if __name__ == '__main__':
    # args = build_parser().parse_args()
    # input_file = args.input_file
    input_file = './fig.jpg'
    # num_bits = args.num_bits
    num_bits = 4
    print(input_file, num_bits)

    if not 1 <= num_bits <= 8:
        raise TypeError('Number of bits should be within 0 and 8 bits')
    num_clusters = np.power(2, num_bits)
    compression_rate = round(100 * (8.0 - num_bits) / 8.0, 2)
    print('number of clusters:', num_clusters, 'compression_rate:', compression_rate)

    input_img = misc.imread(input_file, True).astype(np.uint8)
    plot_img(input_img, 'original image')

    compressed_img = compress_img(input_img, num_clusters)
    plot_img(compressed_img, 'compressed image')
