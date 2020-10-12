##############################################
# module: midterm03_s20.py
# Connor Osborne
# A01880782
##############################################

import numpy as np
import cv2
import sys
import os
import re
import pickle
import cs3430_hw9_hinx
from cs3430_hw9_hret import show_images
import cs3430_s20_hw02
import HuffmanTree
from hw12_BinHuffmanTree import BinHuffmanTree

# PUT ALL YOUR IMPORTS HERE AND REMEMBER TO INCLUDE
# ALL THE IMPORTED MODULES IN YOUR SUBMISSION.

# ======================== Problem 1 ======================================


def generate_file_names(fnpat, rootdir):
  '''
  generate all the files in directory rootdir that match regular expression fnpat.
  '''
  for path, dirlist, filelist in os.walk(rootdir):
    for file_name in filelist:
      if not file_name.startswith('.') and not re.match(fnpat, file_name) is None:
        yield os.path.join(path, file_name)
    for d in dirlist:
      generate_file_names(fnpat, d)


def hinx_img_dir(imgdir, hist_index, color_space, num_bins, pick_file):
    print('Indexing {}...'.format(imgdir))
    for imgp in generate_file_names(r'.+\.(jpg|png|JPG)', imgdir):
        print('indexing ' + imgp)
        hinx_img(imgp, hist_index, color_space, num_bins=num_bins)
        print(imgp + ' indexed')
    with open(pick_file, 'wb') as histpick:
        pickle.dump(hist_index, histpick)
    print('indexing finished')


def hinx_img(imgp, hist_index, color_space, num_bins=8):
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
    hist_index[imgp] = fin_hist


# ==================== Problem 2 ==================================

def find_sim_rgb_images(imgpath, num_bins, hist_index, hist_sim):
    assert num_bins == 8 or num_bins == 16
    img = cv2.imread(imgpath)
    hist = cv2.calcHist([img], [0, 1, 2], None, [num_bins, num_bins, num_bins], [0, 256, 0, 256, 0, 256])
    hist1 = cv2.normalize(hist, hist).flatten()
    if hist_sim is 'inter':
        matchlist = [('init1', -1), ('init2', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_INTERSECT)
            if value > matchlist[0][1] and value > matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1]:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'correl':
        matchlist = [('init1', -1), ('init2', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CORREL)
            if value > matchlist[0][1] and value > matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1]:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'chisqr':
        matchlist = [('init1', 1000), ('init2', 1000)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CHISQR)
            if value < matchlist[0][1] and value < matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1]:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'bhatta':
        matchlist = [('init1', 1), ('init2', 1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_BHATTACHARYYA)
            if key.find('17_02_21_22_16_43_orig') != -1:
                print("expected value at images/17_02_21_22_16_43_orig.png: ")
                print(value)
                print(matchlist)
            if value < matchlist[0][1] and value < matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1] and value:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist


def find_sim_hsv_images(imgpath, num_bins, hist_index, hist_sim):
    assert num_bins == 8 or num_bins == 16
    img = cv2.imread(imgpath)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv_img], [0, 1, 2], None, [num_bins, num_bins, num_bins], [0, 180, 0, 256, 0, 256])
    hist1 = cv2.normalize(hist, hist).flatten()
    if hist_sim is 'inter':
        matchlist = [('init1', -1), ('init2', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_INTERSECT)
            if value > matchlist[0][1] and value > matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1]:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'correl':
        matchlist = [('init1', -1), ('init2', -1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CORREL)
            if value > matchlist[0][1] and value > matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value > matchlist[1][1]:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'chisqr':
        matchlist = [('init1', 1000), ('init2', 1000)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_CHISQR)
            if value < matchlist[0][1] and value < matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1]:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist
    elif hist_sim == 'bhatta':
        matchlist = [('init1', 1), ('init2', 1)]
        for key in hist_index:
            value = cv2.compareHist(hist1, hist_index[key], cv2.HISTCMP_BHATTACHARYYA)
            if key.find('17_02_21_22_16_43_orig') != -1:
                print("expected value at images/17_02_21_22_16_43_orig.png: ")
                print(value)
                print(matchlist)
            if value < matchlist[0][1] and value < matchlist[1][1]:
                matchlist[0] = (key, value)
            elif value < matchlist[1][1] and value:
                matchlist[1] = (key, value)
        show_images(img, matchlist)
        return matchlist


def load_hinx(pick_path):
    with open(pick_path, 'rb') as histfile:
        return pickle.load(histfile)

# ======================== Problem 3 ====================================


def bsubst(a, n, b, m):
    x = np.zeros((n, m), )
    upper = np.copy(a)
    for vec in range(m):  # loop through each column vector in x and b
        x[n - 1][vec] = b[n - 1][vec] / upper[n - 1][n - 1]  # base case(initial variable for x)
        for i in range(n - 2, -1, -1):
            bb = 0
            for j in range(i + 1, n):  # add up each preceding ax pairing
                bb += upper[i][j] * x[j][vec]
            x[i][vec] = (b[i][vec] - bb) / upper[i][i]  # solve for current x value
    return x


def fsubst(a, n, b, m):
    x = np.zeros((n, m))
    lower = np.copy(a)
    for vec in range(m):  # loop through each column vector in x and b
        x[0][vec] = b[0][vec] / lower[0][0]  # base case(initial variable for x)
        for i in range(1, n):
            bb = 0
            for j in range(i):  # add up each preceding ax pairing
                bb += lower[i][j] * x[j][vec]
            x[i][vec] = (b[i][vec] - bb) / lower[i][i]  # solve for current x value
    return x

