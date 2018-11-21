import random

def cal_code(vec, k):
    lmin, lmax = min(vec), max(vec)
    gap = (lmax - lmin) / k
    codes = [int(lmin - 2 * gap)]
    codes.extend([int(gap / 2 + i * gap) for i in range(k)])
    codes.append(int(lmax + 2 * gap))
    # print('code:', codes)
    return codes


def encode(codes, vector):
    encodes_vec = [encode1(codes, i) for i in vector]
    return encodes_vec


def encode1(codes, number):
    abs_dist=[abs(i-number) for i in codes]
    index=0
    temp=2**30
    return codes[abs_dist.index(min(abs_dist))]


if __name__ == '__main__':

    vector = [random.randint(0,100) for i in range(30)]
    codes = cal_code(vector, 4)
    print('vector:',vector,'\ncodes:',codes)
    print('encoded:',encode(codes,vector))
