# calculates best number of stones to take while playing nim
import time


def nim(stones):
    start = time.time()  # start timer
    if stones == 0:  # base condition
        print('I win!')
        end = time.time()  # stop timer
        print(end - start)  # print time taken
        return 0
    if stones == 1:  # base condition
        print('I lose.')
        end = time.time()
        print(end - start)
        return 1
    if not win(stones - 1):  # see how many stones should be taken so opponent wont win
        end = time.time()
        print(end - start)
        return 1
    end = time.time()
    print(end - start)
    return 2


def win(n):
    if n == 0:  # current player being checked wins
        return True
    if n == 1:  # current player being checked loses
        return False
    return not (win(n-1)) and (win(n-2))  #if true player can take two. If false only takes one.


numstones = input('How many stones are there?')
print(nim(int(numstones)))
