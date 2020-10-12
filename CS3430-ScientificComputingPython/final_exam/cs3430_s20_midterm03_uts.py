#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s20_midterm03_uts.py
# description: unit tests for CS 3430: S20: MIDTERM 03 (FINAL)
##############################################################

import unittest
import math
import numpy as np
import cv2
from midterm03_s20 import hinx_img_dir
from midterm03_s20 import load_hinx
from midterm03_s20 import find_sim_rgb_images, find_sim_hsv_images
from midterm03_s20 import bsubst, fsubst
from midterm03_s20 import do_simplex, display_solution_from_tab, get_solution_from_tab
from midterm03_s20 import dir_corr
from midterm03_s20 import build_huffman_tree_from_text
from midterm03_s20 import encode_moby_dick_ch03
from midterm03_s20 import learn_bin_id3_dt_from_csv_file
from midterm03_s20 import classify_csv_file_with_bin_id3_dt
from midterm03_s20 import display_bin_id3_node

class midterm03_s20_uts(unittest.TestCase):

    def __comp_mats(self, m1, m2, err=0.0001):
        if m1.shape != m2.shape:
            return False
        nr, nc = m1.shape
        for r in range(nr):
            for c in range(nc):
                if abs(m1[r,c] - m2[r,c]) > err:
                    print('{} {}'.format(m1[r,c], m2[r,c]))
                    return False
        return True

    # change these variales as you see fit. they're for the second problem's
    # unit tests.
    # IMGDIR is directory where images are saved.
    IMGDIR = 'hinx/img/'
    # PICDIR is directory where pickle files are saved.
    PICDIR = 'hinx/pck/'
    # TSTDIR is directory where test images are saved.
    TSTDIR = 'hinx/test/'

    # # ======================== Problem 1 =====================
    #
    # def test_midterm03_prob01_ut01(self):
    #     '''
    #     create and persist a dictionary of rgb histograms with 8 bins per color channel.
    #     '''
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 01: Unit Test 01 ************')
    #     hist_index = {}
    #     hinx_img_dir(midterm03_s20_uts.IMGDIR, hist_index, 'rgb', 8, midterm03_s20_uts.PICDIR + 'rgb_hist8.pck')
    #     assert len(hist_index) == 10
    #     print('CS 3430: S20: MIDTERM03: Problem 01: Unit Test 01: pass')
    #
    # def test_midterm03_prob01_ut02(self):
    #     '''
    #     create and persist a dictionary of rgb histograms with 16 bins per color channel.
    #     '''
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 01: Unit Test 02 ************')
    #     hist_index = {}
    #     hinx_img_dir(midterm03_s20_uts.IMGDIR, hist_index, 'rgb', 16, midterm03_s20_uts.PICDIR + 'rgb_hist16.pck')
    #     assert len(hist_index) == 10
    #     print('CS 3430: S20: MIDTERM03: Problem 01: Unit Test 02: pass')
    #
    # def test_midterm03_prob01_ut03(self):
    #     '''
    #     create and persist a dictionary of hsv histograms with 8 bins per color channel.
    #     '''
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 01: Unit Test 03 ************')
    #     hist_index = {}
    #     hinx_img_dir(midterm03_s20_uts.IMGDIR, hist_index, 'hsv', 8, midterm03_s20_uts.PICDIR + 'hsv_hist8.pck')
    #     assert len(hist_index) == 10
    #     print('CS 3430: S20: MIDTERM03: Problem 01: Unit Test 03: pass')
    #
    # def test_midterm03_prob01_ut04(self):
    #     '''
    #     create and persist a dictionary of hsv histograms with 16 bins per color channel.
    #     '''
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 01: Unit Test 04 ************')
    #     hist_index = {}
    #     hinx_img_dir(midterm03_s20_uts.IMGDIR, hist_index, 'hsv', 16, midterm03_s20_uts.PICDIR + 'hsv_hist16.pck')
    #     assert len(hist_index) == 10
    #     print('CS 3430: S20: MIDTERM03: Problem 01: Unit Test 04: pass')
    #
