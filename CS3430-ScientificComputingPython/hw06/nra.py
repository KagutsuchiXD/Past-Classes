
#############################################
# Module: nra.py
# Description: Newton-Raphson Algorithm
#############################################

import numpy as np
import math
from maker import maker
from pwr import pwr
from prod import prod
from var import var
from const import const
from plus import plus
from drv import drv
from hw06_parser import parser
from tof import tof

class nra(object):

    @staticmethod
    def zr1(fstr, x0, num_iters=3):
        x = x0
        fun = parser.parse_sum(fstr)
        der = drv.drv(fun)
        fun = tof.tof(fun)
        der = tof.tof(der)
        num = 0
        while num < num_iters:
            h = fun(x) / der(x)
            x = (x - h)
            num += 1
        return x

    @staticmethod
    def zr2(fstr, x0, delta=0.0001):
        x = x0
        fun = parser.parse_sum(fstr)
        der = drv.drv(fun)
        fun = tof.tof(fun)
        der = tof.tof(der)
        h = fun(x)/der(x)
        ni = 0
        while abs(h) > delta:
            h = fun(x) / der(x)
            x = (x - h)
            ni += 1
        return x, ni


    @staticmethod
    def check_zr(fstr, zr, err=0.0001):
        return abs(tof.tof(parser.parse_sum(fstr))(zr) - 0.0) <= err 
