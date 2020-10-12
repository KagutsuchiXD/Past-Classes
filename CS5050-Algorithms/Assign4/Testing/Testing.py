import time
import numpy as np
from random import randint


table = {'a': {'a': 5, 'c': -1, 'g': -2, 't': -1, 'i': -3, 'n': 0},
         'c': {'a': -1, 'c': 5, 'g': -3, 't': -2, 'i': -4, 'n': 0},
         'g': {'a': -2, 'c': -3, 'g': 5, 't': -2, 'i': -2, 'n': 0},
         't': {'a': -1, 'c': -2, 'g': -2, 't': 5, 'i': -1, 'n': 0},
         'n': {'a': 0, 'c': 0, 'g': 0, 't': 0, 'i': 0, 'n': 0}}

trace = []

checking1 = 'aggactaccttcgaacaccaatttgggagaatccaggtacgccgtgtatcaacgaaaaccaacgggtgaggaacagacactttatggccctgatagctgtgcacatggtgacctactttaataccactatgtgcattcggtgatgatattaattcgagctaagtctgtaagctccctaggcgccgttggtatacgcagcaaaatggcacgctggttgtgagctaacttgcatactccttgccgcatgaatcgtacccccccaattcgtgagagttaataactcatagatcagatagtcagggccgcttctacagatgaagaaccgttgtggcccgtttctctgcaacttacagggattctgatacgcccgatggttgttctaggactaccttcgaacaccaatttgggagaatccaggtacgccgtgtatcaacgaaaaccaacgggtgaggaacagacactttatggccctgatagctgtgcacatggtgacctactttaataccactatgtgcattcggtgatgatattaattcgagctaagtctgtaagctccctaggcgccgttggtatacgcagcaaaatggcacgctggttgtgagctaacttgcatactccttgccgcatgaatcgtacccccccaattcgtgagagttaataactcatagatcagatagtcagggccgcttctacagatgaagaaccgttgtggcccgtttctctgcaacttacagggattctgatacgcccgatggttgttctc'
checking2 = 'aggactaccttcgaacaccaatttgggagaatccaggtacgccgtgtatcaacgaaaaccaacgggtgaggaacagacactttatggccctgatagctgtgcacatggtgacctactttaataccactatgtgcattcggtgatgatattaattcgagctaagtctgtaagctccctaggcgccgttggtatacgcagcaaaatggcacgctggttgtgagctaacttgcatactccttgccgcatgaatcgtacccccccaattcgtgagagttaataactcatagatcagatagtcagggccgcttctacagatgaagaaccgttgtggcccgtttctctgcaacttacagggattctgatacgcccgatggttgttctcaggactaccttcgaacaccaatttgggagaatccaggtacgccgtgtatcaacgaaaaccaacgggtgaggaacagacactttatggccctgatagctgtgcacatggtgacctactttaataccactatgtgcattcggtgatgatattaattcgagctaagtctgtaagctccctaggcgccgttggtatacgcagcaaaatggcacgctggttgtgagctaacttgcatactccttgccgcatgaatcgtacccccccaattcgtgagagttaataactcatagatcagatagtcagggccgcttctacagatgaagaaccgttgtggcccgtttctctgcaacttacagggattctgatacgcccgatggttgttct'

num_function_calls = 0

def dpDNA(A, B, i, j, file):
    file.write("***************************\n")
    file.write("1: " + A + "\n")
    file.write("2: " + B + "\n")
    cache = np.zeros((i+1, j+1), dtype=int)

    cache[0][0] = 0
    for a in range(1, i + 1):
        cache[a][0] = cache[a-1][0] + table[A[a - 1]]['i']
    for b in range(1, j + 1):
        cache[0][b] = cache[0][b-1] + table[B[b - 1]]['i']

    for a in range(1, i + 1):
        for b in range(1, j + 1):
            cache[a][b] = max(cache[a - 1][b] + table[A[a-1]]['i'],  # del
                              cache[a][b - 1] + table[B[b-1]]['i'],  # ins
                              cache[a - 1][b - 1] + table[A[a-1]][B[b-1]])
    file.write("Score: " + str(cache[i][j]) + "\n")
    global trace
    traceback(A, B, cache, i, j)
    trace.reverse()
    for thing in trace:
        file.write(thing + "\n")
    trace = []
    return cache[i][j]


def traceback(A, B, cache, i, j):
    if i == 0:
        return
    if j == 0:
        return
    if cache[i][j] == cache[i - 1][j] + table[A[i-1]]['i']:
        trace.append(A[i-1] + " -> _")
        traceback(A, B, cache, i-1, j)
    if cache[i][j] == cache[i][j - 1] + table[B[j-1]]['i']:
        trace.append("_ -> " + B[j-1])
        traceback(A, B, cache, i, j-1)
    if cache[i][j] == cache[i - 1][j - 1] + table[A[i-1]][B[j-1]]:
        if A[i-1] == B[j-1]:
            trace.append(A[i - 1] + " = " + B[j - 1])
            traceback(A, B, cache, i - 1, j - 1)
        else:
            trace.append(A[i - 1] + " -> " + B[j - 1])
            traceback(A, B, cache, i - 1, j - 1)


def add_rand():
    global checking1
    global checking2
    l = randint(1, 4)
    if l == 1:
        checking1 = checking1 + 'a'
        checking2 = checking2 + 'g'
    if l == 2:
        checking1 = checking1 + 'c'
        checking2 = checking2 + 't'
    if l == 3:
        checking1 = checking1 + 'g'
        checking2 = checking2 + 'c'
    if l == 4:
        checking1 = checking1 + 't'
        checking2 = checking2 + 'a'


for let in range(100):
    add_rand()

results = open('test.txt', 'w')
words = open('words.txt', 'w')

for x in range(877, 10000):
    words.write("WordA " + str(x) + ": " + checking1 + "\n")
    words.write("WordB " + str(x) + ": " + checking1 + "\n")
    start = time.time()
    dpDNA(checking1, checking2, len(checking1), len(checking2), results)
    end = time.time()
    t = end - start
    print(str(x) + " took " + str(t) + " seconds")
    add_rand()
