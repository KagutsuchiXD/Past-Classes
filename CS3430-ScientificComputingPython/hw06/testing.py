import unittest
from maker import maker
from hw06_parser import parser
from prod import prod
from const import const
from pwr import pwr
from var import var
from plus import plus
from tof import tof
from drv import drv
from nra import nra


s = 'x^2 - 333'
ans = nra.zr1(s, 1, num_iters=15)
print(ans)

s = 'x^2 - 11'
ans = nra.zr1(s, 1, num_iters=5)
print(ans)

s = 'x^5 - 10'
ans = nra.zr1(s, 1.0, num_iters=20)
print(ans)

s = 'x^3 - 11'
ans = nra.zr1(s, 1, num_iters=7)
print(ans)

# s = 'x^5 - 15'
# ans = nra.zr1(s, 1, num_iters=9)
# print(ans)
#
# s = 'x^7 - 3113'
# ans = nra.zr1(s, 1.25, num_iters=100)
# print(ans)
#
# s = 'x^17 - 1000131'
# ans = nra.zr1(s, 1, num_iters=200)
# print(ans)
