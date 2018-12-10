import numpy as np
from collections import Counter

if __name__ == '__main__':
    x = np.random.randint(0, 2, 100000)
    c = Counter(x)
    px = [c[key] / len(x) for key in c.keys()]
    # probability of each class
    px = np.array(px)
    print(c, '\n', px)

    entropy = -np.dot(np.log2(px), px)/2
    gini = 1 - np.sum(px * px)
    print('half entropy:', entropy,'gini',gini)
