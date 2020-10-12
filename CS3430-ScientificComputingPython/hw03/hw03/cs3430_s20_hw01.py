######################################################
# module: cs3430_s20_hw01.py
# Connor Osborne
# A01880782
######################################################

import numpy as np
import numpy.linalg
import random

# ============= Problem 1 (Gauss-Jordan Elimination) ===============


def gje(a, b):
    """ Gauss-Jordan Elimination to solve Ax = b. """
    n = len(a)

    for col in range(n-1):  # loop through columns
        if a[col][col] == 0:  # if pivot is 0 loop through rows to find a row to swap with
            for i in range(col + 1, n):
                if a[i][col] != 0:
                    atemp = np.array(a[col, :])  # temporary to swap with
                    a[col, :] = a[col + 1, :]
                    a[col + 1, :] = atemp
                    btemp = np.array(b[col])
                    b[col] = b[col + 1]
                    b[col + 1] = btemp
                    break
        for row in range(col+1, n):  # loop through rows
            gm = a[row][col]/a[col][col]  # calculate gauss multiplier
            a[row, :] = a[row, :] - gm*a[col, :]
            b[row] = b[row] - gm*b[col]
    if np.array_equal(a[n-1, :], np.zeros(n)):  # if row of all 0s matrix has no solution
        print("This matrix has no solution")
        return None
    for col in range(n-1, 0, -1):  # go through in opposite direction to make reduced row echelon
        for row in range(col-1, -1, -1):
            gm = a[row][col]/a[col][col]
            a[row, :] = a[row, :] - gm*a[col, :]
            b[row] = b[row] - gm*b[col]
    x = np.zeros(n)
    for row in range(n):
        x[row] = b[row]/a[row][row]
    return x

# ============== Problem 2 (Determinant) ========================


def random_mat(nr, nc, lower, upper):
    """ Generate an nrxnc matrix of random numbers in [lower, upper]. """
    m = np.zeros((nr, nc))
    for r in range(nr):
        for c in range(nc):
            m[r][c] = random.randint(lower, upper)
    return m


def leibniz_det(a):
    """ Compute determinant of nxn matrix a with Leibniz formula. """
    if a.shape == (2, 2):
        return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])  # base case for recursion

    n = len(a)
    determinant = 0
    for column in range(n):
        atemp = np.delete(a, np.s_[0:1], axis=0)  # copy of a with correct column and row removed
        b = np.delete(atemp, np.s_[column:column+1], axis=1)
        if column % 2 == 0:  # if column number is even add to determinant, if odd subtract from determinant
            determinant += (a[0][column] * leibniz_det(b))
        else:
            determinant -= (a[0][column] * leibniz_det(b))
    return determinant


def gauss_det(a):
    """ Compute determinant of nxn matrix a with Gaussian elimination. """
    # use gauss elimination to get row reduced echelon form
    n = len(a)

    for col in range(n - 1):
        if a[col][col] == 0:
            for i in range(col + 1, n):
                if a[i][col] != 0:
                    atemp = np.array(a[col, :])
                    a[col, :] = a[col + 1, :]
                    a[col + 1, :] = atemp
                    break
        for row in range(col + 1, n):
            gm = a[row][col] / a[col][col]
            a[row, :] = a[row, :] - gm * a[col, :]
    if np.array_equal(a[n - 1, :], np.zeros(n)):
        return 0
    for col in range(n - 1, 0, -1):
        for row in range(col - 1, -1, -1):
            gm = a[row][col] / a[col][col]
            a[row, :] = a[row, :] - gm * a[col, :]
    det = float(1)  # initialize determinant
    for column in range(n):
        det *= a[column][column]  # multiply the pivots to get the determinant
    return det


# ============== Problem 3 (Cramer's Rule) ======================

def cramer(a, b):
    """ Solve Ax = b with Cramer's Rule. """
    n = len(a)
    x = np.zeros(n)
    for column in range(n):
        bk = np.array(a)  # copy of matrix a to be changed
        acopy = np.array(a)  # copy of a
        for row in range(n):
            bk[row][column] = b[row]  # replace column with column vector b
        x[column] = (gauss_det(bk)/gauss_det(acopy))  # calculate current value of x
    return x


if __name__ == '__main__':
    pass
