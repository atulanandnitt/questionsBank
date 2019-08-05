# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:07:14 2018

@author: Atul Anand
"""

#code

import itertools

def find_sum_of_bit_differences(list1):
    sol=0
    for t1 in itertools.combinations(list1,2):
        a=bin(t1[0])
        b=bin(t1[1])
        xorVal = bin(int(t1[0]) ^ int(t1[1]))
        xorValStr=  str(xorVal) 
        print(xorValStr , type(xorValStr))
        #countOfOnes=xorValStr.count(1)
        countOfOnes=0
        for ch in xorValStr:
            if ch =='1':
                countOfOnes += 1
        sol += countOfOnes
        print("countOfOnes :", countOfOnes, t1)
    return sol
    
    
    
t = 1#int(input())

for _ in range(t):
    waste = 1#int(input())
    list1 = [7,8,6,4]#list(map(int, input().strip().split()))
    print(find_sum_of_bit_differences(list1) )