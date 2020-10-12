#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s20_hw08_uts.py
# description: unit tests for CS 3430: S20: Assignment 08
##############################################################

import unittest
import math
import numpy as np
from PIL import Image
from cs3430_s20_hw08 import depil, ht, ht_find_lines


class Assign08UnitTests(unittest.TestCase):

    def __test_depil(self, inpath, outpath, default_delta=1.0, magn_thresh=20):
        input_image = Image.open(inpath)
        output_image = depil(input_image, default_delta=default_delta, magn_thresh=magn_thresh)
        output_image.save(outpath)
        del input_image
        del output_image

    def __test_ht(self, inpath, default_delta=1.0, magn_thresh=20, spl=200):
        img = Image.open(inpath)
        img = depil(img, default_delta=default_delta, magn_thresh=magn_thresh)
        ht_table = ht(img, angle_step=1)
        del img
        print('Lines found in {}:'.format(inpath))
        print(ht_find_lines(ht_table, spl=spl))

    ### ================ Problem 1: Unit Tests =====================

    # def test_hw08_prob01_ut01(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 01 ************')
    #     self.__test_depil('imgs/EdgeImage_01.jpg', 'out_imgs/EdgeImage_01_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 01: pass')
    #
    # def test_hw08_prob01_ut02(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 02 ************')
    #     self.__test_depil('imgs/EdgeImage_02.jpg', 'out_imgs/EdgeImage_02_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 02: pass')
    #
    # def test_hw08_prob01_ut03(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 03 ************')
    #     self.__test_depil('imgs/EdgeImage_03.jpg', 'out_imgs/EdgeImage_03_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 03: pass')
    #
    # def test_hw08_prob01_ut04(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 04 ************')
    #     self.__test_depil('imgs/EdgeImage_04.jpg', 'out_imgs/EdgeImage_04_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 04: pass')
    #
    # def test_hw08_prob01_ut05(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 05 ************')
    #     self.__test_depil('imgs/EdgeImage_05.jpg', 'out_imgs/EdgeImage_05_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 05: pass')
    #
    # def test_hw08_prob01_ut06(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 06 ************')
    #     self.__test_depil('imgs/EdgeImage_06.jpg', 'out_imgs/EdgeImage_06_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 06: pass')
    #
    # def test_hw08_prob01_ut07(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 07 ************')
    #     self.__test_depil('imgs/EdgeImage_07.jpg', 'out_imgs/EdgeImage_07_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 07: pass')
    #
    # def test_hw08_prob01_ut08(self):
    #     print('\n***** CS3430: S20: HW08: Problem 01: Unit Test 08 ************')
    #     self.__test_depil('imgs/road_01.png', 'out_imgs/road_01_ed.png')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 08: pass')
    #
    # def test_hw08_prob01_ut09(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 09 ************')
    #     self.__test_depil('imgs/road_02.png', 'out_imgs/road_02_ed.png')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 09: pass')
    #
    # def test_hw08_prob01_ut10(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 10 ************')
    #     self.__test_depil('imgs/BirdOrnament.jpg', 'out_imgs/BirdOrnament_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 10: pass')
    #
    # def test_hw08_prob01_ut11(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 11 ************')
    #     self.__test_depil('imgs/hive01.png', 'out_imgs/hive01_ed.png')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 11: pass')
    #
    # def test_hw08_prob01_ut12(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 12 ************')
    #     self.__test_depil('imgs/hive02.png', 'out_imgs/hive02_ed.png')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 12: pass')
    #
    # def test_hw08_prob01_ut13(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 13 ************')
    #     self.__test_depil('imgs/hive03.png', 'out_imgs/hive03_ed.png')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 13: pass')
    #
    # def test_hw08_prob01_ut14(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 14 ************')
    #     self.__test_depil('imgs/lunch.jpg', 'out_imgs/lunch_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 14: pass')
    #
    # def test_hw08_prob01_ut15(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 15 ************')
    #     self.__test_depil('imgs/june.jpg', 'out_imgs/june_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 15: pass')
    #
    # def test_hw08_prob01_ut16(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 16 ************')
    #     self.__test_depil('imgs/nt_01.jpg', 'out_imgs/nt_01_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 16: pass')
    #
    # def test_hw08_prob01_ut17(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 17 ************')
    #     self.__test_depil('imgs/sudoku.jpg', 'out_imgs/sudoku_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 17: pass')
    #
    # def test_hw08_prob01_ut18(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 18 ************')
    #     self.__test_depil('imgs/elephant.jpg', 'out_imgs/elephant_ed.jpg')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 18: pass')
    #
    # def test_hw08_prob01_ut19(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 19 ************')
    #     self.__test_depil('imgs/road_03.png', 'out_imgs/road_03_ed.png')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 19: pass')
    #
    # def test_hw08_prob01_ut20(self):
    #     print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 20 ************')
    #     self.__test_depil('imgs/road_04.png', 'out_imgs/road_04_ed.png')
    #     print('CS 3430: S20: HW08: Problem 01: Unit Test 20: pass')


    ### ================ Problem 2: Unit Tests =====================

    '''
    ***** CS3430: S20: HW08: Problem 02: Unit Test 01 ************
    Lines found in imgs/EdgeImage_01.jpg:
    [(13, 90, 270), (12, 90, 270)]
    CS 3430: S20: HW08: Problem 02: Unit Test 01: pass
    '''
    def test_hw08_prob02_ut01(self):
        print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 01 ************')
        self.__test_ht('imgs/EdgeImage_01.jpg')
        print('CS 3430: S20: HW08: Problem 02: Unit Test 01: pass')

    '''
    ***** CS3430: S20: HW08: Problem 02: Unit Test 02 ************
    Lines found in imgs/EdgeImage_02.jpg:
    [(1, 40, 254), (2, 40, 221)]
    CS 3430: S20: HW08: Problem 02: Unit Test 02: pass
    '''
    def test_hw08_prob02_ut02(self):
        print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 02 ************')
        self.__test_ht('imgs/EdgeImage_02.jpg')
        print('CS 3430: S20: HW08: Problem 02: Unit Test 02: pass')

    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 03 ************
    # Lines found in imgs/EdgeImage_03.jpg:
    # [(39, 22, 213), (40, 158, 206), (39, 158, 200)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 03: pass
    # '''
    # def test_hw08_prob02_ut03(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 03 ************')
    #     self.__test_ht('imgs/EdgeImage_03.jpg')
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 03: pass')
    #
    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 04 ************
    # Lines found in imgs/EdgeImage_04.jpg:
    # [(0, 0, 298), (1, 0, 298), (0, 180, 298)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 04: pass
    # '''
    # def test_hw08_prob02_ut04(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 04 ************')
    #     self.__test_ht('imgs/EdgeImage_04.jpg')
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 04: pass')
    #
    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 05 ************
    # Lines found in imgs/EdgeImage_05.jpg:
    # [(0, 0, 298), (1, 0, 298), (0, 180, 298)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 05: pass
    # '''
    # def test_hw08_prob02_ut05(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 05 ************')
    #     self.__test_ht('imgs/EdgeImage_05.jpg')
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 05: pass')
    #
    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 06 ************
    # Lines found in imgs/EdgeImage_06.jpg:
    # [(50, 0, 298), (51, 0, 298), (50, 180, 298), (49, 180, 298)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 06: pass
    # '''
    # def test_hw08_prob02_ut06(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 06 ************')
    #     self.__test_ht('imgs/EdgeImage_06.jpg')
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 06: pass')
    #
    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 07 ************
    # Lines found in imgs/EdgeImage_07.jpg:
    # [(50, 90, 298), (49, 90, 298), (50, 270, 298), (51, 270, 298)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 07: pass
    # '''
    # def test_hw08_prob02_ut07(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 07 ************')
    #     self.__test_ht('imgs/EdgeImage_07.jpg')
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 07: pass')
    #
    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 08 ************
    # Lines found in imgs/hive01.png:
    # [(153, 77, 602), (46, 86, 628), (65, 87, 605), (149, 91, 600), (150, 91, 609),
    #  (143, 93, 600), (141, 93, 618), (154, 94, 603), (159, 96, 603), (152, 96, 603),
    #  (163, 97, 602), (155, 97, 606), (178, 98, 602), (160, 98, 605)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 08: pass
    # '''
    # def test_hw08_prob02_ut08(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 08 ************')
    #     self.__test_ht('imgs/hive01.png', spl=600)
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 08: pass')
    #
    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 09 ************
    # Lines found in imgs/road_04.png:
    # [(36, 265, 217), (37, 265, 256), (35, 266, 201), (36, 266, 218), (49, 270, 218),
    #  (45, 270, 207), (48, 270, 207), (52, 271, 249), (53, 271, 233), (51, 271, 243),
    #  (50, 271, 231), (44, 271, 230), (44, 272, 243), (45, 272, 217), (50, 272, 213),
    #  (52, 272, 277), (53, 272, 265), (54, 272, 207), (51, 272, 248), (48, 272, 213),
    #  (46, 273, 226), (47, 273, 253), (49, 273, 231), (50, 273, 234), (51, 273, 206),
    #  (48, 273, 226), (52, 273, 202), (48, 274, 221), (49, 274, 227), (50, 274, 215),
    #  (43, 275, 202)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 09: pass
    # '''
    # def test_hw08_prob02_ut09(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 09 ************')
    #     self.__test_ht('imgs/road_04.png', spl=200)
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 09: pass')
    #
    # '''
    # ***** CS3430: S20: HW08: Problem 02: Unit Test 10 ************
    # Lines found in imgs/nt_01.jpg:
    # [(18, 45, 166), (16, 45, 163), (21, 45, 164), (23, 45, 159), (25, 45, 150),
    #  (43, 179, 161), (43, 180, 174), (46, 181, 160), (44, 181, 152), (42, 181, 161),
    #  (1, 225, 150), (6, 225, 170), (8, 225, 157), (4, 225, 157), (18, 315, 152),
    #  (1, 330, 152), (47, 350, 170), (48, 351, 160), (42, 356, 155), (44, 357, 164),
    #  (39, 358, 162), (40, 358, 157), (43, 358, 190), (45, 358, 167), (39, 359, 161),
    #  (43, 359, 150), (44, 359, 173)]
    # CS 3430: S20: HW08: Problem 02: Unit Test 10: pass
    # '''
    # def test_hw08_prob02_ut10(self):
    #     print('\n***** CS3430: S20: HW08: Problem 02: Unit Test 10 ************')
    #     self.__test_ht('imgs/nt_01.jpg', spl=150)
    #     print('CS 3430: S20: HW08: Problem 02: Unit Test 10: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
