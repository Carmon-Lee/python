import random
import matplotlib.pyplot as plt


def gauss(num):
    count = 0
    for i in range(num):
        count += random.randint(0, 10)
    return count


def guass1(order):
    stat = {}
    for i in range(100000):
        temp = gauss(order)
        stat[temp] = stat.get(temp, 0) + 1
    print(stat)
    plt.scatter(stat.keys(), stat.values())
    plt.ylim((0, 10000))


if __name__ == "__main__":
    guass1(1)
    guass1(2)
    guass1(3)
    guass1(4)
    guass1(5)
    guass1(6)
    guass1(7)
    plt.show()