#     ### ====================== Problem 2 ==============================
#
#     """
# ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 01 ************
# hinx/test/test1.jpg
# similarity metric: inter
# hinx/img/img6.jpg --> 2.6241015265858323
# hinx/img/img10.jpg --> 1.9212639209071085
# similarity metric: correl
# hinx/img/img6.jpg --> 0.46133169483187464
# hinx/img/img10.jpg --> 0.25405138915865694
# similarity metric: chisqr
# hinx/img/img9.jpg --> 21.13220309863486
# hinx/img/img8.jpg --> 25.122591590634556
# similarity metric: bhatta
# hinx/img/img6.jpg --> 0.4639969990443348
# hinx/img/img10.jpg --> 0.6143115372112586
# CS 3430: S20: MIDTERM03: Problem 02: Unit Test 01: pass
#     """
#     def test_midterm03_prob02_ut01(self):
#         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 01 ************')
#         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'rgb_hist8.pck')
#         assert len(hist_index) == 10
#         imgpath = midterm03_s20_uts.TSTDIR + 'test1.jpg'
#         print(imgpath)
#         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'inter')
#         print('similarity metric: inter')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: correl')
#         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'correl')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: chisqr')
#         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'chisqr')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: bhatta')
#         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'bhatta')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         del hist_index
#         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 01: pass')
#
#     """
# ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 02 ************
# hinx/test/test1.jpg
# similarity metric: inter
# hinx/img/img6.jpg --> 3.6126040376209403
# hinx/img/img7.jpg --> 2.3348736308337266
# similarity metric: correl
# hinx/img/img6.jpg --> 0.3850049182824728
# hinx/img/img7.jpg --> 0.14619678849832404
# similarity metric: chisqr
# hinx/img/img6.jpg --> 200.98192012921248
# hinx/img/img8.jpg --> 263.624892014442
# similarity metric: bhatta
# hinx/img/img6.jpg --> 0.5509965847243383
# hinx/img/img7.jpg --> 0.6917197799035861
# CS 3430: S20: MIDTERM03: Problem 02: Unit Test 02: pass
#     """
#     def test_midterm03_prob02_ut02(self):
#         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 02 ************')
#         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'rgb_hist16.pck')
#         assert len(hist_index) == 10
#         imgpath = midterm03_s20_uts.TSTDIR + 'test1.jpg'
#         print(imgpath)
#         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'inter')
#         print('similarity metric: inter')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: correl')
#         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'correl')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: chisqr')
#         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'chisqr')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: bhatta')
#         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'bhatta')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         del hist_index
#         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 02: pass')
#
#     """
# ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 03 ************
# hinx/test/test1.jpg
# similarity metric: inter
# hinx/img/img6.jpg --> 2.797683347072706
# hinx/img/img7.jpg --> 1.5187115583273112
# similarity metric: correl
# hinx/img/img6.jpg --> 0.4555350986629035
# hinx/img/img7.jpg --> 0.09559583768980101
# similarity metric: chisqr
# hinx/img/img7.jpg --> 223.9691658927892
# hinx/img/img8.jpg --> 241.78071688749355
# similarity metric: bhatta
# hinx/img/img6.jpg --> 0.4958741918177958
# hinx/img/img7.jpg --> 0.687309668232793
# CS 3430: S20: MIDTERM03: Problem 02: Unit Test 03: pass
#     """
#     def test_midterm03_prob02_ut03(self):
#         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 03 ************')
#         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'hsv_hist8.pck')
#         assert len(hist_index) == 10
#         imgpath = midterm03_s20_uts.TSTDIR + 'test1.jpg'
#         print(imgpath)
#         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'inter')
#         print('similarity metric: inter')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: correl')
#         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'correl')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: chisqr')
#         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'chisqr')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: bhatta')
#         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'bhatta')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         del hist_index
#         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 03: pass')
#
#     """
# ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 04 ************
# hinx/test/test1.jpg
# similarity metric: inter
# hinx/img/img6.jpg --> 4.326301977875744
# hinx/img/img7.jpg --> 1.9984646056212796
# similarity metric: correl
# hinx/img/img6.jpg --> 0.34201560943635545
# hinx/img/img3.png --> 0.043152831401770494
# similarity metric: chisqr
# hinx/img/img8.jpg --> 625.415780324732
# hinx/img/img6.jpg --> 868.861158459009
# similarity metric: bhatta
# hinx/img/img6.jpg --> 0.5841156582978565
# hinx/img/img7.jpg --> 0.7438385662308902
# CS 3430: S20: MIDTERM03: Problem 02: Unit Test 04: pass
#     """
#     def test_midterm03_prob02_ut04(self):
#         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 04 ************')
#         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'hsv_hist16.pck')
#         assert len(hist_index) == 10
#         imgpath = midterm03_s20_uts.TSTDIR + 'test1.jpg'
#         print(imgpath)
#         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'inter')
#         print('similarity metric: inter')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: correl')
#         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'correl')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: chisqr')
#         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'chisqr')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         print('similarity metric: bhatta')
#         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'bhatta')
#         for imagepath, sim in top_matches:
#             print(imagepath + ' --> ' + str(sim))
#         del hist_index
#         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 04: pass')
    #
    #     """
    # ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 05 ************
    # hinx/test/test2.png
    # similarity metric: inter
    # hinx/img/img5.png --> 2.8180621260689804
    # hinx/img/img4.png --> 2.5222426153195556
    # similarity metric: correl
    # hinx/img/img5.png --> 0.9483604165164781
    # hinx/img/img4.png --> 0.793007585433665
    # similarity metric: chisqr
    # hinx/img/img5.png --> 1.790338009793387
    # hinx/img/img2.png --> 13.33412926685658
    # similarity metric: bhatta
    # hinx/img/img5.png --> 0.25729204021708424
    # hinx/img/img2.png --> 0.36066284988863256
    # CS 3430: S20: MIDTERM03: Problem 02: Unit Test 05: pass
    #     """
    #     def test_midterm03_prob02_ut05(self):
    #         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 05 ************')
    #         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'rgb_hist8.pck')
    #         assert len(hist_index) == 10
    #         imgpath = midterm03_s20_uts.TSTDIR + 'test2.png'
    #         print(imgpath)
    #         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'inter')
    #         print('similarity metric: inter')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: correl')
    #         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'correl')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: chisqr')
    #         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'chisqr')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: bhatta')
    #         top_matches = find_sim_rgb_images(imgpath, 8, hist_index, 'bhatta')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         del hist_index
    #         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 05: pass')
    #
    #     """
    # ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 06 ************
    # hinx/test/test2.png
    # similarity metric: inter
    # hinx/img/img5.png --> 4.009766881688847
    # hinx/img/img4.png --> 3.2205206580110826
    # similarity metric: correl
    # hinx/img/img5.png --> 0.8774324581737597
    # hinx/img/img4.png --> 0.5277467770846533
    # similarity metric: chisqr
    # hinx/img/img5.png --> 19.782000109165782
    # hinx/img/img2.png --> 21.596853664883255
    # similarity metric: bhatta
    # hinx/img/img5.png --> 0.36634952698503404
    # hinx/img/img2.png --> 0.464828706640273
    # CS 3430: S20: MIDTERM03: Problem 02: Unit Test 06: pass
    #     """
    #     def test_midterm03_prob02_ut06(self):
    #         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 06 ************')
    #         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'rgb_hist16.pck')
    #         assert len(hist_index) == 10
    #         imgpath = midterm03_s20_uts.TSTDIR + 'test2.png'
    #         print(imgpath)
    #         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'inter')
    #         print('similarity metric: inter')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: correl')
    #         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'correl')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: chisqr')
    #         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'chisqr')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: bhatta')
    #         top_matches = find_sim_rgb_images(imgpath, 16, hist_index, 'bhatta')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         del hist_index
    #         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 06: pass')
    #
    #     """
    # ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 07 ************
    # hinx/test/test2.png
    # similarity metric: inter
    # hinx/img/img5.png --> 3.664526556414785
    # hinx/img/img4.png --> 2.7471558254146657
    # similarity metric: correl
    # hinx/img/img5.png --> 0.9357585885389503
    # hinx/img/img4.png --> 0.7546162314879438
    # similarity metric: chisqr
    # hinx/img/img5.png --> 3.8071276804648804
    # hinx/img/img1.png --> 34.986431654232824
    # similarity metric: bhatta
    # hinx/img/img5.png --> 0.3301506931592557
    # hinx/img/img2.png --> 0.4836755962025602
    # CS 3430: S20: MIDTERM03: Problem 02: Unit Test 07: pass
    #     """
    #     def test_midterm03_prob02_ut07(self):
    #         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 07 ************')
    #         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'hsv_hist8.pck')
    #         assert len(hist_index) == 10
    #         imgpath = midterm03_s20_uts.TSTDIR + 'test2.png'
    #         print(imgpath)
    #         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'inter')
    #         print('similarity metric: inter')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: correl')
    #         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'correl')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: chisqr')
    #         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'chisqr')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: bhatta')
    #         top_matches = find_sim_hsv_images(imgpath, 8, hist_index, 'bhatta')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         del hist_index
    #         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 07: pass')
    #
    #     """
    # ***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 08 ************
    # hinx/test/test2.png
    # similarity metric: inter
    # hinx/img/img5.png --> 4.87349258071481
    # hinx/img/img4.png --> 3.697892627613328
    # similarity metric: correl
    # hinx/img/img5.png --> 0.8240127644977583
    # hinx/img/img4.png --> 0.6983599597784991
    # similarity metric: chisqr
    # hinx/img/img5.png --> 17.84560183425219
    # hinx/img/img1.png --> 66.82984811897128
    # similarity metric: bhatta
    # hinx/img/img5.png --> 0.42648079314495196
    # hinx/img/img2.png --> 0.5661007847937081
    # CS 3430: S20: MIDTERM03: Problem 02: Unit Test 08: pass
    #     """
    #     def test_midterm03_prob02_ut08(self):
    #         print('\n***** CS3430: S20: MIDTERM03: Problem 02: Unit Test 08 ************')
    #         hist_index = load_hinx(midterm03_s20_uts.PICDIR + 'hsv_hist16.pck')
    #         assert len(hist_index) == 10
    #         imgpath = midterm03_s20_uts.TSTDIR + 'test2.png'
    #         print(imgpath)
    #         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'inter')
    #         print('similarity metric: inter')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: correl')
    #         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'correl')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: chisqr')
    #         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'chisqr')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         print('similarity metric: bhatta')
    #         top_matches = find_sim_hsv_images(imgpath, 16, hist_index, 'bhatta')
    #         for imagepath, sim in top_matches:
    #             print(imagepath + ' --> ' + str(sim))
    #         del hist_index
    #         print('CS 3430: S20: MIDTERM03: Problem 02: Unit Test 08: pass')
    #
    # # ====================== Problem 3 =============================
    #
    # def test_midterm03_prob03_ut01(self):
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 03: Unit Test 01 ************')
    #     A = np.array([[1, 3, -1],
    #                   [0, 2, 6],
    #                   [0, 0, -15]],
    #                  dtype=float)
    #     b = np.array([[-4, 11],
    #                   [10, -5],
    #                   [-30, 50]],
    #                  dtype=float)
    #     x = bsubst(A, 3, b, 2)
    #     gt = np.array([[  1., -14.83333333],
    #                    [ -1.,  7.5],
    #                    [  2.,  -3.33333333]])
    #     assert self.__comp_mats(x, gt, err=0.0001)
    #     print('CS 3430: S20: MIDTERM03: Problem 03: Unit Test 01: pass')
    #
    # def test_midterm03_prob03_ut02(self):
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 03: Unit Test 02 ************')
    #     A = np.array([[1, 0, 0],
    #                   [2, 1, 0],
    #                   [-1, 3, 1]],
    #                  dtype=float)
    #     b = np.array([[-4, -10],
    #                   [2, 4],
    #                   [4, 8]],
    #                  dtype=float)
    #     x = fsubst(A, 3, b, 2)
    #     gt = np.array([[-4., -10.],
    #                    [10.,  24.],
    #                    [-30., -74.]])
    #     assert self.__comp_mats(x, gt, err=0.0001)
    #     print('CS 3430: S20: MIDTERM03: Problem 03: Unit Test 02: pass')
    #
    # # ====================== Problem 4 =============================
    #
    # def test_midterm03_prob04_ut01(self):
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 04: Unit Test 01 ************')
    #     in_vars = {0:3, 1:4}
    #     m = np.array([[2,    2,   3, 1, 0, 160],
    #                   [5,    1,  10, 0, 1, 100],
    #                   [-10, -6,  -2, 0, 0, 0]],
    #                  dtype=float)
    #     tab = (in_vars, m)
    #     tab, solved = do_simplex(tab)
    #     assert solved is True
    #     err = 0.0001
    #     sol = get_solution_from_tab(tab)
    #     print(sol)
    #     assert abs(sol[0] - 5.0) <= err
    #     assert abs(sol[1] - 75.0) <= err
    #     assert abs(sol['p'] - 500.0) <= err
    #     print('in_vars = {}'.format(in_vars))
    #     print('tab = {}'.format(tab[1]))
    #     display_solution_from_tab(tab)
    #     print('CS 3430: S20: MIDTERM03: Problem 04: Unit Test 01: pass')
    #
    # # ====================== Problem 5 =============================
    #
    # def test_midterm03_prob05_ut01(self):
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 05: Unit Test 01 ************')
    #     M1 = np.array([[162., 118., 111., 133.],
    #                    [ 64.,  37.,  33., 165.],
    #                    [ 38.,   4., 107.,  86.],
    #                    [ 98.,  35.,  67., 107.]])
    #     M2 = np.array([[28, 29, 86, 45, 42],
    #                    [46,  7,  7, 36, 90],
    #                    [27, 42, 22, 44, 79],
    #                    [25,  4, 77, 29, 38],
    #                    [41, 30, 26, 95, 99]],
    #                   dtype=float)
    #     C12 = dir_corr(M1, M2)
    #     gtC12 = np.array([[16038., 27072., 26411., 31640., 25703., 11626.,  8541.,  5453.],
    #                       [12492.,  18925., 28560., 40359., 37193., 20432.,  9610., 10090.],
    #                       [18992., 23718., 36741., 55046., 39328., 30146., 17035., 11242.],
    #                       [30782., 36220., 40629., 63554., 53785., 26528., 22834., 17110.],
    #                       [19290., 24040., 49226., 64454., 51047., 36925., 18242., 16311.],
    #                       [13850., 13239., 27584., 41626., 29047., 23831., 17536., 11465.],
    #                       [10416.,  8556., 15918., 22846., 23326., 13439.,  9321.,  7330.],
    #                       [ 4116.,  5880., 12817., 13361., 14336., 12125.,  4979.,  2996.]])
    #     assert self.__comp_mats(C12, gtC12, err=0.0001)
    #     print(C12)
    #     print(gtC12)
    #
    #     C21 = dir_corr(M2, M1)
    #     gtC21 = np.array([[ 2996.,  4979., 12125., 14336., 13361., 12817.,  5880.,  4116.],
    #                       [ 7330.,  9321., 13439., 23326., 22846., 15918.,  8556., 10416.],
    #                       [11465., 17536., 23831., 29047., 41626., 27584., 13239., 13850.],
    #                       [16311., 18242., 36925., 51047., 64454., 49226., 24040., 19290.],
    #                       [17110., 22834., 26528., 53785., 63554., 40629., 36220., 30782.],
    #                       [11242., 17035., 30146., 39328., 55046., 36741., 23718., 18992.],
    #                       [10090.,  9610., 20432., 37193., 40359., 28560., 18925., 12492.],
    #                       [ 5453.,  8541., 11626., 25703., 31640., 26411., 27072., 16038.]])
    #     assert self.__comp_mats(C12, gtC12, err=0.0001)
    #     print(C21)
    #     print(gtC21)
    #     print('CS 3430: S20: MIDTERM03: Problem 05: Unit Test 01: pass')
    #
    # ### ====================== Problem 6 =============================
    # ### No UTs for this problem. Simply define the appropriate variables with your values in midterm03_s20.py
    # ### and state how you've computed them.
    #
    # ### ====================== Problem 7 =============================
    # ### No UTs for this problem. Simply define the appropriate variables with your values in midterm03_s20.py
    # ### and state how you've computed them.
    #
    #
    # ### ====================== Problem 8 =============================
    #
    # def test_midterm03_prob08_ut01(self):
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 08: Unit Test 01 ************')
    #     txt = 'aababbcdefghaaaaa'
    #     ht = build_huffman_tree_from_text(txt)
    #     cdefg = set(['c', 'd', 'e', 'f', 'g', 'h'])
    #     for c in txt:
    #         enc = ht.encodeSymbol(c)
    #         if c == 'a':
    #             assert len(enc) == 1
    #         elif c == 'b':
    #             assert len(enc) == 3
    #         elif c in cdefg:
    #             assert len(enc) == 4
    #         else:
    #             raise Exception('unknown character {}'.format(c))
    #         print('encoding({}) = {}'.format(c, enc))
    #         dec = ht.decode(enc)
    #         assert c == dec
    #         assert enc == ht.encodeSymbol(ht.decode(enc))
    #     print('CS 3430: S20: MIDTERM03: Problem 08: Unit Test 01: pass')

    # Place HuffmanTree.py, CharFreqMap.py and hw12_BinHuffmanTree.py into
    # the current directory to run this test.
    def test_midterm03_prob08_ut02(self):
        print('\n***** CS3430: S20: MIDTERM03: Problem 08: Unit Test 02 ************')
        from HuffmanTree import HuffmanTree
        from CharFreqMap import CharFreqMap
        from hw12_BinHuffmanTree import BinHuffmanTree
        encode_moby_dick_ch03()
        filename = 'moby_dick_ch03'
        ext = '.txt'
        filepath = filename + ext
        cfm1 = CharFreqMap.computeCharFreqMap(filepath)
        nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm1)
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
        bht = BinHuffmanTree(root=ht.getRoot())
        with open(filepath, 'r', encoding='utf-8') as inf:
            data = inf.read()
            dec0 = bht.decodeTextFromFile(filename)
            assert dec0 == data
        print('CS 3430: S20: MIDTERM03: Problem 08: Unit Test 02: pass')

    # # ====================== Problem 9 =============================
    #
    # def test_midterm03_prob09_ut01(self):
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 09: Unit Test 01 ************')
    #     dt_root = learn_bin_id3_dt_from_csv_file('train_data.csv', 'Class')
    #     assert not dt_root is None
    #     display_bin_id3_node(dt_root)
    #     print('CS 3430: S20: MIDTERM03: Problem 09: Unit Test 01: pass')
    #
    # def test_midterm03_prob09_ut02(self):
    #     print('\n***** CS3430: S20: MIDTERM03: Problem 09: Unit Test 02 ************')
    #     dt_root = learn_bin_id3_dt_from_csv_file('train_data.csv', 'Class')
    #     acc = classify_csv_file_with_bin_id3_dt(dt_root, 'test_data.csv', 'Class')
    #     print('classification accuracy = {}'.format(acc))
    #     assert acc >= 0.9
    #     print('CS 3430: S20: MIDTERM03: Problem 09: Unit Test 02: pass')
    #
    # # ====================== Problem 10 =============================
    # # No UTs for Problem 10.

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
