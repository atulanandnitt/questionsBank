#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def lcm(x,y):
    if y < x: 
        x,y=y,x
    lcm=1
    mini=min(x,y)
    for i in range(2,mini+1):
        if i*y % x ==0:
            lcm=i*y
            return int(lcm)

print(lcm(4,6))        
        
        
    
        
def findLCM(a):
    lcmVal=1
    for i in range(len(a)):
        print(lcmVal,"lcmVal",type(lcmVal),"a[i]",a[i])
        lcmVal=lcm(lcmVal,a[i])
        print(lcmVal,"**************** is lcmVal")
    return lcmVal

print(findLCM([4,6,8]))     


def findHCF(b):
    pass



def getTotalX(a, b):
    #
    # Write your code here.
    #
    miniB=min(b)
    lcm_A=findLCM(a,miniB)
    hcf_B=findHCF(b)

    sol=[]
    for item in lcm_A:
        if item in hcf_B:
            sol.append(item)
    
    return sol

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = [2,3]#input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = [2,4]#list(map(int, input().rstrip().split()))

    b = [16,32,96]#list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(total)
