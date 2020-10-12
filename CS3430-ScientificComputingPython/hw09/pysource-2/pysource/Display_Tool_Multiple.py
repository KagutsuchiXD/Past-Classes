import glob
import sys
import os.path
import multiprocessing

import numpy as np
import scipy.misc
import matplotlib.pyplot as pl
import matplotlib.patches as pt
import matplotlib.image as mpltimg
from scipy import ndimage
from skimage import filters, io
from builtins import range
import math

def display_vector_field(filename, frame, on_img=False, image_name='None', window_size=32, scaling_factor=1, **kw):
    """ Displays quiver plot of the data stored in the file


    Parameters
    ----------
    filename :  string
        the absolute path of the text file

    on_img : Bool, optional
        if True, display the vector field on top of the image provided by image_name

    image_name : string, optional
        path to the image to plot the vector field onto when on_img is True

    window_size : int, optional
        when on_img is True, provide the interogation window size to fit the background image to the vector field

    scaling_factor : float, optional
        when on_img is True, provide the scaling factor to scale the background image to the vector field

    Key arguments   : (additional parameters, optional)
        *scale*: [None | float]
        *width*: [None | float]


    See also:
    ---------
    matplotlib.pyplot.quiver


    Examples
    --------
    --- only vector field
    >>> openpiv.tools.display_vector_field('./exp1_0000.txt',scale=100, width=0.0025)

    --- vector field on top of image
    >>> openpiv.tools.display_vector_field('./exp1_0000.txt', on_img=True, image_name='exp1_001_a.bmp', window_size=32, scaling_factor=70, scale=100, width=0.0025)

    """
    TESTED_VIDEO = "Tested_Video/"
    NAME = filename
    a = np.loadtxt(filename)
    fig = pl.figure()
    if on_img:  # plot a background image
        im = imread(image_name)
        im = negative(im)  # plot negative of the image for more clarity
        imsave('neg.tif', im)
        im = mpltimg.imread('neg.tif')
        xmax = np.amax(a[:, 0]) + window_size / (2 * scaling_factor)
        ymax = np.amax(a[:, 1]) + window_size / (2 * scaling_factor)
        implot = pl.imshow(im, origin='lower', cmap="Greys_r", extent=[0., xmax, 0., ymax])
    invalid = a[:, 4].astype('bool')
    fig.canvas.set_window_title('Vector field, ' + str(np.count_nonzero(invalid)) + ' wrong vectors')
    valid = ~invalid
    # array_element_count = len(a)
    # a = remove_long_vectors(a, array_element_count)
    # pl.quiver(a[invalid, 0], a[invalid, 1], a[invalid, 2], a[invalid, 3], color='r', **kw)
    # pl.quiver(a[valid, 0], a[valid, 1], a[valid, 2], a[valid, 3], color='b', **kw)
    pl.quiver(a[invalid, 0], a[invalid, 1], a[invalid, 2], a[invalid, 3], color='r', **kw)
    pl.quiver(a[valid, 0], a[valid, 1], a[valid, 2], a[valid, 3], color='b', **kw)
    ##################################
    pl.draw()
    pl.savefig('image_edge-'+str(frame)+'.png',dpi=150)
    pl.close('all')
    #################################

    # array_element_count = len(a)
    # upward_estimate, downward_estimate, lateral_estimate, array_element_count = get_vector_estimate_right(a,array_element_count)
    # return upward_estimate, downward_estimate, lateral_estimate, array_element_count
    #######################################
    # print_all_vectors(valid, a, count - 1)
    # print_valid_vectors(valid,a, count-1)


def remove_long_vectors(a, array_element_count):
    for i in range(0, array_element_count, 1):
        if a[i][4] != 1:
            scaling_u = a[i][2] * 0.0003 * 2396.52
            scaling_v = a[i][3] * 0.0003 * 2396.52
            vector_magnitude = math.sqrt((scaling_u) ** 2 + (scaling_v) ** 2)
            if vector_magnitude >= 40 or vector_magnitude <= 1:
                a[i][2] = 0
                a[i][3] = 0
    return a

