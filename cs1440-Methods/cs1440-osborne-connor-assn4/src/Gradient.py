import random
import abc
from Color import Color


class Gradient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gradient(self):
        pass


class DefaultGradient(Gradient):
    def __init__(self):
        pass

    def gradient(self, size):
        grad = []
        for i in range(size):
            color = Color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            grad.append(color)
        return grad


class InputGradient(Gradient):
    def __init__(self):
        pass

    def gradient(self, start, stop, steps):
        dRed = (stop.r - start.r) / (steps - 1)
        dGrn = (stop.g - start.g) / (steps - 1)
        dBlu = (stop.b - start.b) / (steps - 1)
        return list(
            map(lambda n: Color((n * dRed) + start.r, (n * dGrn) + start.g, (n * dBlu) + start.b), range(steps)))
