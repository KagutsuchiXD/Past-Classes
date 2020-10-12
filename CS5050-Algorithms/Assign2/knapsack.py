# All functions asked for in one file for easier testing purposes
from random import random, randint


def complexKnapsack(i, size1, size2, s, v):
    if size1 == 0:  # base case
        if size2 == 0:
            return 0
    if i == 0:  # if there are no items return 0
        return 0
    if s[i - 1] > size1:
        if s[i - 1] > size2:
            return complexKnapsack((i - 1), size1, size2, s, v)
        return max(v[i - 1] + complexKnapsack((i - 1), size1, size2 - s[i - 1], s, v),
                   complexKnapsack((i - 1), size1, size2, s, v))
    else:
        return max(v[i - 1] + complexKnapsack((i - 1), size1 - s[i - 1], size2, s, v),
                   complexKnapsack((i - 1), size1, size2, s, v))


def generator(N, aveSize):
    S = [randint(1, 2*aveSize) for _ in range(0, N + 1)]
    V = [random() for _ in range(0, N + 1)]
    return S, V


v1 = [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0]
s1 = [0, 10, 20, 30, 40, 50, 60]
K1 = 50
K2 = 50
n = len(v1)
cache = [[[None for k in range(K2 + 1)] for j in range(K1 + 1)] for i in range(n + 1)]


def memoizingKnapsack(i, size1, size2, s, v):
    if size1 == 0:
        if size2 == 0:
            return 0.0
    if i == 0:  # if there are no items return 0
        return 0.0

    if cache[i - 1][size1 - 1][size2 - 1] is not None:
        return cache[i - 1][size1 - 1][size2 - 1]

    if s[i - 1] > size1:
        if s[i - 1] > size2:
            cache[i - 1][size1 - 1][size2 - 1] = memoizingKnapsack((i - 1), size1, size2, s, v)
        else:
            cache[i - 1][size1 - 1][size2 - 1] = max(v[i - 1] + memoizingKnapsack((i - 1), size1, size2 - s[i - 1], s, v),
                                                     memoizingKnapsack((i - 1), size1, size2, s, v))
    else:
        cache[i - 1][size1 - 1][size2 - 1] = max(v[i - 1] + memoizingKnapsack((i - 1), size1 - s[i - 1], size2, s, v),
                                                 memoizingKnapsack((i - 1), size1, size2, s, v))

    return cache[i - 1][size1 - 1][size2 - 1]


print(memoizingKnapsack(n, K1, K2, s1, v1))


cache2 = [[[-1 for k in range(K2 + 1)] for j in range(K1 + 1)] for i in range(n + 1)]


def dpKnapsack(i, size1, size2, s, v):
    for k1 in range(size1 + 1):
        for k2 in range(size2 + 1):
            cache2[0][k1][k2] = 0.0
    for item in range(i):
        cache2[item][0][0] = 0.0

    for item in range(1, i + 1):
        for k1 in range(1, size1 + 1):
            for k2 in range(1, size2 + 1):
                if k1 < s[item]:
                    if k2 < s[item]:
                        cache2[item][size1][size2] = cache2[item - 1][k1][k2]
                    else:
                        cache2[item][size1][size2] = max(v[item] + cache2[item - 1][k1][k2 - s[item]],
                                                        cache2[item - 1][k1][k2])
                elif k2 < s[item]:
                    if k1 < s[item]:
                        cache2[item][size1][size2] = cache2[item - 1][k1][k2]
                    else:
                        cache2[item][size1][size2] = max(v[item] + cache2[item - 1][k1- s[item]][k2],
                                                        cache2[item - 1][k1][k2])
                else:
                    cache2[item][size1][size2] = max(v[item] + cache2[item - 1][k1 - s[item]][k2],
                                                    v[item] + cache2[item - 1][k1][k2 - s[item]],
                                                    cache2[item - 1][k1][k2])
    return cache2[i][size1][size2]


print(dpKnapsack(n, K1, K2, s1, v1))
