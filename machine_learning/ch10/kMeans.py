from numpy import *


def load_data(filename):
    dataset = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            vals = line.strip().split('\t')
            vals=map(float, vals)
            dataset.append(vals)
    return dataset


def distEcld(vec1, vec2):
    return sqrt(sum(power(vec1 - vec2, 2)))


if __name__ == '__main__':
    matdata = load_data('./testSet.txt')
    print(distEcld(array(matdata[1]), array(matdata[2])))
