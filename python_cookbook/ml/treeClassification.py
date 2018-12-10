from math import log
import logging
from sklearn import linear_model
import numpy as np

def calShannonEntropy(dataSet):
    labelCount = {}
    totalCount = len(dataSet)
    logging.warning('The input dataSet is:{0!r},the length of which is:{1!r}'
                    .format(dataSet,totalCount))
    for dataRecord in dataSet:
        curLabel = dataRecord[-1]
        # print(curLabel)
        if curLabel not in labelCount.keys():
            labelCount[curLabel] = 0
        labelCount[curLabel] += 1
    print(labelCount)
    shannonEnt = 0
    for label in labelCount.keys():
        prob = float(labelCount[label] / totalCount)
        shannonEnt -= prob * log(prob,2)
    return shannonEnt


data = [[1, 2, 3, 'a'],
        [1, 2, 3, 'a'],
        [1, 2, 3, 'c'],
        [1, 2, 3, 'c'],
        [1, 2, 3, 'b'],
        [1, 2, 3, 'b'],
        [1, 2, 3, 'd']
        ]

shannonEnt=calShannonEntropy(data)
print('the shannon entropy is:{0!s}'.format(shannonEnt))

assert data