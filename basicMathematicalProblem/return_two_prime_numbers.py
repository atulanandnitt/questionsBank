# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:21:43 2018

@author: Atul Anand
"""
import math
if __name__=='__main__':
    t=1#int(input())
    for _ in range(t):
        n=1111#int(input())
        arr=[True]*n
        arr[0]=False
        arr[1]=False
        last=int(math.sqrt(n))+1
        for i in range(2,last):
            j=2
            while j*i<n:
                arr[j*i]=False
                j+=1
        for i in range(2,n//2+1):
            if arr[i] and arr[n-i]:
                print(i,n-i)
                break
            
        