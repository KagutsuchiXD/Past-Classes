import sys
import Config
import ImagePainter


config = sys.argv[1]
info = Config.createDictionary(config)
imageName = config
try:
    float(info['centerx'])
    float(info['centery'])
except ValueError:
    print('centerX and centerY must be numbers please check configuration file and try again.')
try:
    int(info['pixels'])
    int(info['iterations'])
except ValueError:
    print('Both pixels and iterations must be integers, please check configuration file and try again')

if info['type'] != 'Julia' and info['type'] != 'Mandelbrot':  # check for missing/wrong information in config file
    print('Type for fractal must be Julia or Mandelbrot please check configuration file and try again.')
    if info['type'] == 'Julia':
        if 'creal' not in info or 'cimag' not in info:
            print('Configuration files for Julia fractals need cReal and cImag to both be present'
                  ' please check file and try again')
elif 'pixels' not in info or 'centerx' not in info or 'centery' not in info or 'axislength' not in info\
        or 'iterations' not in info:
    print('pixels, centerX, centerY, axislength, and iterations must be present'
          ' in the file, please check configuration file and try again.')
else:
    ImagePainter.paint(info, imageName)  # create image
