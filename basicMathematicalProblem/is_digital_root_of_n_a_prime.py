# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:41:51 2018

@author: Atul Anand
"""

#code

def isPrime(digitalRoot):
    if digitalRoot in [0,1,2,3,5,7]:
        return 1
    else:
        return 0
    
    
def getDigitSum(n):
    sumOfDigits=0
    
    while n >9:
            sumOfDigits += n%10
            n = n // 10
            print("sumOfDigits : " ,sumOfDigits,"n :",n)
    sumOfDigits += n%10
    print("sumOfDigits" ,sumOfDigits)
    return sumOfDigits
    
def is_digital_root_of_n_a_prime(n):
   
    tempRoot = getDigitSum(n)
    
    print("tempRoot ",tempRoot)
    while tempRoot >9:
        tempRoot = getDigitSum(n)
        n = tempRoot
    
    digitalRoot =tempRoot  
    
    return isPrime(digitalRoot)
    
    
t = 1#int(input())

for _ in range(t):
    n = 9740#int(input())

    
    print(is_digital_root_of_n_a_prime(n))