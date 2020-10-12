# justFFT from canvas page

import math
from math import *
import numpy as np

def getV(n, sign = 1):
    return [complex(cos(2*pi*i/n), sign * sin(2*pi*i/n)) for i in range(0, n)]

def fft(p, v, n, depth = 0):
    #print("%s%s" % (" |"*depth+"in =", str(p)))
    if n == 1:
        #print("%s%s" % (" |"*depth+"out=", str(p)))
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
    #print("%s%s" % (" |"*depth+"out=", str(solution)))
    return solution
# justFFT from canvas page

def fftHandler(p):
    n = len(p)
    sol = fft([complex(p[i], 0) for i in range(0, n)], getV(n, 1), n)
    return sol

def inverseFftHandler(pInv):
    n = len(pInv)
    inv = [s / n for s in fft(pInv, getV(n, -1), n)]
    return inv


def fftMultiplication(a, b):
    while 2 ** int(math.log2(len(a))) != len(a):
        a.append(0)
    while 2 ** int(math.log2(len(b))) != len(b):
        b.append(0)
    aLen = len(a)
    for i in range(aLen):
        a.append(0)
    bLen = len(b)
    for i in range(bLen):
        b.append(0)
    while len(a) > len(b):
        b.append(0)
    while len(b) > len(a):
        a.append(0)
    #####################
    aFFT = fftHandler(a)
    bFFT = fftHandler(b)
    
    abFFT = list()
    for i in range(len(aFFT)):
        abFFT.append(aFFT[i] * bFFT[i])
    ab = inverseFftHandler(abFFT)

    realValues = np.zeros(len(ab))
    for i in range(len(ab)):
        realValues[i] = int(ab[i].real)

    index = 0
    carry = 0
    while (carry != 0) or (index < len(ab)):
        tempSum = carry + realValues[index]
        carry = tempSum // BASE
        realValues[index] = (tempSum % BASE)
        index += 1

    while realValues[-1] == 0:
        realValues = realValues[:-1]
    return realValues

BASE = 2**32

intA = (BASE) * 2 + 3 # 0000000002,0000000003
"""
base  2 = 0, 1, 10, 11, 20, ...
base 10 = 8, 9, 10, ...
base 2**32 (or 4294967296) = [0,0,4294967294], [0,0,4294967295], [0,1,0], [0,1,1]...


"""
def tenToBase(n):
    #convert int(BASE 10) to Base 2**32
    myDigits = list()
    while n > 0:
        myDigits = [n % BASE] + myDigits
        n = n // BASE
    return myDigits
print("intA (10):  ", intA)
print("intA(2**32):", tenToBase(intA))

# 321 = (10**2) * 3 + (10**1) * 2 + (10**0) * 1
intB = (BASE**2) * 3 + (BASE**1) * 2 + (BASE**0) * 1 #0000000003,0000000002,0000000001

print("intB (10):  ", intB)
print("intB(2**32):", tenToBase(intB))
print("a * b:", fftMultiplication(tenToBase(intA), tenToBase(intB)))
print("proof:", tenToBase(intA * intB))

