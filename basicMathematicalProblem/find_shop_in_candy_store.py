# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:37:48 2018

@author: Atul Anand
"""

#code


def findMax(candiesPricesForMax,k):
    candiesPricesForMax2=candiesPricesForMax[::-1]
    print(candiesPricesForMax2,"from max")
    maxi =0
    while len(candiesPricesForMax2) >0:
        
        maxi += candiesPricesForMax2[0]
        candiesPricesForMax2.pop(0)
        for i in range(k):
            if len(candiesPricesForMax2)>0:
                candiesPricesForMax2.pop()
    return maxi
    
def findMin(candiesPricesForMini,k):
    print(candiesPrices,"from mini")
    mini =0
    #takenCandyCount =0
    while len(candiesPricesForMini) >0:
        
        mini += candiesPricesForMini[0]
        #takenCandyCount += 1
        candiesPricesForMini.pop(0)
        print(candiesPricesForMini, "candiesPricesForMini",k)
        #takenCandyCount += candy
        for i in range(k):
            if len(candiesPricesForMini)>0:
                candiesPricesForMini.pop()
                print(candiesPricesForMini, "candiesPricesForMini")
    return mini
    
def find_shop_in_candy_store(candiesPrices,k):
    candiesPrices.sort()
    candiesPricesForMini = candiesPrices
    candiesPricesForMax = []
    for item in candiesPricesForMini:
        candiesPricesForMax.append(item)
    mini = findMin(candiesPricesForMini,k)
    maxi = findMax(candiesPricesForMax,k)
    return mini,maxi
    
   
t = 1#int(input())

for _ in range(t):
    waste,k = 4,2#map(int, input().strip().split())
    candiesPrices = [3,2,1,4]#list(map(int, input().strip().split()))
    print(find_shop_in_candy_store(candiesPrices,k))