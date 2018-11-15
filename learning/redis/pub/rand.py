import random
import tensorflow

def prob(oneprob=0.5):
    if random.random() > oneprob:
        return 0
    return 1


if __name__ == '__main__':
    first = 0
    output=[1]
    for i in range(1000000):
        if output[-1]==0:
            output.append(prob(oneprob=0.7))
        else:
            output.append(prob(oneprob=0.9))
    print(sum(output))
