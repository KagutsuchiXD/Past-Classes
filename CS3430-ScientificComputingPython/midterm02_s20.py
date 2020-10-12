#####################################################
# module: midterm02_s20.py
# YOUR NAME
# YOUR A-NUMBER
#
# Don't copy and paste the problem statements
# from the exam's pdf.
######################################################


### ========= Probem 1 (2 points) ================

'''

1. Using nra zr1 from homework 6 I got the answer 3.606503216739488

2. Using nra zr1 from homework 6 I got the answer 3.872983346207417

3.Using nra zr1 from homework 6 I got the answer 13.076696909834958

4.Using nra zr1 from homework 6 I got the answer 12.830137319983306

5.Using nra zr1 from homework 6 I got the answer 1.718771927587479

6.Using nra zr1 from homework 6 I got the answer 3.1551905220000354

7.Using nra zr1 from homework 6 I got the answer 2.2539512722136625

State which functions, methods, and classes and from which assignments
you used to compute the values.

'''

### ========= Probem 2 (2 points) ================


'''

1. -0.12884447282140998 using cdd.drv1_ord2(f, 1.7, 0.001) from homework 7

2. -0.12884449429547326 using cdd.drv1_ord4(f, 1.7, 0.001) from homework 7

3. 4638956.468971446 using cdd.drv1_ord2(f3, 15.35, 0.00001) from homework 7

4. 4638956.468909358 using cdd.drv1_ord4(f3, 15.35, 0.00001) from homework 7

5. 9040.212076024545 using cdd.drv1_ord2(f5, 1.5, 0.00001) from homework 7

6. 9040.212072259616 using cdd.drv1_ord4(f5, 1.5, 0.00001) from homework 7

State which functions, methods, and classes and from which assignments
you used to compute the values.
'''

### ========= Probem 3 (1 point) ================

'''

f'(0.5) = -10.74999985000158

I got this answer using cdd.drv1_ord2(f, 0.5, 0.0001) from homework 7

State which functions, methods, and classes and from which assignments
you used to compute the values.

'''

### ========= Probem 4 (1 point) ================


'''

                     R_(4,4) Error = O(h^8)
                    /       \
           R_(3,3)            R_(4,3) Error = O(h^6)
         /        \           /        \
   R_(2,2)           R_(3,2)             R_(4,2)        Error = O(h^4)
    /     \         /     \            /         \
T_(1,1)    T_(2,1)            T_(3,1)           T_(4,1)  Error = O(h^2)
'''

### ========= Probem 5 (1 point) ================

'''

Gradient's magnitude = ?

Gradient's orientatition = ?

State which functions, methods, and classes and from which assignments
you used to compute the values.

'''

### ========= Probem 6 (1 point) ================

def to_pil_xy_ut0():
    w, h = 5, 5
    for x in range(5):
        for y in range(5):
            cx, cy = center_xy(x, y, w, h)
            print('x={},y={}: cx={},cy={}'.format(x, y, cx, cy))

def center_xy(x, y, w, h):
    x = x - int(w/2)
    y = y - int(h/2)
    return x, y

### ========= Probem 7 (1 point) ================

'''

1. C1 = ?
[[0,0,0,0,0],
 [0,0,0,0,0],
 [100,0,0,0,0],
 [0,0,0,0,0],
 [0,50,0,0,0]]

2. C2 = ?
[[0,0,0,50,0],
 [0,0,0,0,0],
 [0,0,0,0,100],
 [0,0,0,0,0],
 [0,0,0,0,0]]

'''

### ========= Probem 8 (1 point) ================

'''

bin 1: [0, 2) = ?

bin 2: [2, 4) = ?

bin 3: [4, 6) = ?

'''

