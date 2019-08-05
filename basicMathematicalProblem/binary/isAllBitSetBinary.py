# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:33:57 2018

@author: atanand
"""

#code
#code



def isAllBitisSet(num):
    bin_num= bin(num)
    str_bin = bin_num
    print(str_bin)
    for i in range(2,len(str_bin)):
        if str_bin[i] != "1":
            return "NO"
            
    return "YES"
    
    
t= 1#int(input())

for _ in range(t):
    num=63#int(input())
    print(isAllBitisSet(num))