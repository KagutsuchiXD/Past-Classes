import time


def nim(pieces, wins, done):
    start = time.time()  # start timer
    if pieces == 0:
        print('I win!')
        end = time.time()  # end timer
        print(end - start)  # print time taken
        return 0
    if pieces == 1:
        print('I lose.')
        end = time.time()
        print(end - start)
        return 1
    if not win(pieces - 1, wins, done):
        end = time.time()
        print(end - start)
        return 1
    end = time.time()
    print(end - start)
    return 2


def win(n, wins, done):
    if n == 0:
        return True
    if n == 1:
        return False
    if done[n] is True:  # check if this number of stones has been calculated yet.
        return wins[n]
    wins[n] = not (win(n-1, wins, done)) and (win(n-2, wins, done))
    # if True the opponent wont win if you take either number
    done[n] = True
    return wins[n]


numstones = input('How many stones are there?')
stones = int(numstones)
done = [False] * stones  # array for checking if the given value has been calculated
wins = [None] * stones  # array for storing result for given number of stones
print(nim(stones, wins, done))
