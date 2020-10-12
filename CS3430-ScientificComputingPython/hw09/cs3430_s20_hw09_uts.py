#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s20_hw09_uts.py
# description: unit tests for CS 3430: S20: Assignment 09
##############################################################

import unittest
import math
import numpy as np
import cv2
from dcorr import direct_corr
from hinx import hist_index_img_dir
from hinx import HIST_INDEX
from hret import load_hinx, show_images 
from hret import find_sim_rgb_images, find_sim_hsv_images


class Assign09UnitTests(unittest.TestCase):

    def __comp_mats(self, m1, m2, err=0.0001):
        if m1.shape != m2.shape:
            return False
        nr, nc = m1.shape
        for r in range(nr):
            for c in range(nc):
                if abs(m1[r,c] - m2[r,c]) > err:
                    return False
        return True

    # change these variales as you see fit. they're for the second problem's
    # unit tests.
    # IMGDIR is directory where images are saved.
    IMGDIR = 'C:/Users/Sanko/Codding/CS3430/hw09/images/'
    # PICDIR is directory where pickle files are saved.
    PICDIR = 'C:/Users/Sanko/Codding/CS3430/hw09/picks/'
    # TSTDIR is directory where test images are saved.
    TSTDIR = 'C:/Users/Sanko/Codding/CS3430/hw09/hist_test/'

   #  # ================ Problem 1: Unit Tests =====================
   #
   #  def test_hw09_prob01_ut01(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 01 ************')
   #      M1 = np.array([[10, 0, 0],
   #                      [0, 0, 0],
   #                      [0, 0, 0]],
   #                     dtype=float)
   #      M2 = np.array([[0,  0, 0],
   #                     [0, 10, 0],
   #                     [0,  0, 0]],
   #                    dtype=float)
   #      M12 = np.array([[0,   0,  0, 0, 0],
   #                      [0, 100,  0, 0, 0],
   #                      [0,   0,  0, 0, 0],
   #                      [0,   0,  0, 0, 0],
   #                      [0,   0,  0, 0, 0]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      C21 = direct_corr(M2, M1)
   #      M21 = np.array([[0,  0,  0,   0, 0],
   #                      [0,  0,  0,   0, 0],
   #                      [0,  0,  0,   0, 0],
   #                      [0,  0,  0, 100, 0],
   #                      [0,  0,  0,   0, 0]],
   #                     dtype=float)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 01: pass')
   #
   #  def test_hw09_prob01_ut02(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 02 ************')
   #      M1 = np.array([[10, 0, 0],
   #                      [0, 0, 0],
   #                      [0, 0, 0]],
   #                     dtype=float)
   #      M2 = np.array([[0, 10, 0],
   #                     [0,  0, 0],
   #                     [0,  0, 0]],
   #                    dtype=float)
   #      M12 = np.array([[0,   0,  0, 0, 0],
   #                      [0,   0,  0, 0, 0],
   #                      [0, 100,  0, 0, 0],
   #                      [0,   0,  0, 0, 0],
   #                      [0,   0,  0, 0, 0]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([[0,   0,  0,   0, 0],
   #                      [0,   0,  0,   0, 0],
   #                      [0,   0,  0, 100, 0],
   #                      [0,   0,  0,   0, 0],
   #                      [0,   0,  0,   0, 0]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 02: pass')
   #
   #  def test_hw09_prob01_ut03(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 03 ************')
   #      M1 = np.array([[10, 0, 0],
   #                     [0, 0, 0],
   #                     [0, 0, 0]],
   #                     dtype=float)
   #      M2 = np.array([[0,  0, 10],
   #                     [0,  0,  0],
   #                     [0,  0,  0]],
   #                    dtype=float)
   #      M12 = np.array([[0,   0,  0, 0, 0],
   #                      [0,   0,  0, 0, 0],
   #                      [100, 0,  0, 0, 0],
   #                      [0,   0,  0, 0, 0],
   #                      [0,   0,  0, 0, 0]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([[0,   0,  0,  0,   0],
   #                      [0,   0,  0,  0,   0],
   #                      [0,   0,  0,  0, 100],
   #                      [0,   0,  0,  0,   0],
   #                      [0,   0,  0,  0,   0]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 03: pass')
   #
   #  def test_hw09_prob01_ut04(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 04 ************')
   #      M1 = np.array([[10, 0, 0],
   #                      [0, 0, 0],
   #                      [0, 0, 0]],
   #                     dtype=float)
   #      M2 = np.array([[0,  0, 0, 0, 0],
   #                     [10, 0, 0, 0, 0],
   #                     [0,  0, 0, 0, 0],
   #                     [0,  0, 0, 0, 0],
   #                     [0,  0, 0, 0, 0]],
   #                    dtype=float)
   #      M12 = np.array([[0, 0, 0, 0,   0, 0, 0],
   #                      [0, 0, 0, 0,   0, 0, 0],
   #                      [0, 0, 0, 0,   0, 0, 0],
   #                      [0, 0, 0, 0, 100, 0, 0],
   #                      [0, 0, 0, 0,   0, 0, 0],
   #                      [0, 0, 0, 0,   0, 0, 0],
   #                      [0, 0, 0, 0,   0, 0, 0]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([[0, 0,   0,  0,  0, 0, 0],
   #                      [0, 0,   0,  0,  0, 0, 0],
   #                      [0, 0,   0,  0,  0, 0, 0],
   #                      [0, 0, 100,  0,  0, 0, 0],
   #                      [0, 0,   0,  0,  0, 0, 0],
   #                      [0, 0,   0,  0,  0, 0, 0],
   #                      [0, 0,   0,  0,  0, 0, 0]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 04: pass')
   #
   #  def test_hw09_prob01_ut05(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 05 ************')
   #      M1 = np.array([[10, 0,  0],
   #                     [0,  0,  0],
   #                     [0,  0, 10]],
   #                    dtype=float)
   #      M2 = np.array([[0,  0,  0, 0,  0],
   #                     [10, 0,  0, 0,  0],
   #                     [0,  0,  0, 0,  0],
   #                     [0,  0,  0, 0,  0],
   #                     [0,  0,  0, 0,  0]],
   #                    dtype=float)
   #      M12 = np.array([[0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,  100,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,  100],
   #                      [0,  0,  0,  0,    0,  0,    0]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([[0,   0,   0,  0,    0,  0,  0],
   #                      [100, 0,   0,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0],
   #                      [0,   0, 100,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 05: pass')
   #
   #  def test_hw09_prob01_ut06(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 06 ************')
   #      M1 = np.array([[10, 0,  0],
   #                     [0,  0,  0],
   #                     [0,  0,  5]],
   #                    dtype=float)
   #      M2 = np.array([[0,  0,  0, 0,  0],
   #                     [10, 0,  0, 0,  0],
   #                     [0,  0,  0, 0,  0],
   #                     [0,  0,  0, 0,  0],
   #                     [0,  0,  0, 0,  0]],
   #                    dtype=float)
   #      M12 = np.array([[0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,  100,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,    0],
   #                      [0,  0,  0,  0,    0,  0,   50],
   #                      [0,  0,  0,  0,    0,  0,    0]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([[0,   0,   0,  0,    0,  0,  0],
   #                      [50,  0,   0,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0],
   #                      [0,   0, 100,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0],
   #                      [0,   0,   0,  0,    0,  0,  0]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 06: pass')
   #
   #  def test_hw09_prob01_ut07(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 07 ************')
   #      M1 = np.array([[1,   2,  3,  4],
   #                     [5,   6,  7,  8],
   #                     [9,  10, 11, 12],
   #                     [13, 14, 15, 16],
   #                     [17, 18, 19, 20]],
   #                    dtype=float)
   #      M2 = np.array([[21, 22],
   #                     [23, 24],
   #                     [25, 26]],
   #                    dtype=float)
   #      M12 = np.array([[26,   77,   128,  179,  100],
   #                      [154, 352,   450,  548,  292],
   #                      [376, 809,   950, 1091,  568],
   #                      [664, 1373, 1514, 1655,  844],
   #                      [952, 1937, 2078, 2219, 1120],
   #                      [694, 1404, 1494, 1584,  796],
   #                      [374,  753,  796,  839,  420]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([[420,   839,  796,  753, 374],
   #                      [796,  1584, 1494, 1404, 694],
   #                      [1120, 2219, 2078, 1937, 952],
   #                      [844,  1655, 1514, 1373, 664],
   #                      [568,  1091,  950,  809, 376],
   #                      [292,   548,  450,  352, 154],
   #                      [100,   179,  128,   77,  26]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 07: pass')
   #
   #  def test_hw09_prob01_ut08(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 08 ************')
   #      M1 = np.array([[26,    77,   128,    179,    100],
   #                     [154,   352,  450,    548,    292],
   #                     [376,   809,  950,   1091,    568],
   #                     [664,   1373, 1514,  1655,    844],
   #                     [952,   1937, 2078,  2219,   1120],
   #                     [694,   1404, 1494,  1584,    796],
   #                     [374,    753,  796,   839,    420]],
   #                    dtype=float)
   #      M2 = np.array([[420,    839,  796,  753,  374],
   #                     [796,   1584,  1494, 1404, 694],
   #                     [1120,  2219,  2078, 1937, 952],
   #                     [844,   1655,  1514, 1373, 664],
   #                     [568,   1091,   950,  809, 376],
   #                     [292,    548,   450,  352, 154],
   #                     [100,    179,   128,   77,  26]],
   #                    dtype=float)
   #      M12 = np.array([
   #          [676,      4004,      12585,      29020,      49150,      61224,      57641,      35800,      10000],
   #          [8008,     42020,     117032,     243040,     371592,     416756,     360936,     214136,      58400],
   #          [43268,    208388,    532746,    1030328,    1483800,    1567436,    1289090,     741576,     198864],
   #          [150336,   687528,    1660690,   3053440,    4214932,    4265696,    3373090,    1892824,     500512],
   #          [395392,   1746040,   4049451,   7168660,    9590910,    9408644,    7223859,    3975680,    1039520],
   #          [828632,   3553536,   7953682,   13605136,   17704748,   16911384,   12657938,    6846872,    1772064],
   #          [1390000,  5838064,   12727509,  21200484,   26994626,   25250228,   18517165,    9873896,    2533520],
   #          [1901336,  7860448,   16786882,  27366144,   34223500,   31457816,   22672194,   11939464,    3040096],
   #          [2109184,  8629672,   18176875,  29195300,   36049918,   32724244,   23286835,   12148656,    3075168],
   #          [1818048,  7388760,   15425234,  24536720,   30042260,   27041776,   19077026,    9887240,    2492000],
   #          [1193732,  4831340,   10031938,  15864184,   19322472,   17301492,   12139546,    6265048,    1574416],
   #          [519112,   2095356,    4336784,   6834496,    8298232,    7406796,    5180144,    2666248,     668640],
   #          [139876,    563244,    1162417,   1826348,    2211310,    1968208,    1372561,     704760,     176400]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([
   #          [176400,     704760,    1372561,    1968208,    2211310,    1826348,    1162417,     563244,     139876],
   #          [668640,    2666248,    5180144,    7406796,    8298232,    6834496,    4336784,    2095356,     519112],
   #          [1574416,   6265048,   12139546,   17301492,   19322472,   15864184,   10031938,    4831340,    1193732],
   #          [2492000,   9887240,   19077026,   27041776,   30042260,   24536720,   15425234,    7388760,    1818048],
   #          [3075168,   12148656,  23286835,   32724244,   36049918,   29195300,   18176875,    8629672,    2109184],
   #          [3040096,   11939464,  22672194,   31457816,   34223500,   27366144,   16786882,    7860448,    1901336],
   #          [2533520,   9873896,   18517165,   25250228,   26994626,   21200484,   12727509,    5838064,    1390000],
   #          [1772064,   6846872,   12657938,   16911384,   17704748,   13605136,    7953682,    3553536,     828632],
   #          [1039520,   3975680,    7223859,    9408644,    9590910,    7168660,    4049451,    1746040,     395392],
   #          [500512,    1892824,    3373090,    4265696,    4214932,    3053440,    1660690,     687528,     150336],
   #          [198864,     741576,    1289090,    1567436,    1483800,    1030328,     532746,     208388,      43268],
   #          [58400,      214136,     360936,     416756,     371592,     243040,     117032,      42020,       8008],
   #          [10000,       35800,      57641,      61224,      49150,      29020,      12585,       4004,        676]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 08: pass')
   #
   #  def test_hw09_prob01_ut09(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 09 ************')
   #      M1 = np.array([
   #          [74,   65,    5,   97,   78],
   #          [58,   22,   77,   70,    2],
   #          [63,    1,   67,   50,   87],
   #          [15,   95,   25,   68,   33],
   #          [94,   34,   61,   49,   43]],
   #                    dtype=float)
   #      M2 = np.array([[23,   91,   14],
   #                     [29,   39,   85],
   #                     [69,   30,   57]],
   #                    dtype=float)
   #      M12 = np.array([
   #          [4218,    5925,    7341,   10164,    7701,    9033,    5382],
   #          [9596,   11405,   14157,   18143,   18085,   10745,    2400],
   #          [9557,   13723,   24968,   17828,   26249,   17497,    7855],
   #          [7022,   13993,   17285,   26566,   25103,   12317,    4846],
   #          [7515,   19165,   19726,   23299,   21621,   16997,    5925],
   #          [8200,    9251,   18577,   12942,   14560,    7665,    2006],
   #          [1316,    9030,    6110,    7019,    6464,    5040,     989]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([
   #          [989,    5040,    6464,    7019,    6110,    9030,    1316],
   #          [2006,   7665,   14560,   12942,   18577,    9251,    8200],
   #          [5925,   16997,   21621,   23299,   19726,   19165,    7515],
   #          [4846,   12317,   25103,   26566,   17285,   13993,    7022],
   #          [7855,   17497,   26249,   17828,   24968,   13723,    9557],
   #          [2400,   10745,   18085,   18143,   14157,   11405,    9596],
   #          [5382,    9033,    7701,   10164,    7341,    5925,    4218]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 09: pass')
   #
   #  def test_hw09_prob01_ut10(self):
   #      print('\n***** CS3430: S20: HW09: Problem 01: Unit Test 10 ************')
   #      M1 = np.array(
   #          [[93, 70, 70, 15, 31],
   #           [26, 19, 79, 88, 52],
   #           [95, 44, 68, 66, 67],
   #           [10, 12, 76, 89, 71],
   #           [ 4, 13, 56, 47, 49]],
   #          dtype=float)
   #      M2 = np.array(
   #          [[28, 29, 86, 45, 42],
   #           [46,  7,  7, 36, 90],
   #           [27, 42, 22, 44, 79],
   #           [25,  4, 77, 29, 38],
   #           [41, 30, 26, 95, 99]],
   #          dtype=float)
   #      M12 = np.array([
   #          [9207,   15765,   15998,   12745,   12227,    8305,    4126,    1545,    1271],
   #          [6108,    9708,   22153,   25853,   26806,   14461,   11428,    5667,    2907],
   #          [17740,   24479,   29593,   33901,   41323,   27524,   16043,    8831,    4884],
   #          [15024,  18858,   37219,   41840,   50283,   33214,   25270,   13164,    7416],
   #          [14527,   19840,   42351,   53721,   59222,   36640,   28460,   16233,    8853],
   #          [10584,   11346,   24343,   34486,   47437,   32292,   26008,   14233,    7680],
   #          [5206,    8766,   25432,   29902,   34063,   22051,   18760,   11709,    6465],
   #          [780,    2268,   10128,   14845,   20920,   16472,   14063,    7056,    4242],
   #          [168,     726,    3281,    5728,    9478,    8235,    7145,    2737,    1372]],
   #                     dtype=float)
   #      C12 = direct_corr(M1, M2)
   #      print('C12:')
   #      print(C12)
   #      assert self.__comp_mats(C12, M12)
   #      M21 = np.array([
   #          [1372,    2737,    7145,    8235,    9478,    5728,    3281,     726,     168],
   #          [4242,    7056,   14063,   16472,   20920,   14845,   10128,    2268,     780],
   #          [6465,   11709,   18760,   22051,   34063,   29902,   25432,    8766,    5206],
   #          [7680,   14233,   26008,   32292,   47437,   34486,   24343,   11346,   10584],
   #          [8853,   16233,   28460,   36640,   59222,   53721,   42351,   19840,   14527],
   #          [7416,   13164,   25270,   33214,   50283,   41840,   37219,   18858,   15024],
   #          [4884,    8831,   16043,   27524,   41323,   33901,   29593,   24479,   17740],
   #          [2907,    5667,   11428,   14461,   26806,   25853,   22153,    9708,    6108],
   #          [1271,    1545,    4126,    8305,   12227,   12745,   15998,   15765,    9207]],
   #                     dtype=float)
   #      C21 = direct_corr(M2, M1)
   #      assert self.__comp_mats(C21, M21)
   #      print('C21:')
   #      print(C21)
   #      print('CS 3430: S20: HW09: Problem 01: Unit Test 10: pass')
   #
   # # ================ Problem 2: Unit Tests =====================
   #
   #  def test_hw09_prob02_ut01(self):
   #      """
   #      create and persist a dictionary of rgb histograms with 8 bins per color channel.
   #      """
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 01 ************')
   #      HIST_INDEX = {}
   #      hist_index_img_dir(Assign09UnitTests.IMGDIR, 'rgb', 8, Assign09UnitTests.PICDIR + 'rgb_hist8.pck')
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 01: pass')
   #
   #  def test_hw09_prob02_ut02(self):
   #      '''
   #      create and persist a dictionary of rgb histograms with 16 bins per color channel.
   #      '''
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 02 ************')
   #      HIST_INDEX = {}
   #      hist_index_img_dir(Assign09UnitTests.IMGDIR, 'rgb', 16, Assign09UnitTests.PICDIR + 'rgb_hist16.pck')
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 02: pass')
   #
   #  def test_hw09_prob02_ut03(self):
   #      '''
   #      create and persist a dictionary of hsv histograms with 8 bins per color channel.
   #      '''
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 03 ************')
   #      HIST_INDEX = {}
   #      hist_index_img_dir(Assign09UnitTests.IMGDIR, 'hsv', 8, Assign09UnitTests.PICDIR + 'hsv_hist8.pck')
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 03: pass')
   #
   #
   #  def test_hw09_prob02_ut04(self):
   #      '''
   #      create and persist a dictionary of hsv histograms with 16 bins per color channel.
   #      '''
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 04 ************')
   #      HIST_INDEX = {}
   #      hist_index_img_dir(Assign09UnitTests.IMGDIR, 'hsv', 16, Assign09UnitTests.PICDIR + 'hsv_hist16.pck')
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 04: pass')
   #
   #  def test_hw09_prob02_ut05(self):
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 05 ************')
   #      hist_index = load_hinx(Assign09UnitTests.PICDIR + 'rgb_hist8.pck')
   #      assert len(hist_index) == 318
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 05: pass')
   #
   #  def test_hw09_prob02_ut06(self):
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 06 ************')
   #      hist_index = load_hinx(Assign09UnitTests.PICDIR + 'rgb_hist16.pck')
   #      assert len(hist_index) == 318
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 06: pass')
   #
   #  def test_hw09_prob02_ut07(self):
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 07 ************')
   #      hist_index = load_hinx(Assign09UnitTests.PICDIR + 'hsv_hist8.pck')
   #      assert len(hist_index) == 318
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 07: pass')
   #
   #  def test_hw09_prob02_ut08(self):
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 08 ************')
   #      hist_index = load_hinx(Assign09UnitTests.PICDIR + 'hsv_hist16.pck')
   #      assert len(hist_index) == 318
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 08: pass')
   #
   #  '''
   #  ***** CS3430: S20: HW09: Problem 02: Unit Test 09 ************
   #  /home/vladimir/teaching/CS3430/hist_indexing/hist_test/food_test/img01.JPG
   #  /home/vladimir/teaching/CS3430/hist_indexing/images/123461762.JPG --> 2.6907286450397976
   #  /home/vladimir/teaching/CS3430/hist_indexing/images/123465049.JPG --> 2.6331934205607297
   #  /home/vladimir/teaching/CS3430/hist_indexing/images/123472255.JPG --> 2.435314836443297
   #  CS 3430: S20: HW09: Problem 02: Unit Test 09: pass
   #  '''
   #  def test_hw09_prob02_ut09(self):
   #      print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 09 ************')
   #      hist_index = load_hinx(Assign09UnitTests.PICDIR + 'rgb_hist8.pck')
   #      assert len(hist_index) == 318
   #      imgpath = Assign09UnitTests.TSTDIR + 'food_test/img01.JPG'
   #      print(imgpath)
   #      top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'inter')
   #      for imagepath, sim in top_matches:
   #          print(imagepath + ' --> ' + str(sim))
   #      inimg = cv2.imread(imgpath)
   #      # show_images(inimg, top_matches)
   #      del hist_index
   #      print('CS 3430: S20: HW09: Problem 02: Unit Test 09: pass')
