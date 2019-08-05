#https://practice.geeksforgeeks.org/problems/closest-number/0

#code

def requiredNo(m,n):
    a=n%m
    
    if abs(a)<abs(m-a):
        return (n-a)
    elif abs(a)>abs(m-a):
        return(n+m-a)
    else:
        if n<0:
            return(n-a)
        else:
            return(n+a)
    
    
    
t = int(input())

for _ in range(t):
    m,n=list(map(int,input().strip().split()))
    print(requiredNo(n,m))
    
    
    
import os
for parentFolder,subFolder,fileNameList in os.walk("D:/CRM/generic/home/rahul/python_language/objective_doubts/basicDataStructure/basicMathematicalProblem"):
    print(fileNameList)
    
    
import os
for item in os.walk("D:/CRM/generic/home/rahul/python_language/objective_doubts/basicDataStructure/basicMathematicalProblem"):
    print(item)    