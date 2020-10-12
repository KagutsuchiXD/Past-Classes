import numpy as np
import math


def rbs(index, size):
    if size == 1:
        return int(index)
    binary = bin(index)[2:]
    while len(binary) < len(bin(size)[2:]):
        binary = '0' + binary
    reverse = binary[::-1]
    return int(reverse, 2)


def dpfft(P, W, n):
    cache = np.zeros((int(math.log2(n)+1), n), dtype=complex)
    for i in range(n):
        cache[0][i] = P[rbs(i, n-1)]
    # do each row starting at 1
    for i in range(1, int(math.log2(n)+1)):
        size = 2**i
        for j in range(0, n, size):
            for k in range(0, size//2):
                index = ((j + k) % size)*(2**(len(cache) - 1 - i))
                ev = cache[i-1, j + k]
                od = cache[i-1][j + size//2 + k]
                om = W[index]
                even = ev + (om * od)
                odd = ev - (om * od)
                cache[i, j + k] = even
                cache[i, j + size // 2 + k] = odd
    return cache


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


# p = [0, 1, 2, 3, 4, 5, 6, 7]
# n = 8
# solA = fft([complex(p[i], 0) for i in range(0, n)], getV(n, 1), n)
# solB = dpfft([complex(p[i], 0) for i in range(0, n)], getV(n, 1), n)
# print('FFT')
# print(solA)
# print('DPFFT')
# print(solB)
