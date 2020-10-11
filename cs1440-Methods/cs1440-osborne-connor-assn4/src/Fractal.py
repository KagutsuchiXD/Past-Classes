import abc


class Fractal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def count(self):
        pass
