
####################################
# module: cdd.py
# Connor Osborne
# A01880782
####################################

import numpy as np


class cdd(object):

    @staticmethod
    def drv1_ord2(f, x, h):
        # Table 6.3 formula 1, p. 339 in CDD handout
        el1 = f(x+h)
        el2 = f(x-h)
        div = 2*h
        deriv = np.longdouble((el1-el2)/div)
        return deriv

    @staticmethod
    def drv1_ord4(f, x, h):
        # Table 6.4 formula 1, p. 339 in the CDD handout
        el1 = -1 * f(x + (2*h))
        el2 = 8 * f(x + h)
        el3 = -8 * f(x - h)
        el4 = f(x - (2*h))
        top = el1 + el2 + el3 + el4
        div = 12 * h
        deriv = np.longdouble(top / div)
        return deriv

    @staticmethod
    def drv2_ord2(f, x, h):
        # Table 6.3, formula 2, p. 339 in CDD handout
        el1 = f(x + h)
        el2 = -2 * f(x)
        el3 = f(x-h)
        top = el1 + el2 + el3
        div = h**2
        deriv = np.longdouble(top/div)
        return deriv

    @staticmethod
    def drv2_ord4(f, x, h):
        # Table 6.4, formula 2, p. 339 in CDD handout
        el1 = -1 * f(x + (2 * h))
        el2 = 16 * f(x + h)
        el3 = -30 * f(x)
        el4 = 16 * f(x - h)
        el5 = -1 * f(x - (2 * h))
        top = el1 + el2 + el3 + el4 + el5
        bot = 12 * (h**2)
        deriv = np.longdouble(top/bot)
        return deriv
