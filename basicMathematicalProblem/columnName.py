# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:48:35 2018

@author: Atul Anand
"""

def columnName_sort(n):
    str1=""
    while(n):
        rem=n%26
        n//=26
        if(rem==0):
            rem=26
            n-=1
        str1+=chr(64+rem)
    return (str1[::-1])
    
    
def columnName(n):
    n = n-1
    alpha=[]
    colInd=0
    colName=""
    for i in range(65,91):
        alpha.append(chr(i))
    #print(alpha)
    lastCharCount= n%26
    while n > 26:
        
        colInd = n // 26
        colName = alpha[colInd-1] + colName
        lastCharCount = n%26
        n = n//26

        print("colName ",colName)
        
    colName =  colName +alpha[lastCharCount]
    return colName
    
for i in range(1,100):
    colName =columnName_sort(i)    
    print(i, ": " ,colName)