#!/usr/bin/python3

# Mandelbrot Set Visualizer

from Fractal import Fractal


class Mandelbrot(Fractal):
    def __init__(self):
        pass

    def count(self, info, c):
        z = complex(0, 0)  # z0

        for i in range(int(info['iterations'])):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return int(info['iterations']) - 1  # Indicate a bounded sequence
