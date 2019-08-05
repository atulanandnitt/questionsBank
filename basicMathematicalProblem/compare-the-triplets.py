#!/bin/python3
#https://www.hackerrank.com/challenges/compare-the-triplets/problem


import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    pointA,pointB=0,0
    for val1,val2 in zip(a,b):
        if val1 > val2:
            pointA += 1
        elif val1 < val2:
            pointB +=1
        else:
            continue
    return pointA,pointB

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a =[5,6,7]# list(map(int, input().rstrip().split()))

    b =[3,6,10]# list(map(int, input().rstrip().split()))

    result = solve(a, b)

    print(result)
