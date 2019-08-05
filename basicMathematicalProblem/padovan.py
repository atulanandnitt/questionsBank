# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:36:52 2018

@author: Atul Anand
"""

def padovan(x):
    prevprev, prev, curr, nextp = 1, 1, 1, 1
    for j in range(3,x+1):
        nextp = prevprev+prev
        prevprev = prev
        prev = curr
        curr = nextp
    return nextp
        
for i in range(int(input())):
    n = int(input())
    ans = padovan(n)
    print(ans%1000000007)