# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:56:26 2018

@author: Atul Anand
"""

#code
#submission has issue ??????
#https://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range/0/?ref=self

def isPrime(a):
    if a==1 or a==2:
        return True
    for i in range(2,a):
        if a %i ==0:
            return False
    else:
        print(a , "is Prime")
        return True
    
    
def findPrimeNos(m,n):
    solStr =""
    print(m,n)
    for i in range(m,n):
        print("check for ",i)
        if isPrime(i):
            solStr += " " + str(i)
        else:
            continue
            
    return solStr.strip()
    
    
    
    
t = 1#int(input())

for _ in range(t):
    
    m,n = 71,384#map(int, input().strip().split())
    print(findPrimeNos(m,n))