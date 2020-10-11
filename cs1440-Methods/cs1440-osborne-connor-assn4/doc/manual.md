How to use this program:

1. Create a configuration file in the following format:
   type: <fractal type(Julia or Mandelbrot)>
   cReal: <real number for computing a complex number (only needed for type: Julia)>
   cImag: <imaginary number for computing a complex number (only needed for type: Julia)>
   pixels: <size of the picture (must be an integer)>
   centerX: <centerX value>
   centerY: <centery value>
   axisLength: <length of fractal's axis>
   iterations: <size of gradient and number of times colors are added(must be an integer)>

2. Inorder to use this program first open your terminal.
3. Then change you current directory to the directory in which you have this program's src folder saves.
4. Then input in your terminal "python src\main.py data\<configuration filename>"
5. The program will tell you if your configuration file is correct. If it is not it will tell you why. Then edit your file
or check your spelling and try again. If your file is correct this program will create the specified fractal,
display it, and save the picture to the data folder.