#
#     '''
# ***** CS3430: S20: HW09: Problem 02: Unit Test 10 ************
# /home/vladimir/teaching/CS3430/hist_indexing/hist_test/food_test/img10.JPG
# /home/vladimir/teaching/CS3430/hist_indexing/images/123461665.JPG --> 0.358401979729111
# /home/vladimir/teaching/CS3430/hist_indexing/images/123461663.JPG --> 0.4183549743015625
# /home/vladimir/teaching/CS3430/hist_indexing/images/123465245.JPG --> 0.4538522441561253
#     '''
#     def test_hw09_prob03_ut10(self):
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 10 ************')
#         hist_index = load_hinx(Assign09UnitTests.PICDIR + 'rgb_hist16.pck')
#         assert len(hist_index) == 318
#         imgpath = Assign09UnitTests.TSTDIR + 'food_test/img10.JPG'
#         print(imgpath)
#         top_matches = find_sim_rgb_images(imgpath,
#                                           16, hist_index, 'bhatta')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         inimg = cv2.imread(imgpath)
#         # show_images(inimg, top_matches)
#         del hist_index
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 10 ************')
#
#     '''
# ***** CS3430: S20: HW09: Problem 02: Unit Test 11 ************
# /home/vladimir/teaching/CS3430/hist_indexing/hist_test/car_test/img05.png
# /home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_09_01_orig.png --> 0.3659495045040523
# /home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_09_03_orig.png --> 0.3200399230998757
# /home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_08_58_orig.png --> 0.3068581002198671
#     '''
#     def test_hw09_prob03_ut11(self):
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 11 ************')
#         hist_index = load_hinx(Assign09UnitTests.PICDIR + 'hsv_hist8.pck')
#         assert len(hist_index) == 318
#         imgpath = Assign09UnitTests.TSTDIR + 'car_test/img05.png'
#         print(imgpath)
#         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'correl')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         inimg = cv2.imread(imgpath)
#         # show_images(inimg, top_matches)
#         del hist_index
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 11 ************')
#
#     '''
# ***** CS3430: S20: HW09: Problem 02: Unit Test 12 ************
# /home/vladimir/teaching/CS3430/hist_indexing/hist_test/car_test/img01.png
# /home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_17_50_orig.png --> 5.9975637325067295
# /home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_20_51_orig.png --> 5.9980997660608875
# /home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_20_56_orig.png --> 5.998143128606088
# ***** CS3430: S20: HW09: Problem 02: Unit Test 12 ************
#     '''
#     def test_hw09_prob03_ut12(self):
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 12 ************')
#         hist_index = load_hinx(Assign09UnitTests.PICDIR + 'hsv_hist16.pck')
#         assert len(hist_index) == 318
#         imgpath = Assign09UnitTests.TSTDIR + 'car_test/img01.png'
#         print(imgpath)
#         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'chisqr')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         inimg = cv2.imread(imgpath)
#         # show_images(inimg, top_matches)
#         del hist_index
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 12 ************')
#
#     '''
# ***** CS3430: S20: HW09: Problem 02: Unit Test 13 ************
# /home/vladimir/teaching/CS3430/hist_indexing/hist_test/car_test/img01.png
# /home/vladimir/teaching/CS3430/hist_indexing/images/16_07_02_14_21_00_orig.png --> 0.08744988403664498
# /home/vladimir/teaching/CS3430/hist_indexing/images/16_07_02_14_21_02_orig.png --> 0.1834899764322775
# /home/vladimir/teaching/CS3430/hist_indexing/images/16_07_02_14_21_06_orig.png --> 0.24857992030143786
# ***** CS3430: S20: HW09: Problem 02: Unit Test 13 ************
#     '''
#     def test_hw09_prob03_ut13(self):
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 13 ************')
#         hist_index = load_hinx(Assign09UnitTests.PICDIR + 'rgb_hist16.pck')
#         assert len(hist_index) == 318
#         imgpath = Assign09UnitTests.TSTDIR + 'car_test/img01.png'
#         print(imgpath)
#         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'chisqr')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         inimg = cv2.imread(imgpath)
#         # show_images(inimg, top_matches)
#         del hist_index
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 13 ************')
#
    '''
***** CS3430: S20: HW09: Problem 02: Unit Test 14 ************
/home/vladimir/teaching/CS3430/hist_indexing/hist_test/car_test/img23.png
/home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_16_45_orig.png --> 0.08932323211804039
/home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_16_43_orig.png --> 0.15907225275945305
/home/vladimir/teaching/CS3430/hist_indexing/images/17_02_21_22_16_44_orig.png --> 0.1632962909435258
***** CS3430: S20: HW09: Problem 02: Unit Test 14 ************
    '''
    def test_hw09_prob03_ut14(self):
        print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 14 ************')
        hist_index = load_hinx(Assign09UnitTests.PICDIR + 'rgb_hist16.pck')
        assert len(hist_index) == 318
        imgpath = Assign09UnitTests.TSTDIR + 'car_test/img23.png'
        print(imgpath)
        top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'bhatta')
        for imagepath, sim in top_matches:
            print(imagepath + ' --> ' + str(sim))
        inimg = cv2.imread(imgpath)
        # show_images(inimg, top_matches)
        del hist_index
        print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 14 ************')
#
#     '''
# ***** CS3430: S20: HW09: Problem 02: Unit Test 15 ************
# /home/vladimir/teaching/CS3430/hist_indexing/hist_test/car_test/img11.png
# /home/vladimir/teaching/CS3430/hist_indexing/images/16_07_02_14_31_43_orig.png --> 0.04729543743626675
# /home/vladimir/teaching/CS3430/hist_indexing/images/16_07_02_14_31_45_orig.png --> 0.06488649037748359
# /home/vladimir/teaching/CS3430/hist_indexing/images/16_07_02_14_31_46_orig.png --> 0.08840490376529722
# ***** CS3430: S20: HW09: Problem 02: Unit Test 15 ************
#     '''
#     def test_hw09_prob03_ut15(self):
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 15 ************')
#         hist_index = load_hinx(Assign09UnitTests.PICDIR + 'rgb_hist8.pck')
#         assert len(hist_index) == 318
#         imgpath = Assign09UnitTests.TSTDIR + 'car_test/img11.png'
#         print(imgpath)
#         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'bhatta')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         inimg = cv2.imread(imgpath)
#         # show_images(inimg, top_matches)
#         del hist_index
#         print('\n***** CS3430: S20: HW09: Problem 02: Unit Test 15 ************')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
