from functools import cmp_to_key
import random
from operator import itemgetter


def asc_letter(first, second):
    for i, j in zip(first, second):
        if i == j:
            continue
        else:
            return ord(i) - ord(j)
    return len(first) - len(second)


if __name__ == '__main__':
    a = ['fdas', 'a', 'b', 'zuo']
    print(a)
    b = sorted(a, key=cmp_to_key(asc_letter))
    print(b)
