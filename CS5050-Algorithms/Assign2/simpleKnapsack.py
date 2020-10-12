###########################
from random import random, randint

N = 7
K = 100


def knapsackBool(i, size):
    if size == 0:  # base case
        return True
    if size < 0:  # clean up in case of going negative (at least one object left with not enough space)
        return False
    if i == 0:  # if there are no items and still bag space left then the answer is false
        return False
    return knapsackBool(i-1, size) or knapsackBool(i-1, size - S[i])


for _ in range(0, 100):
    S = [randint(1, K/2) for _ in range(0, N + 1)]
    if knapsackBool(N, K):  # if true then solution exists
        print("Solution exists")
    else:
        print("Solution does not exist")
        

N = 10
K = 10
S = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(knapsackBool(N, K))
