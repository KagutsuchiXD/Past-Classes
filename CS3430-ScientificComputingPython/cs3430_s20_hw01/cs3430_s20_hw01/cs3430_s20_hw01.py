######################################################
# module: cs3430_s20_hw01.py
# YOUR NAME
# YOUR A-NUMBER
######################################################

import numpy as np
import numpy.linalg
import random

### ============= Problem 1 (Gauss-Jordan Elimination) ===============

def gje(a, b):
    """ Gauss-Jordan Elimination to solve Ax = b. """
    ## your code here
    pass

## ============== Problem 2 (Determinant) ========================

def random_mat(nr, nc, lower, upper):
    """ Generate an nrxnc matrix of random numbers in [lower, upper]. """
    m = np.zeros((nr, nc))
    for r in range(nr):
        for c in range(nc):
            m[r][c] = random.randint(lower, upper)
    return m

def leibniz_det(a):
    """ Compute determinant of nxn matrix a with Leibniz formula. """
    ## your code here
    pass

def gauss_det(a):
    """ Compute determinant of nxn matrix a with Gaussian elimination. """
    ### your code here
    pass

## ============== Problem 3 (Cramer's Rule) ======================

def cramer(A, b):
    """ Solve Ax = b with Cramer's Rule. """
    pass

if __name__ == '__main__':
    pass



    
    
              
