
import Gradient
from Color import Color


class GradientFactory:
    def __init__(self):
        pass

    def makeGradient(self, info, size):
        if info == '':
            gradient = Gradient.DefaultGradient()
            print(f"Gradient Factory: creating default color gradient")
            return gradient.gradient(size)
        elif info == 'Grayscale':
            start = Color(0, 0, 0)
            stop = Color(255, 255, 255)
            gradient = Gradient.InputGradient()
            print(f"Gradient Factory: creating {info} color gradient")
            return gradient.gradient(start, stop, size)
        elif info == 'Fire':
            start = Color(255, 255, 0)
            stop = Color(255, 0, 0)
            gradient = Gradient.InputGradient()
            print(f"Gradient Factory: creating {info} color gradient")
            return gradient.gradient(start, stop, size)
        elif info == 'Tron':
            start = Color(0, 255, 255)
            stop = Color(0, 0, 0)
            gradient = Gradient.InputGradient()
            print(f"Gradient Factory: creating {info} color gradient")
            return gradient.gradient(start, stop, size)
        elif info == 'Water':
            start = Color(0, 255, 255)
            stop = Color(0, 0, 255)
            gradient = Gradient.InputGradient()
            print(f"Gradient Factory: creating {info} color gradient")
            return gradient.gradient(start, stop, size)
        elif info == 'Earth':
            start = Color(0, 100, 0)
            stop = Color(217, 166, 33)
            gradient = Gradient.InputGradient()
            print(f"Gradient Factory: creating {info} color gradient")
            return gradient.gradient(start, stop, size)
        elif info == 'Air':
            start = Color(205, 205, 205)
            stop = Color(0, 255, 255)
            gradient = Gradient.InputGradient()
            print(f"Gradient Factory: creating {info} color gradient")
            return gradient.gradient(start, stop, size)
        else:
            gradient = Gradient.DefaultGradient()
            print(f"Gradient Factory: Unknown gradient '{info}'; creating default color gradient")
            return gradient.gradient(size)

