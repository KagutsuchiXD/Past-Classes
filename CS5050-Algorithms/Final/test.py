import matplotlib.pyplot as plt
import numpy as np
import random
import time
import iterativefft as fft


def test():
    start_value = 5  # for 2^5 = 32
    end_value = 15  # for 2^12 = 4096
    num_loops = 10
    sizes = []
    newdptimes = []
    dptimes = []

    for i in range(start_value, end_value + 1):  # loop doubling problem size each iteration
        n = 2 ** i
        sizes.append(n)

        # fftstart = time.time()
        # for x in range(num_loops):
        #     p = randintlist(1, 9, n)
        #     q = fft.getV(n, 1)
        #     ans = fft.fft(p, q, len(p))
        # fftend = time.time()
        # ffttimes.append(fftend - fftstart)

        dpstart = time.time()
        for x in range(num_loops):
            p = randintlist(1, 9, n)
            q = fft.getV(n, 1)
            dpans, timer = fft.dpfft(p, q, len(p))
        dpend = time.time()
        newdptimes.append(timer)
        dptimes.append(dpend - dpstart)

    graph(sizes, newdptimes, dptimes)
    ans = dptimes[-1]/newdptimes[-1]
    print(ans)
    pass


def randintlist(a, b, size):
    # returns a list of floats of specified size with values ranging from a to b
    intlist = []
    for i in range(size):
        intlist.append(random.randint(a, b))
    return intlist


def graph(xaxis, times1, times2):
    # takes in arrays and graphs them
    plt.title("Empirical Study")
    plt.plot(xaxis, times1, "b", label="DP FFT Without Setup Steps")
    plt.plot(xaxis, times2, "r", label="DP FFT With Setup Steps")
    # plt.plot(xaxis, times3, "g", label="")

    plt.yscale('log', basey=2)
    plt.xscale('log', basex=2)
    plt.grid(True)
    plt.legend()
    plt.ylabel('runtime(in seconds)')
    plt.xlabel('problem size')
    plt.show()


test()
