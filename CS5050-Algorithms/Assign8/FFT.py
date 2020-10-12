import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time


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


def inversefft(p, x, n):
    sol = fft(p, x, n)
    solution = [s/n for s in fft(sol, getV(n, -1), n)]
    return solution


def getV(size, sign):
    v = []

    for i in range(0, size):
        v.append(complex(math.cos((sign*2*i*math.pi)/size), math.sin((sign*2*i*math.pi)/size)))
    return v


def graph(xaxis, times1, times2):
    # takes in arrays and graphs them
    plt.title("Empirical Study")
    plt.plot(xaxis, times1, "b", label="FFT")
    plt.plot(xaxis, times2, "r", label="InverseFFT")

    plt.yscale('log', basey=2)
    plt.xscale('log', basex=2)
    plt.grid(True)
    plt.legend()
    plt.ylabel('runtime(in seconds)')
    plt.xlabel('problem size')
    plt.show()


def randintlist(a, b, size):
    # returns a list of floats of specified size with values ranging from a to b
    intlist = []
    for i in range(size):
        intlist.append(random.randint(a, b))
    return intlist


def empiricalstudy():
    # uses the graph() and randfloatlist() functions to implement the empirical study
    # of the two algorithms and then outputs the results to a .txt file and as a graph.

    start_value = 7  # for 2^7 = 128
    end_value = 20  # for 2^20 =
    num_loops = 10

    sizes = []
    times = []
    invtimes = []

    # results = open('results.txt', 'w')
    for i in range(start_value, end_value + 1):  # loop doubling problem size each iteration
        n = 2**i
        sizes.append(n)
        start = time.time()
        for x in range(num_loops):
            poly = randintlist(1, 9, n)
            omega = getV(n, 1)

            ans = fft([complex(poly[i], 0) for i in range(0, n)], omega, n)
        end = time.time()
        times.append(end - start)

        start2 = time.time()
        for x in range(num_loops):
            poly = randintlist(1, 9, n)
            omega = getV(n, -1)

            ans = inversefft([complex(poly[i], 0) for i in range(0, n)], omega, n)
        end2 = time.time()
        invtimes.append(end2 - start2)

    graph(sizes, times, invtimes)


# n = 8
#
# p = [0, 1, 2, 3, 4, 5, 6, 7]
#
# print("Forward FFT")
#
# sol = fft([complex(p[i], 0) for i in range(0, n)], getV(n, 1), n)
# print(sol)
#
# print("Inverse FFT")
#
# back = [s/8 for s in fft(sol, getV(n, -1), n)]
#
# print("Answer")
#
# print(back)
#
# print(getV(8, 1))
empiricalstudy()
