import matplotlib.pyplot as plt
from random import random, randint
import timeit


K1 = 50
K2 = 50
n = 10
ave_size = 20

cache = [[[None for k in range(K2 + 1)] for j in range(K1 + 1)] for i in range(n + 1)]


def generator(N, aveSize):
    S = [randint(1, 2*aveSize) for _ in range(0, N + 1)]
    V = [random() for _ in range(0, N + 1)]
    return S, V


def memoizingKnapsack(i, size1, size2, s, v):
    global cache
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

    value = cache[i - 1][size1 - 1][size2 - 1]

    cache = [[[None for k in range(K2 + 1)] for j in range(K1 + 1)] for i in range(n + 1)]
    return value


def dpKnapsack(i, size1, size2, s, v):
    cache1 = [[[-1.0 for k in range(K2 + 1)] for j in range(K1 + 1)] for i in range(n + 1)]

    for k1 in range(size1 + 1):
        for k2 in range(size2 + 1):
            cache1[0][k1][k2] = 0.0
    for item in range(i):
        cache1[item][0][0] = 0.0

    for item in range(1, i + 1):
        for k1 in range(1, size1 + 1):
            for k2 in range(1, size2 + 1):
                if k1 < s[item]:
                    if k2 < s[item]:
                        cache1[item][size1][size2] = cache1[item - 1][k1][k2]
                    else:
                        cache1[item][size1][size2] = max(v[item] + cache1[item - 1][k1][k2 - s[item]],
                                                         cache1[item - 1][k1][k2])
                elif k2 < s[item]:
                        cache1[item][size1][size2] = max(v[item] + cache1[item - 1][k1 - s[item]][k2],
                                                         cache1[item - 1][k1][k2])
                else:
                    cache1[item][size1][size2] = max(v[item] + cache1[item - 1][k1 - s[item]][k2],
                                                     v[item] + cache1[item - 1][k1][k2 - s[item]],
                                                     cache1[item - 1][k1][k2])
    return cache1[i][size1][size2]


sizes = [1, 3, 5, 7, 10, 12, 14, 16, 18, 20]
dpruntimes = [1.2428698000000011, 0.9330645000000004, 0.9718564000000001, 0.7869660000000067,
              1.030841500000001, 0.9620772000000031, 1.0599461999999988, 0.8945256999999991,
              0.8089149999999989, 0.9412880000000001]
memoruntimes = [55.862270300000006, 48.9451923, 50.448296, 53.6858894,
                48.2366288, 46.985236, 46.9018552, 25.6787057, 32.6747065, 42.452467899999995]

s1, v1 = generator(n, ave_size)
# memotime = timeit.timeit("memoizingKnapsack(n, K1, K2, s1, v1)", number=20, globals=globals())
# dptime = timeit.timeit("dpKnapsack(n, K1, K2, s1, v1)", number=20, globals=globals())
#
# print(dptime)
# print(memotime)

plt.title('Memoizing and DP Knapsack: runtimes based on aveSize used')
plt.plot(sizes, memoruntimes)
plt.text(5.0, 45.0, "Memoizing Knapsack")

plt.plot(sizes, dpruntimes)
plt.text(5.0, 5.0, "Dynamic Programming Knapsack")

plt.yscale('linear')
plt.xscale('linear')
plt.ylabel('runtime(in seconds)')
plt.xlabel('aveSize')
plt.show()
