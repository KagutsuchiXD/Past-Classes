#!/usr/bin/python

################################
# module: image_retrieval.py
# Connor Osborne
# A01880782
#################################

import cv2
import sys
import os
import pickle
from matplotlib import pyplot as plt
from os.path import basename


def show_images(input_image, match_list):
    # show image 1
    inrgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    fig1 = plt.figure(1)
    fig1.suptitle('Input Image')
    plt.imshow(inrgb)

    # show matched image 1
    # print('match 1 ' + match_list[0][0])
    retimg1 = cv2.imread(match_list[0][0])
    simscore1 = match_list[0][1]
    retimg1 = cv2.cvtColor(retimg1, cv2.COLOR_BGR2RGB)
    fig2 = plt.figure(2)
    fig2.suptitle('Matched Image 1: ' + basename(match_list[0][0]) + '; Sim = ' + str(simscore1))
    plt.imshow(retimg1)

    # show matched image 2
    # print('match 2 ' + match_list[1][0])
    retimg2 = cv2.imread(match_list[1][0])
    simscore2 = match_list[1][1]
    retimg2 = cv2.cvtColor(retimg2, cv2.COLOR_BGR2RGB)
    fig3 = plt.figure(3)
    fig3.suptitle('Matched Image 2: ' + basename(match_list[1][0]) + '; Sim = ' + str(simscore2))
    plt.imshow(retimg2)

    # show matched image 3
    # print('match 3 ' + match_list[2][0])
    # retimg3 = cv2.imread(match_list[2][0])
    # simscore3 = match_list[2][1]
    # retimg3 = cv2.cvtColor(retimg3, cv2.COLOR_BGR2RGB)
    # fig4 = plt.figure(4)
    # fig4.suptitle('Matched Image 3: ' + basename(match_list[2][0]) + '; Sim = ' + str(simscore3))
    # plt.imshow(retimg3)

    plt.show()


def find_sim_rgb_images(imgpath, num_bins, hist_index, hist_sim):
    assert num_bins == 8 or num_bins == 16
    img = cv2.imread(imgpath)
    hist = cv2.calcHist([img], [0, 1, 2], None, [num_bins, num_bins, num_bins], [0, 256, 0, 256, 0, 256])
    hist1 = cv2.normalize(hist, hist).flatten()
    if hist_sim is 'inter':
        matchlist = [('init1', -1), ('init2', -1), ('init3', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_INTERSECT)
            if value > matchlist[0][1] and value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value > matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'correl':
        matchlist = [('init1', -1), ('init2', -1), ('init3', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CORREL)
            if value > matchlist[0][1] and value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value > matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'chisqr':
        matchlist = [('init1', 1000), ('init2', 1000), ('init3', 1000)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CHISQR)
            if value < matchlist[0][1] and value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value < matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'bhatta':
        matchlist = [('init1', 1), ('init2', 1), ('init3', 1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_BHATTACHARYYA)
            if key.find('17_02_21_22_16_43_orig') != -1:
                print("expected value at images/17_02_21_22_16_43_orig.png: ")
                print(value)
                print(matchlist)
            if value < matchlist[0][1] and value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value < matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist


def find_sim_hsv_images(imgpath, num_bins, hist_index, hist_sim):
    assert num_bins == 8 or num_bins == 16
    img = cv2.imread(imgpath)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv_img], [0, 1, 2], None, [num_bins, num_bins, num_bins], [0, 180, 0, 256, 0, 256])
    hist1 = cv2.normalize(hist, hist).flatten()
    if hist_sim is 'inter':
        matchlist = [('init1', -1), ('init2', -1), ('init3', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_INTERSECT)
            if value > matchlist[0][1] and value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value > matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'correl':
        matchlist = [('init1', -1), ('init2', -1), ('init3', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CORREL)
            if value > matchlist[0][1] and value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1] and value > matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value > matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'chisqr':
        matchlist = [('init1', 1000), ('init2', 1000), ('init3', 1000)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CHISQR)
            if value < matchlist[0][1] and value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value < matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'bhatta':
        matchlist = [('init1', 1), ('init2', 1), ('init3', 1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_BHATTACHARYYA)
            if value < matchlist[0][1] and value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1] and value < matchlist[2][1]:
                matchlist[1] = (key, value)
            elif value < matchlist[2][1]:
                matchlist[2] = (key, value)
        show_images(img, matchlist)
        return matchlist


def load_hinx(pick_path):
    with open(pick_path, 'rb') as histfile:
        return pickle.load(histfile)
