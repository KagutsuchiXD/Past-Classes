from math import *
import numpy as np


def getV(n, sign = 1):
    return [complex(cos(2*pi*i/n), sign * sin(2*pi*i/n)) for i in range(0, n)]


def fft(p, v, n, depth = 0):
    # print("%s%s" % (" |"*depth+"in =", str(p)))
    if n == 1:
        # print("%s%s" % (" |"*depth+"out=", str(p)))
        return p 
    # split into even and odd
    eve = [p[i] for i in range(0, n, 2)]
    odd = [p[i] for i in range(1, n, 2)]
    # square the v values
    v2 = [v[i]*v[i] for i in range(0, n//2)]
    # solve the two sub problems
    eveS = fft(eve, v2, n//2, depth+3)
    oddS = fft(odd, v2, n//2, depth+3)
    # construct the solution
    solution = ([eveS[i] + v[i]*oddS[i] for i in range(0, n//2)] + 
                [eveS[i] - v[i]*oddS[i] for i in range(0, n//2)])
    # print("%s%s" % (" |"*depth+"out=", str(solution)))
    return solution
