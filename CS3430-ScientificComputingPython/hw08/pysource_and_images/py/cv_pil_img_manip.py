####################################################
# module: cv_pil_img_manip.py
# description: image manipulation w/ OpenCV and PIL
# bugs to vladimir dot kulyukin at usu dot edu
####################################################

import argparse
import cv2
from  PIL import Image
from matplotlib import pyplot as plt    

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to image')
ap.add_argument('-r', '--row', required=True, help = 'row number to display')
ap.add_argument('-c', '--col', required=True, help = 'col number to display')
args = vars(ap.parse_args())

def set_cv2_img_row_dsc(img, r, pix_val):
    '''
    Set each pixel in row r in OpenCV image img to pix_val (destructive)
    '''
    _, w, _ = img.shape
    for c in range(w):
        img[r,c] = pix_val

def set_cv2_img_col_dsc(img, c, pix_val):
    '''
    Set each pixel in col c in OpenCV image img to pix_val (destructive)
    '''
    h, _, _ = img.shape
    for r in range(h):
        img[r,c] = pix_val

def set_pil_img_row_dsc(img, r, pix_val):
    """
    Set each pixel in row r in PIL image img to pix_val (destructive)
    """
    w, _ = img.size
    for c in range(w):
        img.putpixel((c, r), pix_val)

def set_pil_img_col_dsc(img, c, pix_val):
    """
    Set each pixel in col r in PIL image img to pix_val (destructive)
    """
    _, h = img.size
    for r in range(h):
        img.putpixel((c, r), pix_val)

def set_cv2_img_row_col(img_path, r, c, row_pix_val, col_pix_val):
    ## 1. read an image
    img = cv2.imread(img_path)
    ## 2. show the image
    cv2.imshow('Original CV2 Image', img)
    ## 3. make a copy of the image
    img2 = img.copy()
    ## 4. modify a row in the image's copy
    set_cv2_img_row_dsc(img2, r, row_pix_val)
    ## 5. modify a column in the image's copy
    set_cv2_img_col_dsc(img2, c, col_pix_val)
    ## 6. show the modified image
    cv2.imshow('Modified CV2 Image', img2)
    cv2.waitKey()
    ## 7. save the modified image
    cv2.imwrite('img/cv2_temp.jpg', img2)
    del img
    del img2
    cv2.destroyAllWindows()

def set_pil_img_row_col(img_path, r, c, row_pix_val, col_pix_val):
    ## 1. read in an image
    img = Image.open(img_path)
    ## 2. show the image
    fig1 = plt.figure(1)
    fig1.suptitle('Original PIL Image')
    plt.imshow(img)
    ## 3. make a copy of the image
    img2 = img.copy()
    ## 4. modify a row in the image's copy
    set_pil_img_row_dsc(img2, r, row_pix_val)
    ## 5. modify a column in the image's copy
    set_pil_img_col_dsc(img2, c, col_pix_val)
    ## 6. show the modified image
    fig2 = plt.figure(2)
    fig2.suptitle('Modified PIL Image')
    plt.imshow(img2)
    ## 7. save the modified image
    img2.save('img/pil_temp.jpg')
    del img
    del img2
    plt.show()

if __name__ == '__main__':
    set_cv2_img_row_col(args['image'], int(args['row']), int(args['col']), (255,255,255), (0, 0, 255))
    set_pil_img_row_col(args['image'], int(args['row']), int(args['col']), (255,255,255), (255, 0, 0))
    pass
    
