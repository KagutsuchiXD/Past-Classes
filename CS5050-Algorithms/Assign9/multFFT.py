import numpy as np
import math


def fft(P, W, n):
    # base cases
    if n == 1:
        return [P[0]]
    # splitting
    Pe = [P[j] for j in range(0, n, 2)]
    Po = [P[j] for j in range(1, n, 2)]

    W2 = [(W[j]**2) for j in range(0, int(n/2))]

    Se = fft(Pe, W2, int(n/2))
    So = fft(Po, W2, int(n/2))

    return [(Se[j] + (W[j]*So[j])) for j in range(0, int(n/2))] + [(Se[j] - (W[j]*So[j])) for j in range(0, int(n/2))]


def getV(size, sign):
    v = []

    for i in range(0, size):
        v.append(complex(math.cos((sign*2*i*math.pi)/size), math.sin((sign*2*i*math.pi)/size)))
    return v


def inversefft(pq, n):
    solution = [s/n for s in fft(pq, getV(n, -1), n)]
    return solution


def multfft(n0, n1, n):
    p = n0
    q = n1
    for i in range(n):
        p.append(0)
        q.append(0)
    v = getV(2*n, 1)

    ps = fft(p, v, 2*n)
    qs = fft(q, v, 2*n)
    pqs = [ps[i] * qs[i] for i in range(2*n)]

    pq = inversefft(pqs, 2*n)

    answer = [pq[i].real for i in range(2*n)]

    return answer


# p1 = [1, 2, 3, 4]
# q1 = [5, 6, 7, 8]
# pq1 = multfft(p1, q1, 4)
# pq2 = highschool(p1, q1)
#
# print('PQ1: ')
# print(pq1)
# print('PQ2: ')
# print(pq2)
