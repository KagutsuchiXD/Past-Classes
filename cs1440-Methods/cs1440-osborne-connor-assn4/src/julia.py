#!/usr/bin/python3

# Julia Set Visualizer
from Fractal import Fractal


class Julia(Fractal):
    def __init__(self):
        pass

    def count(self, info, z):

        c = complex(float(info['creal']), float(info['cimag']))  # c0

        for i in range(info['iterations']):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded

        return int(info['iterations']) - 1  # Indicate a bounded sequence
