import sys

from FractalFactory import FractalFactory
from GradientFactory import GradientFactory
from tkinter import Tk, Canvas, PhotoImage, mainloop


def paint(config, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This function displays a really handy status bar so you can see how far
    along in the process the program is."""
    gfactory = GradientFactory()
    ffactory = FractalFactory()
    if len(sys.argv) >= 3:
        gradient = gfactory.makeGradient(sys.argv[2], int(config['iterations']))
    else:
        gradient = gfactory.makeGradient('', int(config['iterations']))
    numPixels = int(config['pixels'])

    window = Tk()
    canvas = Canvas(window, width=numPixels, height=numPixels, bg=gradient[0])
    img = PhotoImage(master=canvas, width=numPixels, height=numPixels)

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = float(config['centerx']) - (float(config['axislength']) / 2.0)
    maxx = float(config['centerx']) + (float(config['axislength']) / 2.0)
    miny = float(config['centery']) - (float(config['axislength']) / 2.0)
    maxy = float(config['centery']) + (float(config['axislength']) / 2.0)

    pixelsize = abs(maxx - minx) / numPixels

    portion = int(numPixels / (numPixels / 10))

    for col in range(numPixels):
        if col % portion == 0:
            # Update the status bar
            pips = col // portion
            pct = col / numPixels
            print(f"{imagename}.png ({numPixels}x{numPixels})"
                  f" {'=' * pips}{'_' * (int((numPixels / 10)) - pips)} {pct:.0%}", end='\r', file=sys.stderr)
        for row in range(numPixels):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            compNum = complex(x, y)
            color = gradient[ffactory.makeFractal(config, compNum)]
            img.put(color, (col, row))

    print(f"{imagename}.png ({numPixels}x{numPixels})"
          f" ================================================================ 100%",
          file=sys.stderr)

    # Display the image on the screen

    canvas.pack()
    canvas.create_image(((numPixels / 2), (numPixels / 2)), image=img, state="normal")

    # Save the image as a PNG
    # TODO: I have heard that you can create pictures in other formats, such as GIF
    #       and PPM.  I wonder how I do that?
    img.write(imagename + ".png")
    print(f"Wrote image {img}.png")
    mainloop()
