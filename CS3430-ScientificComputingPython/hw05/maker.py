#!/usr/bin/python

###########################################
# module: maker.py
# bugs to vladimir dot kulyukin dot usu dot edu
###########################################

from var import var
from pwr import pwr
from const import const
from plus import plus
from prod import prod


class maker(object):

    @staticmethod
    def make_var(var_name):
        return var(name=var_name)

    @staticmethod
    def make_const(val):
        return const(val=val)

    @staticmethod
    def make_pwr(var_name, d):
        return pwr(base=maker.make_var(var_name),
                   deg=maker.make_const(d))

    @staticmethod
    def make_prod(mult_expr1, mult_expr2):
        return prod(mult1=mult_expr1, mult2=mult_expr2)

    @staticmethod
    def make_plus(elt_expr1, elt_expr2):
        return plus(elt1=elt_expr1, elt2=elt_expr2)

    @staticmethod
    def make_pwr_expr(expr, deg):
        return pwr(base=expr, deg=maker.make_const(deg))


# $5x^3 + 10x^2 + x + 100$.
elt1 = maker.make_prod(maker.make_const(5),
                       maker.make_pwr('x', 3))
elt2 = maker.make_prod(maker.make_const(10),
                       maker.make_pwr('x', 2))
elt3 = maker.make_prod(maker.make_const(1),
                       maker.make_pwr('x', 1))
elt4 = maker.make_const(100)

poly_sum = maker.make_plus(maker.make_plus(maker.make_plus(elt1, elt2),
                                           elt3),
                           elt4)
