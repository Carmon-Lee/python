import numpy as np
from collections import Counter

rules = {
    'equals': lambda x, y: x == y,
    'greater': lambda x, y: x > y
}


class DecisionTree:
    class Node:

        def __init__(self):
            pass

    def __init__(self, X, y):
        self.X, self.y = X, y
        self.c = Counter(y)
        self.pos_rule = (1, rules['greater'], 'a')
        self.neg_rule = (1, rules['greater'], 'a')

        self.rule = (0, rules['equals'], 'r')
        pass

    def make_decision(self, x):
        #   receive a feature input,and output the feature class

        pass

    def entropy(self, y):
        class_count = Counter(y)
        class_prob = {i: class_count[i] / sum(class_count.values()) for i in class_count.keys()}
        props = np.array(list(class_prob.values()))
        return -np.dot(props, np.log2(props))

    def gain(self, data, feature_index):
        features = data[:, feature_index]

        c = Counter(features)
        feature_set = c.keys()
        p_feature = {i: c[i] / sum(c.values()) for i in feature_set}
        # print(features,feature_set)
        print('feature probability:', p_feature)

        cond_entropy = 0
        for feature in feature_set:
            di = self.y[data[:, feature_index] == feature]
            print('Di:', di)
            cond_entropy += p_feature[feature] * self.entropy(di)
        return cond_entropy

    def max_cond_ent(self, x, y):
        feature_count = x.shape[1]
        print('feature count', feature_count)
        min_feature = []
        for i in range(feature_count):
            print('the {0}th feature gain is {1}'.format(i, self.gain(x, i)))
            min_feature.append(self.gain(x, i))
        return min_feature.index(min(min_feature))




if __name__ == '__main__':
    # https://blog.csdn.net/z962013489/article/details/80024574
    dt = DecisionTree(np.array([['g', 'h', 't'],
                                ['r', 'h', 'r'],
                                ['g', 'l', 't'],
                                ['g', 'h', 'r'],
                                ['r', 'l', 't'],
                                ['g', 'l', 'r'],
                                ]),
                      np.array(['a', 'b', 'b', 'a', 'b', 'b']))
    # print(dt.entropy(dt.y))
    # print(dt.gain(dt.X, 0))
    # print(dt.gain(dt.X, 1))
    # print(dt.gain(dt.X, 2))
    # print(dt.max_cond_ent(dt.X, dt.y))
    print(dt.make_decision('g'))
    print(dt.make_decision('r'))


