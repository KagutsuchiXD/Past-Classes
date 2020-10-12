
####################################
# module: cs3430_s20_hw04.py
# Connor Osborne
# A01880782
####################################

import numpy as np


# ============== Problem 1 ==================

def simplex(tab):
    """
    Apply the simplex algorithm to the tableaue tab.
    """
    invars, matrix = tab[0], tab[1]
    nr, nc = matrix.shape

    is_solved = False
    while is_solved == False:
        entcol = 0
        deprow = 0
        departinglist = []
        mostneg = 0
        pivot = 0
        smallestans = float('inf')
        if min(matrix[nr - 1]) >= 0:
            return tab, True
        for col in range(nc - 1):
            if matrix[nr - 1][col] < mostneg:
                mostneg = matrix[nr - 1][col]
                entcol = col
        for row in range(nr - 1):
            departinglist.append(matrix[row][entcol])
        if all(x <= 0 for x in departinglist):
            return tab, False
        for row in range(nr - 1):
            if matrix[row][entcol] > 0:
                if (matrix[row][nc - 1] / matrix[row][entcol]) < smallestans:
                    smallestans = (matrix[row][nc - 1] / matrix[row][entcol])
                    deprow = row
                    pivot = matrix[deprow][entcol]
        invars[deprow] = entcol
        matrix[deprow, :] = matrix[deprow, :] / pivot
        for row in range(deprow - 1, -1, -1):
            val = matrix[row][entcol]
            matrix[row, :] = (matrix[row, :] - (val * matrix[deprow, :]))
        for row in range(deprow + 1, nr):
            val = matrix[row][entcol]
            matrix[row, :] = (matrix[row, :] - (val * matrix[deprow, :]))


def get_solution_from_tab(tab):
    in_vars, mat = tab[0], tab[1]
    nr, nc = mat.shape
    sol = {}
    for k, v in in_vars.items():
        sol[v] = mat[k, nc-1]
    sol['p'] = mat[nr-1, nc-1]
    return sol


def display_solution_from_tab(tab):
    sol = get_solution_from_tab(tab)
    for var, val in sol.items():
        if var == 'p':
            print('p\t=\t{}'.format(val))
        else:
            print('x{}\t=\t{}'.format(var, val))


# =============== Problem 2 ====================

def problem_2_1():
    # replace tab with your definitions
    # for Problem 2.1
    in_vars = {0: 2, 1: 3}
    mat = np.array([[3, 8, 1, 0, 24],
                    [6, 4, 0, 1, 30],
                    [-2, -3, 0, 0, 0]],
                   dtype=float)
    tab = (in_vars, mat)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


def problem_2_2():
    # replace tab with your definitions
    # for Problem 2.2.
    in_vars = {0: 2, 1: 3}
    mat = np.array([[1, -1, 1, 0, 4],
                    [-1, 3, 0, 1, 4],
                    [-1, 0, 0, 0, 0]],
                   dtype=float)
    tab = (in_vars, mat)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


def problem_2_3():
    # replace tab with your definitions
    # for Problem 2.3.
    in_vars = {0: 3, 1: 4, 2: 5}
    mat = np.array([[12, 6, 0, 1, 0, 0, 1500],
                    [18, 12, 10, 0, 1, 0, 2500],
                    [15, 8, 0, 0, 0, 1, 2000],
                    [-1.5, -0.8, -0.25, 0, 0, 0, 0]],
                   dtype=float)
    tab = (in_vars, mat)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


def problem_2_4():
    # replace tab with your definitions
    # for Problem 2.4.
    in_vars = {0: 3, 1: 4}
    mat = np.array([[1, 1, 1, 1, 0, 0, 1000],
                    [6, 4, 4, 0, 1, 0, 7200],
                    [-120, -96, -100, 0, 0, 0, 0]],
                   dtype=float)
    tab = (in_vars, mat)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


problem_2_1()
problem_2_2()
problem_2_3()
problem_2_4()
