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
