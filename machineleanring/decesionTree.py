import numpy as np
from collections import Counter


class DecisionTree:
    def __init__(self, X, y):
        self.X, self.y = X, y
        pass

    def total_entropy(self):
        class_count = Counter(self.y)
        class_prob = {i: class_count[i] / sum(class_count.values()) for i in class_count.keys()}
        props = np.array(list(class_prob.values()))
        return -np.dot(props, np.log2(props))

    def rela_diff(self):
        
        pass


if __name__ == '__main__':
    dt = DecisionTree(np.array([['g', 'h', 't'],
                                ['r', 'h', 'r'],
                                ['g', 'l', 't'],
                                ['g', 'h', 'r'],
                                ['r', 'l', 't'],
                                ['g', 'l', 'r'],
                                ]),
                      np.array(['a', 'b', 'b', 'a', 'b', 'b']))
    print(dt.total_entropy())
