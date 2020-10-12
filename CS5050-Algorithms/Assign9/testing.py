# This is code for running each ot the testing prompts from the assignment

import multFFT as m
import matplotlib.pyplot as plt
import numpy as np
import random
import time



def test1():
    # I tested these cases using different values showing that my algorithm is correct.

    p1 = [1, 2, 3, 4]
    q1 = [5, 6, 7, 8]
    pq1a = m.multfft(p1, q1, len(p1))
    pq1b = highschool(p1, q1)
    print('MultFFT:')
    print(pq1a)
    print('Highschool:')
    print(pq1b)

    # num3 = (base ** 3) * 4 + (base ** 2) * 3 + (base ** 1) * 2 + (base ** 0) * 1
    # num4 = (base ** 3) * 7 + (base ** 2) * 8 + (base ** 1) * 3 + (base ** 0) * 2
    # p2 = baseTenToBase2to32(num3)
    # q2 = baseTenToBase2to32(num4)
    p2 = [2, 3, 4, 5]
    q2 = [1, 3, 5, 7]
    pq2a = m.multfft(p2, q2, len(p2))
    pq2b = highschool(p2, q2)
    print('MultFFT:')
    print(pq2a)
    print('Highschool:')
    print(pq2b)


def test2():
    # As shown in the graph the size of the errors grows with the size of n.


    xaxis = []
    yaxis = []

    for i in range(2, 13):
        n = 2**i
        p = randintlist(1, 9, n)
        q = randintlist(1, 9, n)
        pqa = m.multfft(p, q, n)
        pqb = highschool(p, q)
        xaxis.append(n)
        diffs = [abs(pqa[j] - pqb[j]) for j in range(len(pqa))]
        aae = 0
        for k in range(len(diffs)):
            aae += diffs[k]
        aae = (aae/(2*n))
        yaxis.append(aae)


    plt.title("Test 2: Average Absolute Errors")
    plt.plot(xaxis, yaxis, "b", label="Differences")

    # plt.yscale('log', basey=2)
    plt.xscale('log', basex=2)
    plt.grid(True)
    plt.legend()
    plt.ylabel('Average Absolute Error')
    plt.xlabel('Problem Size')
    plt.show()


def test3():
    start_value = 5  # for 2^5 = 32
    end_value = 12  # for 2^12 = 4096
    num_loops = 10

    sizes = []
    hstimes = []
    ffttimes = []
    dc3times = []

    for i in range(start_value, end_value + 1):  # loop doubling problem size each iteration
        n = 2 ** i
        sizes.append(n)
        hsstart = time.time()
        for x in range(num_loops):
            p = randintlist(1, 9, n)
            q = randintlist(1, 9, n)
            hsans = highschool(p, q)
        hsend = time.time()
        hstimes.append(hsend - hsstart)

        fftstart = time.time()
        for x in range(num_loops):
            p = randintlist(1, 9, n)
            q = randintlist(1, 9, n)
            ans = m.multfft(p, q, len(p))
        fftend = time.time()
        ffttimes.append(fftend - fftstart)

        dc3start = time.time()
        for x in range(num_loops):
            p = randintlist(1, 9, n)
            q = randintlist(1, 9, n)
            dc3ans = dc3prob(p, q, len(p))
        dc3end = time.time()
        dc3times.append(dc3end - dc3start)

    graph(sizes, hstimes, ffttimes, dc3times)
    pass


