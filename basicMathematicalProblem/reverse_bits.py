# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:33:23 2018

@author: Atul Anand
"""

#code

#def reverse_bits():
    
def findDecimal(bit32):
    decimalVal=0
    for i in range(len(bit32)-1,-1,-1):
        #print(i)
        if bit32[i] == "0":
            continue
        else:
            decimalVal += int(bit32[i]) *(2** (31-i))
    return decimalVal
    


def find32Bit(n):
    binN= str(bin(n))
    print(binN)
    binN=binN[2:]
    print(binN)
    length = len(str(binN))
    for i in range(length,32):
        binN= "0" + binN
    print(binN)
    
    revBin = binN[::-1]
    print(revBin)
    return revBin

t = 1#int(input())

for _ in range(t):
    n = 1#int(input())
    bit32 = find32Bit(n)
    print(findDecimal(bit32))
    
    
    



print(str2[len(str2)-1:-1])    



print(str2[1:2:-1])    