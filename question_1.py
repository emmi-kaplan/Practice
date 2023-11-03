import string
from collections import defaultdict
from typing import List
import math

def excelSum(formula: str):  #data: List[List[float]],
    sum = 0
    form = formula[5:-1]  # this is the string without the unnecesary chars
    form_array = form.split(",")    # next we want to create a list separated by commas
    indexed_array = [] # make each cell eg A1 a list with index of alphabet for column and number for row eg. A1 = [0,0]  E6= [4,5]
    for i in form_array:
        if ':' in i:
            pass  # here we must slice the string again
        else:
            indexed_array.append([string.ascii_uppercase.index(i[0]), int(i[1])-1])
            # turn the letters into alphabet index
            #sum += cell value          find the value of the single cell

    return sum


if abs(x) == abs(y) and x > 0 and y > 0:
    move_x, move_y = move_y, -move_x
    print(n, "case 1")
if abs(x) == abs(y) and x > 0 and y < 0:
    move_x, move_y = move_y, -move_x
    print(n, "case 2")
if abs(x) == abs(y) and x < 0 and y < 0:
    move_x, move_y = move_y, -move_x
    print(n, "case 3")
elif x <= 0 and y > 0 and x == y - 1:
    move_x, move_y = move_y, -move_x
    print(n, "case 4")




test_formula = '=Sum(A1, A2)'
print(excelSum(test_formula))