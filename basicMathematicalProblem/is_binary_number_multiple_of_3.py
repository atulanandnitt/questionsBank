# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 19:12:03 2018

@author: Atul Anand
"""

#code

def is_binary_number_multiple_of_3(binStr):
    n =0
    for i in range(1,len(binStr)+1):
        print(binStr[-i], i, "2**(i-1): ", (2**(i-1)),binStr[-i]*(2**(i-1)) )
        temp = int(binStr[-i])
        n += temp *(2**(i-1))
        print(n)
        #n += 2**binStr[i]
        #print(n,i)
    
    revbinStr = binStr[::-1]
    for chr1 in revbinStr:
        

    

t = 1#int(input())
for _ in range(t):
    binStr = "0000100"#input()
    print(is_binary_number_multiple_of_3(binStr))