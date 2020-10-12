
#################################################
# module: cs3430_s20_hw03.py
# Connor Osborne
# YA01880782
##################################################

import numpy as np
import matplotlib.pyplot as plt
from cs3430_s20_hw01 import gje


# =============== Problem 01 ==================

def line_ip(line1, line2):
    a = np.array([[line1[0], line1[1]],
                 [line2[0], line2[1]]], dtype=float)
    b = np.array([line1[2], line2[2]], dtype=float)

    x = np.array([gje(a, b)])
    v = np.transpose(x)
    return v


def check_line_ip(line1, line2, ip, err=0.0001):
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    x = ip[0, 0]
    y = ip[1, 0]
    assert abs((A1*x + B1*y) - C1) <= err
    assert abs((A2*x + B2*y) - C2) <= err


def find_line_ips(lines):
    n = len(lines)
    v = []
    for line in range(n):
        for i in range(line + 1, n):
            v.append(line_ip(lines[line], lines[i]))
    return v


def max_obj_fun(f, cps):
    n = len(cps)
    curval = float("-inf")
    x = ()
    for point in range(n):
        cp = cps[point]
        ans = f(cp[0][0], cp[1][0])
        if ans > curval:
            curval = ans
            x = (cp, ans)

    return x


def min_obj_fun(f, cps):
    lst = [(cp, f(cp[0, 0], cp[1, 0])) for cp in cps]
    return min(lst, key=lambda x: x[1])


