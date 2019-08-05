# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:11:39 2018

@author: Atul Anand
"""

def swaptwoNibblesInAByte(n): 
    binaryVal = bin(n)[2:]
    print(binaryVal )
    length = len(binaryVal)
    while length <8:
        binaryVal = "0" + binaryVal
        length = len(binaryVal)   
        
    half = length //2
    firstNibble = binaryVal[:4]
    lastNibble =  binaryVal[4:]
    solBin = lastNibble+firstNibble
    print( firstNibble , lastNibble)
    print(lastNibble , firstNibble)
    print(solBin)
    decimalVal = int(solBin,2)
    return decimalVal
    
t = int(input())

for _ in range(t):
    n = int(input())
    print(swaptwoNibblesInAByte(n))
    