#!/usr/bin/python

#######################################################
# module: cs3430_s20_hw08.py
# Connor Osborne
# A01880782
########################################################

import math
from PIL import Image
import numpy as np


def lumin(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    """
    Convert rgb pixel to grayscale value.
    """
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]


def is_in_pil_range(pil_img, cr):
    """
    Check if 2-tuple cr references to a legal pixel in a PIl image pil_img
    """
    ncols, nrows = pil_img.size
    c, r = cr
    # print('ncols={}; nrows={}'.format(ncols, nrows))
    # print('c={}; r={}'.format(c, r))
    return c > 0 and c < ncols-1 and r > 0 and r < nrows-1


def display_pil_img_row(pil_img, r):
    """
    Prints pixel values in row r in a PIL image pil_img.
    Useful for debugging.
    """
    ncols, _ = pil_img.size
    for c in range(ncols):
        print(pil_img.getpixel((c, r)))


def display_pil_img_col(pil_img, c):
    """
    Prints pixel values in column c in a PIL image pil_img.
    Useful for debugging.
    """
    _, nrows = pil_img.size
    for r in range(nrows):
        print(pil_img.getpixel((c, r)))


# ================ Problem 01 =================================

# Remember: in PIL images, c = x, r = y
def pil_pix_dxdy(pil_img, cr, default_delta):
    """
    Returns dx, dy values for pixel (c, r) in PIL image pil_img.
    If the luminosity values of the horizontal neighbors are the same,
    dx = default_delta.
    If the luminosity values of the vertical neighbors are the same,
    dy = default_delta.
    """
    assert is_in_pil_range(pil_img, cr)
    pil_img = pil_img.convert('RGB')
    dx = default_delta
    dy = default_delta

    pixelx1 = pil_img.getpixel((cr[0]+1, cr[1]))
    pixelx2 = pil_img.getpixel((cr[0]-1, cr[1]))
    if lumin(pixelx1)-lumin(pixelx2) != 0:
        dx = lumin(pixelx1)-lumin(pixelx2)

    pixely1 = pil_img.getpixel((cr[0], cr[1] + 1))
    pixely2 = pil_img.getpixel((cr[0], cr[1] - 1))
    if lumin(pixely2)-lumin(pixely1) != 0:
        dy = lumin(pixely2)-lumin(pixely1)

    return dx, dy


def grd_magn(dx, dy):
    """
    Gradient magnitude given dx and dy.
    """
    mag = math.sqrt(dx**2 + dy**2)
    return mag


def grd_deg_theta(dx, dy):
    """
    Gradient orientation (in degrees) given dx and dy.
    """
    theta = math.degrees(math.atan(dy/dx))
    return theta


def depil(pil_img, default_delta=1.0, magn_thresh=20):
    """
    - detects edges in a PIL image pil_img.
    - returns a new binary PIL image where the pixel
    value 255 means that it's a edge pixel and 0 means
    that it's not an edge pixel.
    - default_delta is used in calls to pil_pix_dxdy
    - magn_thresh is a gradient magnitude threshold, i.e.,
    if the computed value is >= magn_thresh, the pixel
    is an edge pixel; otherwise, it's not.
    """
    output_img = Image.new('L', pil_img.size)
    num_cols, num_rows = pil_img.size
    for i in range(1, num_cols-1):
        for j in range(1, num_rows-1):
            cr = (i, j)
            dx, dy = pil_pix_dxdy(pil_img, cr, default_delta)
            mag = grd_magn(dx, dy)
            deg = grd_deg_theta(dx, dy)
            assert abs(deg) <= 180
            if mag >= magn_thresh:
                pixval = 255
            else:
                pixval = 0
            output_img.putpixel((i, j), pixval)
    return output_img

# ================ Problem 02 =================================


def ht(pil_img, angle_step=1, pix_val_thresh=5):
    num_cols, num_rows = pil_img.size
    xmod = int(num_cols/2)
    ymod = int(num_rows/2)
    maxrho = math.sqrt(num_rows**2 + num_cols**2)
    table = np.zeros((360, int(maxrho)))
    for i in range(1, num_cols-1):
        for j in range(1, num_rows-1):
            cr = (i, j)
            pixval = pil_img.getpixel(cr)
            if pixval >= pix_val_thresh:
                for th in range(0, 360, angle_step):
                    rho = int(((i-xmod) * math.cos(th)) + ((j-ymod) * math.sin(th)))
                    if rho > 0:
                        table[th, rho] += 1
    return table


def ht_find_lines(htb, spl=1):
    """
    - Returns a list of all lines in the hough transform table htb if
    with rhos >= 0 and support level >= spl.
    - Each line is represented as a 3-tuple (rho, angle, spl), 
    where angle is given in degrees.
    """
    lines = []
    thetas, rhos = htb.shape
    for th in range(thetas):
        for r in range(1, rhos):
            if htb[th, r] >= spl:
                lines.append((r, th, int(htb[th, r])))
    return lines
