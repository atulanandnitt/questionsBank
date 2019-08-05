#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    countA, countO =0,0
    for apple in apples:
        if apple +a >= s and apple +a <= t:
            countA += 1
            #print(countA , apple + a)
    
    for orange in oranges:
        if orange + b >= s and orange + b <= t:
            countO += 1
    
    print(countA)
    print(countO)
    
    
    
    

if __name__ == '__main__':
    st = 1#input().split()

    s = 7#int(st[0])

    t = 11#int(st[1])

    ab =1# input().split()

    a = 5#int(ab[0])

    b = 15#int(ab[1])

    mn = 1#input().split()

    m = 3#int(mn[0])

    n = 2#int(mn[1])

    apple = [-2,2,1]#list(map(int, input().rstrip().split()))

    orange = [5,-6]#list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
