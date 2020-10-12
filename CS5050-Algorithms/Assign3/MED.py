import re


def recMED(A, i, B, j):
    if i == 0 and j == 0:
        return 0
    if i == 0 and j > 0:
        return j
    if j == 0 and i > 0:
        return i
    return min((recMED(A, i-1, B, j) + 1),
               (recMED(A, i, B, j-1) + 1),
               (recMED(A, i - 1, B, j - 1) + (A[i] != B[i])))


def dpMED(A, i, B, j):
    cache = [[-1 for k in range(j + 1)] for l in range(i + 1)]
    for a in range(i + 1):
        cache[a][0] = i
        for b in range(j + 1):
            cache[0][b] = b
    cache[0][0] = 0
    for a in range(1, i + 1):
        for b in range(1, j + 1):
            cache[a][b] = min(1 + cache[a - 1][b],
                              1 + cache[a][b - 1],
                              (A[a] != B[b]) + cache[a - 1][b - 1])
    return cache[i][j]


meds = {}
maxpairing = []
maxeditdistance = 0

with open("spellcheck.txt") as spellcheck:
    for line in spellcheck:
        curline = line.strip()
        checking = re.split("->|, ", curline)
        for word in range(1, len(checking)):
            curmed = dpMED("_"+checking[0], len(checking[0]), "_"+checking[word], len(checking[word]))
            if curmed > maxeditdistance:
                maxeditdistance = curmed
                maxpairing = []
                maxpairing.append(checking[0] + "->" + checking[word])
            if curmed in meds:
                meds[curmed] += 1
            else:
                meds[curmed] = 1
answers = []
for key in meds:
    answers.append(key)
answers.sort()

results = open('results.txt', 'w')
results.write("Results for Minimum Edit Distance\n")
for key in range(len(answers)):
    results.write(str(answers[key]) + ", " + str(meds[answers[key]]) + "\n")

results.write("\nMaximum edit distance: " + str(maxeditdistance) + "\n")
for word in maxpairing:
    results.write(word + "\n")
