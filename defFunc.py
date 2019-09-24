# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

def quadratic(a, b, c):
    sq = b * b - 4 * a * c
    if sq < 0:
        print('No solution')
    elif sq == 0:
        x = (-b)/(2 * a)
        return x
    else:
        x1 = ((-b) + math.sqrt(sq)) / (2 * a)
        x2 = ((-b) - math.sqrt(sq)) / (2 * a)
        return x1, x2