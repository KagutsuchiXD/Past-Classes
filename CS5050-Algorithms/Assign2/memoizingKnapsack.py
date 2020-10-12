val = [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0]
wt = [0, 10, 20, 30, 40, 50, 60]
K1 = 50
K2 = 50
n = len(val)
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
