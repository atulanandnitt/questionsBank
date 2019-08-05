# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 08:18:21 2018

@author: Atul Anand
"""

list1=[1,2,3,4,7,9]
list2=[3,4,5,6,7,8]

set1=set(list1)
set2=set(list2)

unionVal = set1.union(set2)

intersectionVal = set1.intersection(set2)



def findUnion(list1,list2):
    i,j =0,0
    union=[]
    while True:
        
        if list1[i] < list2[j]  :
            if list1[i] not in union:
                union.append(list1[i])
                i += 1
                print(i)
        
        elif list1[i] > list2[j]  and list2[i] not in union:
            union.append(list2[j])
            j += 1
            print(j)
            
            
        if len(list1) == i :
            union += list2[j:]
            break
            
        elif len(list2) == j:
            union += list1[i:]
            break
        
        if len(list1) == i  and len(list2)== j:
            break
        
        print("union till now", union)
    
    return union

print(findUnion(list1,list2))
