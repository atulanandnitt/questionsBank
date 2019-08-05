# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:45:19 2018

@author: Atul Anand
"""

#https://practice.geeksforgeeks.org/viewSol.php?subId=10349670&pid=945&user=DedeepyaLekkala

#code
N=32
def trail_of_ones():
    f=[0]*(N+1)
    f[0]=0
    f[1]=1
    for i in range(2,N+1):
        f[i]=f[i-1]+f[i-2]
    return f
fi=trail_of_ones()
t=1#int(input())
for i in range(t):
    n=5#int(input())
    #print(2**n-(fi[n+2]))
    
    

for t in range(1):
    n = 5#int(input())
    
    M = [[0,0] for i in range(n)]
    M[0] = [1,1]
    for i in range(1,n):
        M[i][0] = sum(M[i-1])
        M[i][1] = M[i-1][0]
        print(M[i])
    without = sum(M[n-1])
    total = (2**n)
    print(total-without)
        