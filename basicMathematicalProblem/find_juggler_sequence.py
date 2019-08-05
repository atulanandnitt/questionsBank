# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:34:54 2018

@author: Atul Anand
"""

#code
solList=[]
def find_juggler_sequence(n):
    solList.append(n)
    if n ==1:
        return solList
    elif n %2 ==0:
        
        return find_juggler_sequence(int(n**0.5))
    else:
        return find_juggler_sequence(int(n**1.5))

t =1# int(input())
for _ in range(t):
    n = 9#int(input())
    print(find_juggler_sequence(n))