import numpy as np
import matplotlib.pyplot as plt
import random
import time


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


def graph(xaxis, times1, times2):
    # takes in arrays and graphs them
    fig = plt.figure()
    ax = fig.add_subplot()

    # line1 = plt.plot(xaxis, times1)
    line1 = plt.Line2D(xaxis, times1, color='red', label='Highschool')
    # line2 = plt.plot(xaxis, times2)
    line2 = plt.Line2D(xaxis, times2, color='blue', label='Divide and Conquer')
    ax.add_line(line1)
    ax.add_line(line2)

    plt.legend(handles=[line1, line2])

    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('runtime(in seconds)')
    plt.xlabel('problem size')
    plt.show()


def empiricalstudy():
    # uses the graph() and randfloatlist() functions to implement the empirical study
    # of the two algorithms and then outputs the results to a .txt file and as a graph.

    start_value = 5  # for 2^5 = 32
    end_value = 13  # for 2^13 = 8192
    num_loops = 10

    sizes = []
    hstimes = []
    dctimes = []

    results = open('empiricalresults.txt', 'w')
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

    graph(sizes, hstimes, dctimes)
    results.write('***************Results of Empirical Study***************\n')
    for i in range(len(sizes)):
        results.write('For size of ' + str(sizes[i]) + ': \n')
        results.write('Runtime for Highschool Algorithm: ' + str(hstimes[i]) + ' seconds\n')
        results.write('Runtime for Divide and Conquer Algorithm: ' + str(dctimes[i]) + ' seconds\n')
        results.write('****************************************************************\n')


empiricalstudy()