def get_vector_estimate_right(a, array_element_count):
    lateral_count = 0
    upward_count = 0
    downward_count = 0
    upward_estimate = 0
    downward_estimate = 0
    lateral_estimate = 0

    for i in range(0, array_element_count, 1):
        if a[i][4] != 1:
            angle = (np.arctan2(a[i][3], a[i][2]) * 180 / np.pi)
            if 0 < angle <= 10:
                lateral_count = lateral_count + 1
            elif 11 <= angle <= 170:
                upward_count = upward_count + 1
            elif 171 <= angle <= 180:
                lateral_count = lateral_count + 1
            elif -10 <= angle < 0:
                lateral_count = lateral_count + 1
            elif -170 <= angle <= -11:
                downward_count = downward_count + 1
            elif -179 <= angle <= -171:
                lateral_count = lateral_count + 1
        if ((lateral_count + upward_count + downward_count) != 0):
            upward_estimate = upward_count
            downward_estimate = downward_count
            lateral_estimate = lateral_count
            # upward_estimate = ((upward_count / ((float)(array_element_count)))*100)
            # downward_estimate = ((downward_count / ((float)(array_element_count)))*100)
            # lateral_estimate = ((lateral_count / ((float)(array_element_count)))*100)
        else:
            upward_estimate = 0
            downward_estimate = 0
            lateral_estimate = 0

    return upward_estimate,downward_estimate,lateral_estimate, array_element_count



def x_axis_term_count(valid_y_array):
    first_term = valid_y_array[0]
    count = 0
    for i in range(0,len(valid_y_array) -1):
        if valid_y_array[i]==first_term:
            count = count +1
        else:
            break
    return count

# def print_all_vectors(valid, a, count):
#     j2 = 0
#     for i in range(0, len(a[valid, 0]), count):
#         if (i != 0):
#             z = i + j2 - 0
#             # print (z), a[valid, 0][z], a[valid, 1][z], a[valid, 2][z], a[valid, 3][z], (
#             #                 np.arctan2(a[valid, 3][z], a[valid, 2][z]) * 180 / np.pi)
#             j2 = j2 + 1
#
#
# def print_valid_vectors(valid, a, count):
#     # print ('valid vectors \n')
#     j1 = 0
#     for i in range(0, len(a[valid, 0]), count):
#         if (i != 0):
#             z = i + j1 - 0
#             if (np.abs(a[valid, 2][z] - a[valid, 3][z]) > 0.5):
#                 # print (z), a[valid, 0][z], a[valid, 1][z], a[valid, 2][z], a[valid, 3][z], (
#                 #             np.arctan2(a[valid, 3][z], a[valid, 2][z]) * 180 / np.pi)
#             j1 = j1 + 1

def imread(filename, flatten=0):
    """Read an image file into a numpy array
    using skimage.io.imread

    Parameters
    ----------
    filename :  string
        the absolute path of the image file
    flatten :   bool
        True if the image is RGB color or False (default) if greyscale

    Returns
    -------
    frame : np.ndarray
        a numpy array with grey levels


    Examples
    --------

    >>> image = openpiv.tools.imread( 'image.bmp' )
    >>> print image.shape
        (1280, 1024)


    """

    return io.imread(filename, as_grey=True)


def imsave(filename, arr):
    """Write an image file from a numpy array
    using scipy.misc.imread

    Parameters
    ----------
    filename :  string
        the absolute path of the image file that will be created
    arr : 2d np.ndarray
        a 2d numpy array with grey levels

    Example
    --------

    >>> image = openpiv.tools.imread( 'image.bmp' )
    >>> image2 = openpiv.tools.negative(image)
    >>> imsave( 'negative-image.tif', image2)

    """

    if np.amax(arr) < 256 and np.amin(arr) >= 0:
        scipy.misc.imsave(filename, arr)
    else:
        raise ValueError('please provide a 2d array of grey levels (value in [0, 255])')


def negative(image):
    """ Return the negative of an image

    Parameter
    ----------
    image : 2d np.ndarray of grey levels

    Returns
    -------
    (255-image) : 2d np.ndarray of grey levels

    """
    return (255 - image)
