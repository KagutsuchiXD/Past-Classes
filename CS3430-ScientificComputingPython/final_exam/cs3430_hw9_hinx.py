################################
# module: cs3430_hw9_hinx.py
# Connor Osborne
# A01880782
################################

import argparse
import cv2
import sys
import os
import re
import pickle
import numpy as mp
import matplotlib as plt


def generate_file_names(fnpat, rootdir):
    """
      generate all the files in directory rootdir that match regular expression fnpat.
      """
    for path, dirlist, filelist in os.walk(rootdir):
        for file_name in filelist:
            if not file_name.startswith('.') and not re.match(fnpat, file_name) is None:
                yield os.path.join(path, file_name)
        for d in dirlist:
            generate_file_names(fnpat, d)


# Global dictionary of flattened and normalized image historgrams
HIST_INDEX = {}


def hist_index_img(imgp, color_space, num_bins=8):
    """
      imgp is a path to an rgb image file (e.g., '/images/17_02_21_22_11_12_orig.png';
      color_space is either 'rgb' or 'hsv';
      num_bins is the number of bins per color channel in each histogram.
      This function reads an image from imgp wtih cv2.imread(imgp) and
      converts the image to the hsv color space with cv2.cvtColor() if necessary.
      Then cv2.calcHist() is used to compute the image's histogram of the specified bin_size for each channel.
      The histogram is normalized and flattened.
      The normalized and flattened historgram is saved in HIST_INDEX under the key imgp.
      """
    global HIST_INDEX
    img = cv2.imread(imgp)

    if color_space == 'hsv':
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv_img], [0, 1, 2], None, [num_bins, num_bins, num_bins], [0, 180, 0, 256, 0, 256])
    else:
        # blu_histo_256 = cv2.calcHist([img], [0], None, [256], [0, 256])
        # grn_histo_256 = cv2.calcHist([img], [1], None, [256], [0, 256])
        # red_histo_256 = cv2.calcHist([img], [2], None, [256], [0, 256])
        hist = cv2.calcHist([img], [0, 1, 2], None, [num_bins, num_bins, num_bins], [0, 256, 0, 256, 0, 256])
    fin_hist = cv2.normalize(hist, hist).flatten()
    HIST_INDEX[imgp] = fin_hist




def hist_index_img_dir(imgdir, color_space, num_bins, pick_file):
    """
      Uses hist_index_img() to index all jpg, png, JPG images in directory imgdir.
      The color_space and bin_size arguments are as in hist_index_img. The
      argument pick_file specifies the path to a pickle file where
      the HIST_INDEX dictionary is persisted.
      """
    print('Indexing {}...'.format(imgdir))
    for imgp in generate_file_names(r'.+\.(jpg|png|JPG)', imgdir):
        print('indexing ' + imgp)
        hist_index_img(imgp, color_space, num_bins=num_bins)
        print(imgp + ' indexed')
    with open(pick_file, 'wb') as histpick:
        pickle.dump(HIST_INDEX, histpick)
    print('indexing finished')
