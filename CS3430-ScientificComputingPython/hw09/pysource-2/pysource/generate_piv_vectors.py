# from openpiv import tools, process, scaling, validation, filters, pyprocess, preprocess
# from Display_Tool_Multiple import display_vector_field
from piv_functions import extended_search_area_piv, get_coordinates
from openpiv import tools, validation, filters, scaling
import numpy as np
import pickle
import os
import sys
#from collections import defaultdict
import csv
import json
from matplotlib.image import imsave as _imsave, imread as _imread
from skimage.transform import resize
from Display_Tool_Multiple import display_vector_field
from skimage import io

def imread(filename, flatten=0):
    img = io.imread( filename, as_grey = True)
    img = resize(img, (720, 1280))
    return img

def generateVectors():
    for i in range(9,10,1):
        frame_number = i
        next_frame_number = (i+1)

        frame_a  = imread( 'FRAMES/'+str(frame_number)+'.png')
        frame_b  = imread( 'FRAMES/'+str(next_frame_number)+'.png')

        ### we can change overlap to 45.
        u, v, sig2noise = extended_search_area_piv( frame_a , frame_b, corr_method='fft',
                                                              window_size=64, overlap=32,
                                                              dt=0.033,
                                                              sig2noise_method='peak2peak')
        x, y = get_coordinates( image_size=frame_a.shape, window_size=64, overlap=32)

        u, v, mask = validation.sig2noise_val( u, v, sig2noise, threshold = 0.05 )
        # u, v, mask = validation.global_std( u, v, std_threshold = 3 )
        #
        u, v = filters.replace_outliers( u, v, method='localmean', max_iter=15, kernel_size=2)
        x, y, u, v = scaling.uniform(x, y, u, v, scaling_factor = 396.52 )

        tools.save(x, y, u, v, mask, 'image_edge-'+str(frame_number)+'.txt' )

        ## we can change the scale factor.
        display_vector_field('image_edge-' + str(frame_number) + '.txt',
                             frame=frame_number, scale=80, width=0.0025)

if __name__== '__main__':
    generateVectors()
