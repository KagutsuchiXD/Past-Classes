import argparse
import cv2

#####################################################################
# module: blurring.py
# author: vladimir kulyukin
# description: use canny edge detection	
# To run: python cv_detect_edges -ip <input_path> -op <output_path>
#####################################################################

'''
ap = argparse.ArgumentParser()
ap.add_argument('-ip', '--input_path', required=True, help='path to input image')
ap.add_argument('-op', '--output_path', required=True, help='path to output image')
args    = vars(ap.parse_args())
'''

dp = '/home/vladimir/teaching/CS3430/S20/lectures/lec15/py/img/'
fp01 = dp + 'elephant.jpg'
fp02 = dp + 'EdgeImage_01_gd_ed.jpg'
fp03 = dp + 'EdgeImage_02.jpg'
fp04 = dp + 'horline.png'
fp05 = dp + 'verline.png'

def detectEdgesWithoutBlur(input_path, output_path):
    image = cv2.imread(input_path)
    gray_image  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_edges = cv2.Canny(gray_image, 100, 200, apertureSize=3, L2gradient=True)
    cv2.imshow('Input', image)
    cv2.imshow('Gray Image', gray_image)
    cv2.imshow('Edges', image_edges)
    cv2.waitKey(0)
    cv2.imwrite(output_path, image_edges)
    del gray_image
    del image_edges

def detectEdgesWithBlur(input_path, output_path, gauss_blur_mask):
    image = cv2.imread(input_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, gauss_blur_mask, 0)
    image_edges = cv2.Canny(blurred_image, 100, 200, apertureSize=3, L2gradient=True)
    cv2.imshow('Input', image)
    cv2.imshow('Gray Image', gray_image)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.imshow('Edges', image_edges)
    cv2.waitKey(0)
    cv2.imwrite(output_path, image_edges)
    del image
    del gray_image
    del blurred_image
    del image_edges

if __name__ == '__main__':
    detectEdgesWithoutBlur(dp + 'EdgeImage_01.jpg', dp + 'EdgeImage_01_edg_cv_woblur.jpg')
    detectEdgesWithBlur(dp + 'EdgeImage_01.jpg', dp + 'EdgeImage_01_edg_cv_wblur.png', (3, 3))
    
    detectEdgesWithoutBlur(dp + 'EdgeImage_02.jpg', dp + 'EdgeImage_02_edg_cv_woblur.jpg')
    detectEdgesWithBlur(dp + 'EdgeImage_02.jpg', dp + 'EdgeImage_02_edg_cv_wblur.png', (3, 3))
    
    detectEdgesWithoutBlur(dp + 'EdgeImage_03.jpg', dp + 'EdgeImage_03_edg_cv_woblur.jpg')
    detectEdgesWithBlur(dp + 'EdgeImage_03.jpg', dp + 'EdgeImage_03_edg_cv_wblur.png', (3, 3))
    
    detectEdgesWithoutBlur(dp + 'verline.png', dp + 'verline_edg_cv_woblur.png')
    detectEdgesWithBlur(dp + 'verline.png', dp + 'verline_edg_cv_wblur.png', (3, 3))
    
    detectEdgesWithoutBlur(dp + 'horline.png', dp + 'horline_edg_cv_woblur.png')
    detectEdgesWithBlur(dp + 'horline.png', dp + 'horline_edg_cv_wblur.png', (3, 3))
    
    detectEdgesWithoutBlur(dp + 'verline.png', dp + 'verline_edg_cv_wblur.png')
    detectEdgesWithBlur(dp + 'verline.png', dp + 'verline_edg_cv_woblur.png', (3, 3))

    detectEdgesWithoutBlur(dp + 'elephant.jpg', dp + 'elephant_edg_cv_woblur.jpg')
    detectEdgesWithBlur(dp + 'elephant.jpg', dp + 'elephant_edg_cv_wblur.jpg', (3, 3))

    detectEdgesWithoutBlur(dp + 'june.jpg', dp + 'june_edg_cv_woblur.jpg')
    detectEdgesWithBlur(dp + 'june.jpg', dp + 'june_edg_cv_wblur.jpg', (3, 3))

    detectEdgesWithoutBlur(dp + 'truck.jpg', dp + 'truck_edg_cv_woblur.jpg')
    detectEdgesWithBlur(dp + 'truck.jpg', dp + 'truck_edg_cv_wblur.jpg', (3, 3))
    
    pass


