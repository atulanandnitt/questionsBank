# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:41:36 2018

@author: Atul Anand
"""


def squares_difference(n):
    square = n **2
    print(square)
    sumOfSquares=0
    for i in range(n+1):
        sumOfSquares += i **2
        print(sumOfSquares, i**2)
    return abs(sumOfSquares - square)

t = 1#int(input())
for _ in range(t):
    n = 10#int(input())
    
    print(squares_difference(n))