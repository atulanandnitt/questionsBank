# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 22:56:56 2018

@author: Atul Anand
"""

# Sample bash code




def findSol(x1,y1,x2,y2,r):
    #print("SAFE")
    if (x2 **2)  + ( ((x2-x1+y2-y1)/(x2-x1)) **2) > r**2:
        return "SAFE"
    
    elif (x2 **2)  + ( ((x2-x1+y2-y1)/(x2-x1)) **2) == r**2:
        return "JUST MISSED"
    
    else:
        return "REPLANNING"
    
    
    
    
    
    
t = 1#int(input())
print(t)
for _ in range(t):
    #list1 = [5, 5 ,-5, 5 ]#
    list1=list(map(int,input().strip().split()))
    #list1= [1,2,3,4]
    x1 = list1[0]
    y1 = list1[1]
    x2 = list1[2]
    y2 = list1[3]
    r=5#4#int(input())
    print(x1,y1,x2,y2)
    print(findSol(x1,y1,x2,y2,r))
    
    
    
dict1={"a":1,"b":2}
dict2={"y":25,"z":26}

for key,val in dict1.items():
    dict2[key] = dict1[key]
print(dict2)
# dict3 = dict1+dict2 wrong
dict2.update(dict1)
print(dict2)
    