import string
from collections import defaultdict
from typing import List
import math

def Spiral(n: int):
    x = 0 # x coordinate
    y = 0  # y coordinate

    move_x = 0
    move_y = 1

    # ohhhh we change directions when:
    # x == y UNLESS
    # x<0 and y>0 THEN change directions when:
    # x = y-1

    for i in range(n):
        if abs(x) == abs(y) and x>0 and y>0:
            move_x, move_y = move_y, -move_x
        if abs(x) == abs(y) and x > 0 and y<0:
            move_x, move_y = move_y, -move_x
        if abs(x) == abs(y) and x < 0 and y<0:
            move_x, move_y = move_y, -move_x
        elif x<=0 and y>0 and abs(x) == abs(y)-1:
            move_x, move_y = move_y, -move_x

        x,y = x+move_x, y+move_y
        print(x,y)


    return [x,y]


test_n = 11
print(Spiral(test_n))







