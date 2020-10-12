
#################################################
# Module: cs3430_s20_hw02.py
# Connor Osborne
# A01880782
# bugs to vladimir dot kulyukin at usu dot edu
#################################################

import numpy as np
import pickle
import os


def comp_2d_mats(a, b, err=0.0001):
    """
    Compare two matrices a and b. Returns true if
    a and b are of the same shape and, for every
    legitimate position (i, j), abs(a[i][j] - b[i][j]) <= err.
    """
    ra, ca = a.shape
    rb, cb = b.shape
    if ra != rb:
        return False
    if ca != cb:
        return False
    for r in range(ra):
        for c in range(ca):
            if abs(a[r][c] - b[r][c]) > err:
                return False
    return True


def lu_decomp(a, n):
    """ 
    lu_decomp(a, n) returns u, l such that np.dot(l, u) === a.
    a is an nxn matrix that is reduced to the upper and lower triangular matrices. 
    throws exception when there is no pivot in a column or rows must be swapped
    to create a pivot.
    lu_decomp(a, n) is destructive in that a is destructively modified into u.
    """
    lower = np.eye(n, n)
    upper = np.copy(a)
    for col in range(n-1):  # loop through columns
        if upper[col][col] == 0:  # if pivot is 0 loop through rows to find a row to swap with
            print("Cannot use LU Decomposition for the matrix A")
            return None
        for row in range(col+1, n):  # loop through rows
            gm = upper[row][col]/upper[col][col]  # calculate gauss multiplier
            upper[row, :] = upper[row, :] - gm*upper[col, :]
            lower[row][col] = gm  # store gm in lower
    return upper, lower


def check_lin_sys_sol(a, n, b, m, x, err=0.0001):
    ra, ca = a.shape
    assert ra == n
    assert ca == n
    assert b.shape[0] == n
    assert b.shape[1] == m
    assert b.shape == x.shape
    for c in range(m):
        bb = np.array([np.matmul(a, x[:,c])]).T
        for r in range(n):
            assert abs(b[r][c] - bb[r][0]) <= err


def test_lud_solve(a, n, b, m, err=0.0001, prnt_flag=True):
    x = lud_solve(a, n, b, m)
    check_lin_sys_sol(a, n, b, m, x, err=err)
    if prnt_flag:
        print('A:')
        print(a)
        print('b:')
        print(b)
        print('x:')
        print(x)
        print('A*x:')
        print(np.dot(a, x))


def test_lud_solve2(a, n, b, m, err=0.0001, prnt_flag=True):
    aa = a.copy()
    u, l = lu_decomp(aa, n)
    bb = b.copy()
    x = lud_solve2(u, l, n, bb, m)
    print(x)
    check_lin_sys_sol(a, n, b, m, x, err=err)
    if prnt_flag:
        print('A:')
        print(a)
        print('b:')
        print(b)
        print('x:')
        print(x)
        print('A*x:')
        print(np.dot(a, x))


def bsubst(a, n, b, m):
    """
    bsubst uses back substitution to solve ax = b1, b2, ..., bm.
    a is an nxn upper-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm. 
    returns x.
    """
    x = np.zeros((n, m),)
    upper = np.copy(a)
    for vec in range(m):  # loop through each column vector in x and b
        x[n-1][vec] = b[n-1][vec] / upper[n-1][n-1]  # base case(initial variable for x)
        for i in range(n-2, -1, -1):
            bb = 0
            for j in range(i+1, n):  # add up each preceding ax pairing
                bb += upper[i][j]*x[j][vec]
            x[i][vec] = (b[i][vec] - bb) / upper[i][i]  # solve for current x value
    return x


def fsubst(a, n, b, m):
    """
    fsubst uses forward substitution to solve ax = b1, b2, ..., bm.
    a is an nxn lower-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm.
    returns x.
    """
    x = np.zeros((n, m))
    lower = np.copy(a)
    for vec in range(m):  # loop through each column vector in x and b
        x[0][vec] = b[0][vec] / lower[0][0]  # base case(initial variable for x)
        for i in range(1, n):
            bb = 0
            for j in range(i):  # add up each preceding ax pairing
                bb += lower[i][j]*x[j][vec]
            x[i][vec] = (b[i][vec] - bb) / lower[i][i]  # solve for current x value
    return x


def lud_solve(a, n, b, m):
    """
    a is an nxn matrix; b is m nx1 vectors.
    Use forward subst to solve Ly = b for y.
    Use back    subst to solve Ux = y for x.
    Then LUx = Ly = b.
    Returns x.
    """
    upper, lower = lu_decomp(a, n)  # use lu_decomp() to initialize u and l

    y = fsubst(lower, n, b, m)  # Use forward subst to solve Ly = b for y.

    x = bsubst(upper, n, y, m)  # Use back subst to solve Ux = y for x.

    return x


def lud_solve2(u, l, n, b, m):
    """
    Uses L to transform b to c.
    Then backsubst to solve Ux = c for x.
    Returns x.
    """
    for col in range(n-1):
        for row in range(col + 1, n):
            b[row, :] = b[row] - l[row][col]*b[col]
    x = bsubst(u, n, b, m)  # Use back subst to solve Ux = y for x.
    return x


def load_lin_systems(file_name):
    with open(file_name, 'rb') as fp:
        return pickle.load(fp)


def test_lud_solve_on_lin_systems(file_name, err=0.0001):
    print('Testing LUD on {} ...'.format(file_name))
    lu_problems = []
    lin_systems = load_lin_systems(file_name)
    for A, b in lin_systems:
        try:
            test_lud_solve(A, A.shape[0], b, 1, err=err, prnt_flag=False)
        except Exception as e:
            print(e)
            lu_problems.append((A, b))
    print('{} LUD solve failures out of {}'.format(len(lu_problems), len(lin_systems)))
