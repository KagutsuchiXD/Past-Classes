import numpy as np
import matplotlib.pyplot as plt
import random
import time
import math
from Assign6 import dc3prob


def highschool(p, q):
    pq = np.zeros((len(p) + len(q)))
    for i in range(len(p)):
        for j in range(len(q)):
            pq[i + j] += p[i] * q[j]
    return pq


def dc(p, q, n):
    pq = np.zeros((2*n))
    if n == 1:
        pq[0] = p[0] * q[0]
        return pq

    nextsize = (n//2)
    PQll = dc(p[0:nextsize], q[0:nextsize], nextsize)
    PQlh = dc(p[0:nextsize], q[nextsize:], nextsize)
    PQhl = dc(p[nextsize:], q[0:nextsize], nextsize)
    PQhh = dc(p[nextsize:], q[nextsize:], nextsize)

    for i in range(n):
        pq[i] += PQll[i]
        pq[i + nextsize] += PQlh[i]
        pq[i + nextsize] += PQhl[i]
        pq[i + n] += PQhh[i]

    return pq


def randfloatlist(a, b, size):
    # returns a list of floats of specified size with values ranging from a to b
    floatlist = []
    for i in range(size):
        floatlist.append(random.uniform(a, b))
    return floatlist


def randintlist(a, b, size):
    # returns a list of floats of specified size with values ranging from a to b
    intlist = []
    for i in range(size):
        intlist.append(random.uniform(a, b))
    return intlist



def graph(xaxis, times1, times2, times3):
    # takes in arrays and graphs them
    plt.title("Empirical Study")
    plt.plot(xaxis, times1, "b", label="Simple")
    plt.plot(xaxis, times2, "r", label="DC 4 Problem")
    plt.plot(xaxis, times3, "g", label="DC 3 Problem")

    plt.yscale('log', basey=2)
    plt.xscale('log', basex=2)
    plt.grid(True)
    plt.legend()
    plt.ylabel('runtime(in seconds)')
    plt.xlabel('problem size')
    plt.show()


def empiricalstudy():
    # uses the graph() and randfloatlist() functions to implement the empirical study
    # of the two algorithms and then outputs the results to a .txt file and as a graph.

    start_value = 5  # for 2^5 = 32
    end_value = 12  # for 2^12 = 4096
    num_loops = 10

    sizes = []
    hstimes = []
    dctimes = []
    dc3times = []

    results = open('results.txt', 'w')
    for i in range(start_value, end_value + 1):  # loop doubling problem size each iteration
        sizes.append(2**i)
        hsstart = time.time()
        for x in range(num_loops):
            poly1 = randfloatlist(-1.0, 1.0, 2**i)
            poly2 = randfloatlist(-1.0, 1.0, 2**i)
            hsans = highschool(poly1, poly2)
        hsend = time.time()
        hstimes.append(hsend - hsstart)

        dcstart = time.time()
        for x in range(num_loops):
            poly1 = randfloatlist(-1.0, 1.0, 2**i)
            poly2 = randfloatlist(-1.0, 1.0, 2**i)
            dcans = dc(poly1, poly2, len(poly1))
        dcend = time.time()
        dctimes.append(dcend - dcstart)

        dc3start = time.time()
        for x in range(num_loops):
            poly1 = randfloatlist(-1.0, 1.0, 2 ** i)
            poly2 = randfloatlist(-1.0, 1.0, 2 ** i)
            dc3ans = dc3prob(poly1, poly2, len(poly1))
        dc3end = time.time()
        dc3times.append(dc3end - dc3start)

    graph(sizes, hstimes, dctimes, dc3times)
    results.write('***************Results of Empirical Study***************\n')
    for i in range(len(sizes)):
        results.write('For size of ' + str(sizes[i]) + ': \n')
        results.write('Runtime for Highschool Algorithm: ' + str(hstimes[i]) + ' seconds\n')
        results.write('Runtime for Divide and Conquer 4 Subproblem Algorithm: ' + str(dctimes[i]) + ' seconds\n')
        results.write('Runtime for Divide and Conquer 3 Subproblem Algorithm: ' + str(dc3times[i]) + ' seconds\n')
        results.write('****************************************************************\n')
    results.write("\n\nSlopes for each set of results: \n\n")
    results.write("Slope for Highschool Algorithm: " +
                  str((math.log2(hstimes[-1]) - math.log2(hstimes[2]))/(math.log2(4096) - math.log2(128))) + "\n")
    results.write("Slope for DC 4 Subproblem Algorithm: " +
                  str((math.log2(dctimes[-1]) - math.log2(dctimes[2]))/(math.log2(4096) - math.log2(128))) + "\n")
    results.write("Slope for DC 3 Subproblem Algorithm: " +
                  str((math.log2(dc3times[-1]) - math.log2(dc3times[2]))/(math.log2(4096) - math.log2(128))) + "\n")

empiricalstudy()
# p = [1, 1, 1, 1]
# q = [1, 1, 1, 1]
#
# print(dc(p, q, 4))
# print(dc3prob(p, q, 4))


