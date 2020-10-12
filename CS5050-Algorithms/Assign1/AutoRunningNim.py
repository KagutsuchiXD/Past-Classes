#This program is to run recursive nim program 100 times or until it is force exited.
import time


def nim(stones):
    start = time.time()
    if stones == 0:
        print('I win!')
        end = time.time()
        print(end - start)
        return 0
    if stones == 1:
        print('I lose.')
        end = time.time()
        print(end - start)
        return 1
    if not win(stones - 1):
        end = time.time()
        print(end - start)
        return 1
    end = time.time()
    print(end - start)
    return 2


def win(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return not (win(n-1)) and (win(n-2))


for x in range(0, 101):  # run nim() for given range
    numstones = x
    print('For ' + str(x) + ' stones')
    print(nim(numstones))