def test4():
    base = 2 ** 32
    num1 = (base ** 3) * 5 + (base ** 2) * 4 + (base ** 1) * 3 + (base ** 0) * 1
    num2 = (base ** 3) * 2 + (base ** 2) * 3 + (base ** 1) * 2 + (base ** 0) * 7
    p1 = baseTenToBase2to32(num1)
    q1 = baseTenToBase2to32(num2)
    print('Input:')
    print(ptostring(p1))
    print(ptostring(q1))
    pq1a = m.multfft(p1, q1, len(p1))
    pq1b = highschool(p1, q1)
    rpq1a = []
    rpq1b = []
    for j in range(len(pq1a)):
        rpq1a.append(int(pq1a[j]))
        rpq1b.append(int(pq1b[j]))
    print('MultFFT:')
    print(ptostring(rpq1a))
    print('Highschool:')
    print(ptostring(rpq1b))

    num3 = (base ** 7) * 32 + (base ** 6) * 18 + (base ** 5) * 49 + (base ** 4) * 76 +\
           (base ** 3) * 53 + (base ** 2) * 46 + (base ** 1) * 13 + (base ** 0) * 21
    num4 = (base ** 7) * 4 + (base ** 6) * 7 + (base ** 5) * 2 + (base ** 4) * 1 + \
           (base ** 3) * 2 + (base ** 2) * 3 + (base ** 1) * 2 + (base ** 0) * 7
    p2 = baseTenToBase2to32(num3)
    q2 = baseTenToBase2to32(num4)
    print('Input:')
    print(ptostring(p2))
    print(ptostring(q2))
    pq2a = m.multfft(p2, q2, len(p2))
    pq2b = highschool(p2, q2)
    rpq2a = []
    rpq2b = []
    for j in range(len(pq2a)):
        rpq2a.append(int(pq2a[j]))
        rpq2b.append(int(pq2b[j]))
    print('MultFFT:')
    print(ptostring(rpq2a))
    print('Highschool:')
    print(ptostring(rpq2b))


# below are helper functions for running each test above
def ptostring(p):
    output = str()
    for index in range(len(p)):
        strval = str(p[index])
        output += str('0' * (10 - len(strval))) + strval + ','
    return output

def randintlist(a, b, size):
    # returns a list of floats of specified size with values ranging from a to b
    intlist = []
    for i in range(size):
        intlist.append(random.randint(a, b))
    return intlist


def baseTenToBase2to32(n):
    base = 2**32
    digits = []
    while n > 0:
        digits = [n % base] + digits
        n = n//base
    return digits


def highschool(p, q):
    pq = np.zeros((len(p) + len(q)))
    for i in range(len(p)):
        for j in range(len(q)):
            pq[i + j] += p[i] * q[j]
    return pq


def dc3prob(p, q, n):  # Divide and Conquer with 3 Subproblems
    pq = np.zeros((2*n))
    nextsize = (n // 2)
    qlh = np.zeros(nextsize)
    plh = np.zeros(nextsize)
    if n == 1:
        pq[0] = p[0] * q[0]
        return pq
    elif n == 2:
        PQll = p[0] * q[0]
        PQhh = p[1] * q[1]
        Lo = ((p[0] + p[1]) * (q[0] + q[1])) - PQll -PQhh
        return [PQll, Lo, PQhh]
    else:
        pl = p[0:nextsize]
        ph = p[nextsize:]
        ql = q[0:nextsize]
        qh = q[nextsize:]
        for i in range(nextsize):
            qlh[i] = ql[i] + qh[i]
            plh[i] = pl[i] + ph[i]
        Sll = dc3prob(pl, ql, nextsize)
        Shh = dc3prob(ph, qh, nextsize)
        qlh_plh = dc3prob(qlh, plh, nextsize)

        for i in range(len(Sll)):
            pq[i] += Sll[i]
            pq[i + nextsize] += qlh_plh[i] - Sll[i] - Shh[i]
            pq[i + n] += Shh[i]
        return pq


def graph(xaxis, times1, times2, times3):
    # takes in arrays and graphs them
    plt.title("Empirical Study")
    plt.plot(xaxis, times1, "b", label="Simple")
    plt.plot(xaxis, times2, "r", label="multFFT")
    plt.plot(xaxis, times3, "g", label="DC 3 Problem")

    plt.yscale('log', basey=2)
    plt.xscale('log', basex=2)
    plt.grid(True)
    plt.legend()
    plt.ylabel('runtime(in seconds)')
    plt.xlabel('problem size')
    plt.show()

# running each test prompt from the homework description
test1()
test2()
test3()
test4()
