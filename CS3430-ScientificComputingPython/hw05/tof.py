#!/usr/bin/python

#################################################
# module: tof.py
# YOUR NAME
# YOUR A#
#################################################


from pwr import pwr
from const import const
from plus import plus
from prod import prod
from var import var


class tof(object):

    @staticmethod
    def const_tof(fr):
        """convert a const object to Py function."""
        assert isinstance(fr, const)
        return lambda x: fr.get_val()

    @staticmethod
    def var_tof(fr):
        """convert a var object to Py function."""        
        assert isinstance(fr, var)
        return lambda x: x

    @staticmethod
    def prod_tof(fr):
        """convert a prod object to a Py function."""
        assert isinstance(fr, prod)
        con = tof.tof(fr.get_mult1())
        pow = tof.tof(fr.get_mult2())
        return lambda x: con(x) * pow(x)
    
    @staticmethod
    def plus_tof(fr):
        """convert a plus object to a Py function."""
        assert isinstance(fr, plus)

        p1 = tof.tof(fr.get_elt1())

        p2 = tof.tof(fr.get_elt2())

        return lambda x: p1(x) + p2(x)

    @staticmethod
    def pwr_tof(fr):
        """convert a pwr object to a Py function."""
        assert isinstance(fr, pwr)
        var = tof.tof(fr.get_base())
        deg = tof.tof(fr.get_deg())

        return lambda x: var(x)**deg(x)

    @staticmethod
    def tof(fr):
        """convert a const/var/prod/plus/pwr/ object to a Py function."""
        if isinstance(fr, const):
            return tof.const_tof(fr)
        elif isinstance(fr, var):
            return tof.var_tof(fr)
        elif isinstance(fr, prod):
            return tof.prod_tof(fr)
        elif isinstance(fr, plus):
            return tof.plus_tof(fr)
        elif isinstance(fr, pwr):
            return tof.pwr_tof(fr)
        else:
            print('error: not a valid object')
