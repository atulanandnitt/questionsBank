# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:01:17 2018

@author: atanand
"""

with open("input.txt","r") as f1:
    data=f1.read()
    
    print(data)
    
    


from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 0 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


print(isPrime(1))     