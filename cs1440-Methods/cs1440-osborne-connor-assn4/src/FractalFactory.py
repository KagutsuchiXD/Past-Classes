import abc
from mandelbrot import Mandelbrot
from julia import Julia
from Snowflake import Snowflake


class FractalFactory:
    def __init__(self):
        pass

    def makeFractal(self, config, complexNum):

        if config['type'] == 'Mandelbrot':
            fractal = Mandelbrot()
            return fractal.count(config, complexNum)

        elif config['type'] == 'Julia':
            fractal = Julia()
            return fractal.count(config, complexNum)
        elif config['type'] == 'Snowflake':
            fractal = Snowflake()
            return fractal.count(config, complexNum)
        else:
            raise NotImplementedError("Invalid fractal requested")
