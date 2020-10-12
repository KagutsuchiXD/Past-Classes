import unittest
import math
import numpy as np
# rename this module if importing parser causes a problem in your Py IDE
# remember to rename in the relevant unit tests below
from hw07_parser import parser
from tof import tof
from drv import drv
from cdd import cdd
from rxp import rxp
from rmb import rmb

f = lambda x: math.e**(2.5*x)
print(cdd.drv1_ord2(f, 0.41, 0.00001))

f2 = lambda x: math.e**(3.5*x)
print(cdd.drv1_ord4(f2, 0.51, 0.00001))

f3 = lambda x: math.e**(4.5*x)
print(cdd.drv1_ord2(f3, 0.61, 0.00001))

f4 = lambda x: math.e**(5.5*x)
print(cdd.drv1_ord4(f4, 0.71, 0.00001))


# s = "10x^4 - 5x^3 + 3x^2 - 15x"
# f = lambda x: 10*x**4 - 5*x**3 + 3*x**2 - 15*x
#
# print(rxp.drv2(f, cdd.drv1_ord2(f, 0.5, 0.0001), 0.5, 0.0001))
