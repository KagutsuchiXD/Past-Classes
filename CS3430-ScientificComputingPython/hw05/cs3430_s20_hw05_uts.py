#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: unit_tests.py
# description: unit tests for CS 3430: S20: Assignment 05
# bugs to vladimir dot kulyukin at usu dot edu.
##############################################################

import unittest
from hw5parser import parser
from prod import prod
from const import const
from pwr import pwr
from var import var
from plus import plus
from tof import tof


class Assign04UnitTests(unittest.TestCase):

    # ================ Problem 1: Unit Tests =====================

    def test_hw05_prob01_ut01(self):
        print('\n***** CS3430: S20: HW05: Problem 01: Unit Test 01 ************')
        s1 = '5x^10'
        e1 = parser.parse_elt(s1)
        err = 0.0001
        assert str(e1) == '(5.0*(x^10.0))'
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() - 5.0) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() - 10.0) <= err
        print('CS 3430: S20: HW05: Problem 01: Unit Test 01: pass')

    def test_hw05_prob01_ut02(self):
        print('\n***** CS3430: S20: HW05: Problem 01: Unit Test 02 ************')
        s1 = '50.5123x^-123.345'
        e1 = parser.parse_elt(s1)
        err = 0.0001
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() - 50.5123) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 123.345) <= err
        assert str(e1) == '(50.5123*(x^-123.345))'
        print('CS 3430: S20: HW05: Problem 01: Unit Test 02: pass')

    def test_hw05_prob01_ut03(self):
        print('\n***** CS3430: S20: HW05: Problem 01: Unit Test 03 ************')
        s1 = '-1001.7341y^-11.57'
        e1 = parser.parse_elt(s1)
        err = 0.0001
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() + 1001.7341) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'y'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 11.57) <= err
        assert str(e1) == '(-1001.7341*(y^-11.57))'
        print('CS 3430: S20: HW05: Problem 01: Unit Test 03: pass')

    def test_hw05_prob01_ut04(self):
        print('\n***** CS3430: S20: HW05: Problem 01: Unit Test 04 ************')
        s1 = '1001.7341z^-11.57'
        e1 = parser.parse_elt(s1)
        err = 0.0001
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() - 1001.7341) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'z'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 11.57) <= err
        assert str(e1) == '(1001.7341*(z^-11.57))'
        print('CS 3430: S20: HW05: Problem 01: Unit Test 04: pass')

    def test_hw05_prob01_ut05(self):
        print('\n***** CS3430: S20: HW05: Problem 01: Unit Test 05 ************')
        s1 = '5x^-10 + 3x^5'
        sum_ex = parser.parse_sum(s1)
        err = 0.0001
        assert isinstance(sum_ex, plus)
        assert isinstance(sum_ex.get_elt1(), prod)
        assert isinstance(sum_ex.get_elt2(), prod)
        e1 = sum_ex.get_elt1()
        assert abs(e1.get_mult1().get_val() - 5.0) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 10.0) <= err
        assert str(e1) == '(5.0*(x^-10.0))'
        e2 = sum_ex.get_elt2()
        assert abs(e2.get_mult1().get_val() - 3.0) <= err
        assert isinstance(e2.get_mult2(), pwr)
        assert isinstance(e2.get_mult2().get_base(), var)
        assert e2.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e2.get_mult2().get_deg().get_val() - 5.0) <= err
        assert str(e2) == '(3.0*(x^5.0))'
        print('CS 3430: S20: HW05: Problem 01: Unit Test 05: pass')

    def test_hw05_prob01_ut06(self):
        print('\n***** CS3430: S20: HW05: Problem 01: Unit Test 06 ************')
        s1 = '5x^-10 + 3x^5 - 9x^3'
        sum_ex = parser.parse_sum(s1)
        err = 0.0001

        assert isinstance(sum_ex, plus)
        assert isinstance(sum_ex.get_elt1(), plus)
        assert isinstance(sum_ex.get_elt2(), prod)

        e1 = sum_ex.get_elt1()  # e1 = 5x^-10 + 3x^5
        e2 = sum_ex.get_elt2()  # e2 = -9x^3
        e11 = e1.get_elt1()  # e11 = 5x^-10
        e12 = e1.get_elt2()  # e12 = 3x^5

        # let's test e11 = 5x^-10
        assert abs(e11.get_mult1().get_val() - 5.0) <= err
        assert isinstance(e11.get_mult2(), pwr)
        assert isinstance(e11.get_mult2().get_base(), var)
        assert e11.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e11.get_mult2().get_deg(), const)
        assert abs(e11.get_mult2().get_deg().get_val() + 10.0) <= err
        assert str(e11) == '(5.0*(x^-10.0))'

        # let's test e12 = 3x^5
        assert abs(e12.get_mult1().get_val() - 3.0) <= err
        assert isinstance(e12.get_mult2(), pwr)
        assert isinstance(e12.get_mult2().get_base(), var)
        assert e12.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e12.get_mult2().get_deg(), const)
        assert abs(e12.get_mult2().get_deg().get_val() - 5.0) <= err
        assert str(e12) == '(3.0*(x^5.0))'

        # let's test e2 = -9x^3
        assert abs(e2.get_mult1().get_val() + 9.0) <= err
        assert isinstance(e2.get_mult2(), pwr)
        assert isinstance(e2.get_mult2().get_base(), var)
        assert e2.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e2.get_mult2().get_deg(), const)
        assert abs(e2.get_mult2().get_deg().get_val() - 3.0) <= err
        assert str(e2) == '(-9.0*(x^3.0))'

        print('CS 3430: S20: HW05: Problem 01: Unit Test 06: pass')

    # ================ Problem 2: Unit Tests =====================

    def test_hw05_prob02_ut01(self):
        print('\n***** CS3430: S20: HW05: Problem 02: Unit Test 01 ************')
        ex = '5x^2'
        my_fun = tof.tof(parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**2.0)
        err = 0.0001
        for x in range(-1000000, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        print('CS 3430: S20: HW05: Problem 02: Unit Test 01: pass')

    def test_hw05_prob02_ut02(self):
        print('\n***** CS3430: S20: HW05: Problem 02: Unit Test 02 ************')
        ex = '5x^2 - 3x^5'
        my_fun = tof.tof(parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**2.0) - 3.0*(x**5.0)
        err = 0.0001
        for x in range(-1000000, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        print('CS 3430: S20: HW05: Problem 02: Unit Test 02: pass')

    def test_hw05_prob02_ut03(self):
        print('\n***** CS3430: S20: HW05: Problem 02: Unit Test 03 ************')
        ex = '5x^-2 - 3x^5 + 4.5x^7.342'
        my_fun = tof.tof(parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**-2.0) - 3.0*(x**5.0) + 4.5*(x**7.342)
        err = 0.0001
        for x in range(-1000000, 0):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        for x in range(1, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        print('CS 3430: S20: HW05: Problem 02: Unit Test 03: pass')

    def test_hw05_prob02_ut04(self):
        print('\n***** CS3430: S20: HW05: Problem 02: Unit Test 04 ************')
        ex = '5x^-2 - 3x^5 + 4.5x^7.342 + 50x^1 - 100x^0'
        my_fun = tof.tof(parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**-2.0) - 3.0*(x**5.0) + 4.5*(x**7.342) + 50.0*x - 100.0
        err = 0.0001
        for x in range(-1000000, 0):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        for x in range(1, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err            
        print('CS 3430: S20: HW05: Problem 02: Unit Test 04: pass')
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
