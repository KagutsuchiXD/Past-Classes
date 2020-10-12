#!/usr/bin/python

#################################################
# module: hw07_parser.py
# YOUR NAME
# YOUR A#
#################################################

from maker import maker


class parser(object):

    @staticmethod
    def parse_elt(elt):
        # let's make sure that elt is a string.
        assert isinstance(elt, str)
        constant, variable, power = elt, 'x', '^0'
        for i in range(len(elt)):
            if elt[i].isalpha():
                constant, variable, power = elt.partition(elt[i])
        if constant == '':
            constant = '1'
        if power != '':
            power = power.split("^")
            power = power[1]

        element = maker.make_prod(maker.make_const(float(constant)), maker.make_pwr(variable, float(power)))
        return element

    @staticmethod
    def parse_sum(poly_str):
        assert isinstance(poly_str, str)
        elementals = poly_str.split()
        i = 0

        while i != len(elementals):
            if elementals[i] == '+':
                elementals.pop(i)
            if elementals[i] == '-':
                elementals.pop(i)
                elementals[i] = '-' + elementals[i]
            i += 1

        for e in range(len(elementals)):
            elementals[e] = parser.parse_elt(elementals[e])

        if len(elementals) == 1:
            return elementals[0]
        else:
            adder = maker.make_plus(elementals[0], elementals[1])
            for i in range(2, len(elementals)):
                adder = maker.make_plus(adder, elementals[i])
            return adder
