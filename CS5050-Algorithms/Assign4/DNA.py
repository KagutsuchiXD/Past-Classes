import numpy as np

table = {'a': {'a': 5, 'c': -1, 'g': -2, 't': -1, 'i': -3, 'n': 0},
         'c': {'a': -1, 'c': 5, 'g': -3, 't': -2, 'i': -4, 'n': 0},
         'g': {'a': -2, 'c': -3, 'g': 5, 't': -2, 'i': -2, 'n': 0},
         't': {'a': -1, 'c': -2, 'g': -2, 't': 5, 'i': -1, 'n': 0},
         'n': {'a': 0, 'c': 0, 'g': 0, 't': 0, 'i': 0, 'n': 0}}

trace = []

humtonean = 0
humtoape = 0
neantoape = 0


def dna(i, j, file):
    file.write("**********************************\n")
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
    traceback(cache, i, j)
    trace.reverse()
    for thing in trace:
        file.write(thing + "\n")
    trace = []
    return cache[i][j]


def traceback(cache, i, j):
    if i == 0:
        return
    if j == 0:
        return
    if cache[i][j] == cache[i - 1][j] + table[A[i-1]]['i']:
        trace.append(A[i-1] + " -> _")
        traceback(cache, i-1, j)
    if cache[i][j] == cache[i][j - 1] + table[B[j-1]]['i']:
        trace.append("_ -> " + B[j-1])
        traceback(cache, i, j-1)
    if cache[i][j] == cache[i - 1][j - 1] + table[A[i-1]][B[j-1]]:
        if A[i-1] == B[j-1]:
            trace.append(A[i - 1] + " = " + B[j - 1])
            traceback(cache, i - 1, j - 1)
        else:
            trace.append(A[i - 1] + " -> " + B[j - 1])
            traceback(cache, i - 1, j - 1)


human = open('human.txt', 'r')
ape = open('Gorilla.txt', 'r')
nean = open('neanderthal.txt', 'r')

list1 = []
list2 = []
list3 = []

for line in human:
    line = line.rstrip()
    if line == "ORIGIN":
        continue
    curline = line.split(" ")
    curline.pop(0)
    list1 += curline

for line in nean:
    line = line.rstrip()
    if line == "ORIGIN":
        continue
    curline = line.split(" ")
    curline.pop(0)
    list2 += curline

for line in ape:
    line = line.rstrip()
    if line == "ORIGIN":
        continue
    curline = line.split(" ")
    curline.pop(0)
    list3 += curline
# Human to Neanderthal comparison
h2n = open('HumantoNeadertal.txt', 'w')
for word in range(len(list1)):
    A = list1[word]
    B = list2[word]
    value = dna(len(A), len(B), h2n)
    humtonean += value

print(humtonean)


# Human to Ape comparison
h2a = open('HumantoApe.txt', 'w')
if len(list3) < len(list1):
    for x in range(len(list3), len(list1)):
        list3.append("")
for word in range(len(list1)):
    A = list1[word]
    B = list3[word]
    value = dna(len(A), len(B), h2a)
    humtoape += value

print(humtoape)


# Neanderthal to Ape comparison
n2a = open('NeaderthaltoApe.txt', 'w')
for word in range(len(list1)):
    A = list2[word]
    B = list3[word]
    value = dna(len(A), len(B), n2a)
    neantoape += value

print(neantoape)