# ================= Problem 02 ===============================
# Sample solution to Ted's Toys Problem.
def plot_teds_constraints():
    # plastic constraint: 4x + 3y <= 480
    def plastic_constraint(x): return -(4/3.0)*x + 160.0

    # steel constraints: 3x + 6y <= 720
    def steel_constraint(x): return -0.5*x + 120.0
    xvals = np.linspace(0, 160, 10000)
    yvals1 = np.array([plastic_constraint(x) for x in xvals])
    yvals2 = np.array([steel_constraint(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Ted\'s Toys Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 160])
    plt.xlim([-5, 160])
    # x = 0
    x1, y1 = [0, 0], [0, 160]
    # y = 0
    x2, y2 = [0, 160], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='4x+3y=480', c='red')
    plt.plot(xvals, yvals2, label='3x+6y=720', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()


def teds_problem():
    red_line = (4, 3, 480)
    blue_line = (3, 6, 720)
    green_line = (1, 0, 0)
    yellow_line = (0, 1, 0)

    cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)

    obj_fun = lambda x, y: 5.0*x + 4.0*y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num cars   = {}'.format(x))
    print('num trucks = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p


def plot_2_1_constraints():
    # constraint1: x + y >= 3
    def constraint1(x): return -1.0 * x + 3.0

    # constraint2: 3x - y >= -1
    def constraint2(x): return 3.0 * x + 1.0

    xvals = np.linspace(-5, 10, 10000)
    yvals1 = np.array([constraint1(x) for x in xvals])
    yvals2 = np.array([constraint2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Problem 2.1')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 10])
    plt.xlim([-5, 10])
    # x = 0
    x1, y1 = [2, 2], [0, 10]

    plt.grid()
    plt.plot(xvals, yvals1, label='x + y >= 3', c='red')
    plt.plot(xvals, yvals2, label='3x - y >= -1', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.legend(loc='best')
    plt.show()


def problem_2_1():
    red_line = (1, 1, 3)
    blue_line = (3, -1, -1)
    green_line = (1, 0, 2)

    cp1 = line_ip(green_line, red_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)

    obj_fun = lambda x, y: 3.0 * x + y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num cars   = {}'.format(x))
    print('num trucks = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p


def plot_2_2_constraints():
    # constraint1: x + 2y >= 6
    def constraint1(x): return -0.5 * x + 3.0

    # constraint2: x - y >= -4
    def constraint2(x): return x + 4.0

    # constraint3: 2x + y <= 8
    def constraint3(x): return -2.0 * x + 8.0

    xvals = np.linspace(-5, 10, 10000)
    yvals1 = np.array([constraint1(x) for x in xvals])
    yvals2 = np.array([constraint2(x) for x in xvals])
    yvals3 = np.array([constraint3(x) for x in xvals])
    fig2 = plt.figure(2)
    fig2.suptitle('Problem 2.2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 10])
    plt.xlim([-5, 10])
    # x = 0
    x1, y1 = [0, 0], [0, 10]
    # y = 0
    x2, y2 = [0, 10], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='x + 2y >= 6', c='red')
    plt.plot(xvals, yvals2, label='x - y >= -4', c='blue')
    plt.plot(xvals, yvals3, label='2x + y <= 8', c='purple')

    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()


def problem_2_2():
    red_line = (1, 2, 6)
    blue_line = (1, -1, -4)
    purple_line = (2, 1, 8)
    green_line = (1, 0, 0)
    yellow_line = (0, 1, 0)

    cp3 = line_ip(blue_line, red_line)
    cp7 = line_ip(purple_line, red_line)
    cp8 = line_ip(purple_line, blue_line)

    obj_fun = lambda x, y: x + y

    rslt = max_obj_fun(obj_fun, [cp3, cp7, cp8])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num cars   = {}'.format(x))
    print('num trucks = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p


def plot_2_3_constraints():
    # constraint1: 3x + 6y >= 600
    def constraint1(x): return -0.5 * x + 100.0

    # constraint2: 0.8x + 0.2y >= 90
    def constraint2(x): return -4.0 * x + 450

    xvals = np.linspace(-5, 300, 10000)
    yvals1 = np.array([constraint1(x) for x in xvals])
    yvals2 = np.array([constraint2(x) for x in xvals])

    fig2 = plt.figure(3)
    fig2.suptitle('Problem 2.2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 500])
    plt.xlim([-5, 300])
    # x = 0
    x1, y1 = [0, 500], [0, 0]
    # y = 0
    x2, y2 = [0, 0], [0, 500]
    plt.grid()
    plt.plot(xvals, yvals1, label='3x + 6y >= 600', c='red')
    plt.plot(xvals, yvals2, label='0.8x + 0.2y >= 90', c='blue')

    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()


def problem_2_3():
    red_line = (3.0, 6.0, 600.0)
    blue_line = (0.8, 0.2, 90.0)
    green_line = (1.0, 0, 0)
    yellow_line = (0, 1.0, 0)

    cp9 = line_ip(green_line, red_line)
    cp3 = line_ip(blue_line, red_line)
    cp10 = line_ip(blue_line, yellow_line)

    obj_fun = lambda x, y: 4.0*x + 5.0*y

    rslt = max_obj_fun(obj_fun, [cp3, cp9, cp10])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num Raisins   = {}'.format(x))
    print('num Peanuts = {}'.format(y))
    print('Cost     = {}'.format(p))

    return x, y, p


def plot_2_4_constraints():

    # constraint1: 2x+4y=100,000
    def constraint1(x): return 25000-0.5*x

    # constraint2: 8x+3y=2400
    def constraint2(x): return 800-2.6666*x

    xvals = np.linspace(-10000, 50000, 100000)
    yvals1 = np.array([constraint1(x) for x in xvals])
    yvals2 = np.array([constraint2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Plot 2.1')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5000, 50000])
    plt.xlim([-5000, 50000])
    # x = 0
    x1, y1 = [0, 0], [-100000, 100000]
    # y = 0
    x2, y2 = [-10000, 50000], [10000, 10000]
    plt.grid()
    plt.plot(xvals, yvals1, label='x + y ≥ 3', c='red')
    plt.plot(xvals, yvals2, label='3x − y ≥ −1', c='blue')
    plt.plot(x1, y1, label='x<=2', c='green')
    plt.plot(x2, y2, label='y=0', c='orange')
    plt.legend(loc='best')
    plt.show()


def problem_2_4():
    red_line = (2, 4, 100000)
    blue_line = (8, 3, 2400)
    green_line = (1, 0, 0)
    yellow_line = (0, 1, 10000)

    cp1 = line_ip(green_line, red_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)

    obj_fun = lambda x, y: 25.0*x + 50.0*y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num standard   = {}'.format(x))
    print('num heavy = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p