# ======================== Problem 4 ====================================


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


def do_simplex(tab):
    invars, matrix = tab[0], tab[1]
    nr, nc = matrix.shape

    is_solved = False
    while not is_solved:
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


# ======================== Problem 5 ====================================

def dir_corr(fixed, dancer):
    fnr, fnc = fixed.shape
    dnr, dnc = dancer.shape
    C = np.zeros(((fnr + dnr - 1), (fnc + dnc - 1)))

    for r in range((fnr + dnr - 1)):
        for c in range((fnc + dnc - 1)):
            value = 0
            for x in range(fnr):
                for y in range(fnc):
                    fval = fixed[x, y]
                    if x - (r - dnr + 1) < 0 or x - (r - dnr + 1) >= dnr or y - (c - dnc + 1) < 0 or y - (
                            c - dnc + 1) >= dnc:
                        dval = 0
                    else:
                        dval = dancer[x - (r - dnr + 1)][y - (c - dnc + 1)]
                    value += fval * dval
            C[r, c] = value

    return C

# ======================== Problem 6 ====================================

# Write your answers to problem 6 as the values of the appropriate variables
# below and state how you computed them. You may not use scientific
# calculators/MATLAB/Octave/etc. You have to use your implementation
# of the NRA from a previous assignment or write it from scratch.


'''
1. Using nra zr1 from homework 6 I got the answer 18.24828759089466

2. Using nra zr1 from homework 6 I got the answer 3.316624805231569

3.Using nra zr1 from homework 6 I got the answer 1.5848931924611136

4.Using nra zr1 from homework 6 I got the answer 2.2239800905693157
'''

midterm03_s20_problem_6_1 = 18.24828759089466
midterm03_s20_problem_6_2 = 3.316624805231569
midterm03_s20_problem_6_3 = 1.5848931924611136
midterm03_s20_problem_6_4 = 2.2239800905693157

# ======================== Problem 7 ====================================

# Write your answers to problem 7 as the value of the appropriate variables
# below and state how you computed them. You may not use scientific
# calculators/MATLAB/Octave/etc. You have to use your implementation
# of CDD from a previous assignment or write it from scratch.

'''
1. Using cdd drv1_ord2 from homework 7 I got the answer 6.967738652119414

2. Using cdd drv1_ord4 from homework 7 I got the answer 20.858529816451345

3. Using cdd drv1_ord2 from homework 7 I got the answer 70.04076271828197

4. Using cdd drv1_ord4 from homework 7 I got the answer 273.075439514514
'''

midterm03_s20_problem_7_1 = 6.967738652119414
midterm03_s20_problem_7_2 = 20.858529816451345
midterm03_s20_problem_7_3 = 70.04076271828197
midterm03_s20_problem_7_4 = 273.075439514514


# ======================== Problem 8 =====================================

def build_huffman_tree_from_text(txtstr):
    freq_list = {}
    for char in txtstr:
        if char in freq_list:
            freq_list[char] += 1
        else:
            freq_list[char] = 1
    node_list = HuffmanTree.HuffmanTree.freqMapToListOfHuffmanTreeNodes(freq_list)
    ht = HuffmanTree.HuffmanTree.fromListOfHuffmanTreeNodes(node_list)
    # ht.displayHuffmanTree(ht)
    return ht


'''
Remember to state the number of saved bytes.
moby_dick_ch03.txt = 32,605 bytes
moby_dick_ch03.bin = 19,747 bytes
moby_dick_ch03_pb.txt = 10 bytes

Number of saved bytes = 32,605 - (19,747 + 10) = 12,848 bytes
'''

def encode_moby_dick_ch03():
    char_freq_map = {}
    with open('moby_dick_ch03.txt', encoding='utf-8') as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c in char_freq_map:
                char_freq_map[c] += 1
            else:
                char_freq_map[c] = 1
    nodes = HuffmanTree.HuffmanTree.freqMapToListOfHuffmanTreeNodes(char_freq_map)
    ht = HuffmanTree.HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
    bht = BinHuffmanTree(root=ht.getRoot())
    bht.encodeTextFromFileToFile('moby_dick_ch03.txt',
                                 'moby_dick_ch03')


# ======================== Problem 9 ====================================

# Place your bin_id3.py into the current folder and uncomment
# the next line
from hw11_bin_id3 import bin_id3


def display_bin_id3_node(node):
    bin_id3.display_id3_node(node, '')


def learn_bin_id3_dt_from_csv_file(csv_fp, target_attrib):
    examples, attributes = bin_id3.parse_csv_file_into_examples(csv_fp)
    avt = bin_id3.construct_attrib_values_from_examples(examples, attributes)
    tree = bin_id3.fit(examples, target_attrib, attributes, avt, True)
    return tree


def classify_csv_file_with_bin_id3_dt(dt_root, csv_fp, target_attrib):
    acc = 0.0
    test_examples, colnames = bin_id3.parse_csv_file_into_examples(csv_fp)
    for i in range(10):
        run_acc = sum([bin_id3.predict(dt_root, tex) == tex[target_attrib] for tex in test_examples])/len(test_examples)
        acc += run_acc
    return acc/3


### ======================== Problem 10 ====================================

'''
Write 2-3 short paragraphs to answer the questions in Problem 10 here.

The missing attribute value problem in the context of the ID3 Algorithm is that when w are training
the trees we inject randomness in the data splits. This randomness may cause an issue by causing specific
attributes to have missing values which will lead to errors.

In homework 11 I addressed this issue by automatically assigning the value of MINUS if the attribute's 
value happened to be missing in a test example.
'''

    








               





