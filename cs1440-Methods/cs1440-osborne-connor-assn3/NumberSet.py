import random


class NumberSet():

    def __init__(self, size):
        """NumberSet constructor"""
        self.size = size;
        self._numSet = []
        for i in range(1, size + 1):
            num = i
            self._numSet.append(num)
        self.numIndex = 0

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return len(self._numSet)

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        return self._numSet[index]


    def randomize(self):
        """void function: Shuffle this NumberSet"""
        pass


    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""

        if self.numIndex == self.getsize():
            return None
        else:
            next = self.numIndex
            self.numIndex += 1
            return self._numSet[next]
