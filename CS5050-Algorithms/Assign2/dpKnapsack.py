val = [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0]
wt = [0, 10, 20, 30, 40, 50, 60]
K1 = 50
K2 = 50
n = len(val)


def dpKnapsack(i, size1, size2, s, v):
    cache = [[[-1.0 for k in range(K2 + 1)] for j in range(K1 + 1)] for i in range(n + 1)]
    for k1 in range(size1 + 1):
        for k2 in range(size2 + 1):
            cache[0][k1][k2] = 0.0
    for item in range(i):
        cache[item][0][0] = 0.0

    for item in range(1, i + 1):
        for k1 in range(1, size1 + 1):
            for k2 in range(1, size2 + 1):
                if k1 < s[item]:
                    if k2 < s[item]:
                        cache[item][size1][size2] = cache[item - 1][k1][k2]
                    else:
                        cache[item][size1][size2] = max(v[item] + cache[item - 1][k1][k2 - s[item]],
                                                        cache[item - 1][k1][k2])
                elif k2 < s[item]:
                    if k1 < s[item]:
                        cache[item][size1][size2] = cache[item - 1][k1][k2]
                    else:
                        cache[item][size1][size2] = max(v[item] + cache[item - 1][k1 - s[item]][k2],
                                                        cache[item - 1][k1][k2])
                else:
                    cache[item][size1][size2] = max(v[item] + cache[item - 1][k1 - s[item]][k2],
                                                    v[item] + cache[item - 1][k1][k2 - s[item]],
                                                    cache[item - 1][k1][k2])
    return cache[i][size1][size2]
