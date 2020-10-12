from random import random, randint


def generator(N, aveSize):
    S = [randint(1, 2*aveSize) for _ in range(0, N + 1)]
    V = [random() for _ in range(0, N + 1)]
    return S, V
