import numpy as np


def lcs(text1, text2):
    if not text1 or not text2:
        return ''
    result = np.zeros((len(text1) + 1, len(text2) + 1))

    for i in range(len(text1) + 1):

        for j in range(len(text2) + 1):
            if text1
                pass
    pass


if __name__ == '__main__':
    print(lcs('this is the first line', 'this is the second line'))
    pass
