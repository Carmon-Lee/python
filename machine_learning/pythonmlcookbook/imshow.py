import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import tensorflow as tf


def compress(clusters):
    kmeans = KMeans(init='k-means++', n_clusters=clusters, n_init=10)
    pixel = img.reshape((img.shape[0] * img.shape[1], img.shape[2]))
    kmeans.fit(pixel)
    cc = kmeans.cluster_centers_.astype(np.int16)
    label2 = kmeans.labels_.reshape((300, 450))
    output = [[cc[label2[i, j]] for j in range(450)] for i in range(300)]
    return output


if __name__ == '__main__':
    image = tf.image.decode_jpeg(tf.read_file('./fig.jpg'))
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        img = sess.run((image))

        output1 = compress(5)
        output2 = compress(10)
        output3 = compress(20)
        output4 = compress(40)

        plt.figure()
        plt.subplot(221)
        plt.imshow(output1)

        plt.subplot(222)
        plt.imshow(output2)

        plt.subplot(223)
        plt.imshow(output3)

        plt.subplot(224)
        plt.imshow(output4)
        plt.show()
