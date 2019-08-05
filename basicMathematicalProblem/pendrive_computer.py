# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 19:24:54 2018

@author: Atul Anand
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def findSol2(n,m):
    counter =0
    copiedIntoComputers =0
    for i in range(1,m):
        if copiedIntoComputers <n:
            copiedIntoComputers += i
            counter +=1
            
    while copiedIntoComputers <n:
        copiedIntoComputers += m
        counter +=1
        
    return counter


def findSol(n,m):
    solList=[1]
    for i in range(1,m+1):
        print(solList)
        if sum(solList) <n:
            solList.append(i)
            print("solList" ,solList)
            
    while sum(solList) <n:
        solList.append(m)
        print("solList in while ", solList)
    return len(solList)
    
t = 1#int(input())

for _ in range(t):
    n,m = 10,3#map(int, input().strip().split())
    print(findSol(n,m))
    print(findSol2(n,m))