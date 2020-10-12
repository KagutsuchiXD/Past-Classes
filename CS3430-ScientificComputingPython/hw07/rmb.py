####################################
# module: rmb.py
# Connor Osborne
# A01880782
####################################

import numpy as np


class rmb(object):

    @staticmethod
    def rjl(f, a, b, j, l):

        if l == 1:
            return np.longdouble(rmb.trapezoid(f, a, b, j))

        else:
            el1 = rmb.rjl(f, a, b, j, l - 1)
            el2 = rmb.rjl(f, a, b, j - 1, l - 1)
            return np.longdouble(el1 + ((el1 - el2) / ((4 ** (l - 1)) - 1)))

    @staticmethod
    def trapezoid(f, a, b, j):
        k = 2 ** (j - 1)
        h = (b - a) / k

        trapezoid = 0.0
        for i in range(k + 1):
            if i == k:
                temp = f(b)
            else:
                temp = f(a + (i * h))
            if i != 0 and i != k:
                temp = 2.0 * temp
            trapezoid += temp
        answer = trapezoid * (h/2.0)
        return np.longdouble(answer)
