import itertools    
n=int(input())    
import random
valList=[]
valStr=""
for _ in range(n):
    valStr += (str(random.random())[2])
print(valStr)
val=int(valStr)
for item in valStr:
    valList.append(item)
test=(itertools.combinations(valList,4))
print(test)



"""
for i in range(26):
    with open(chr(ord('a') + i) +".txt" ,"w") as f1:
        f1.write(chr(ord('a') + i))
        
import os  
list1=['p','y','t']      
for parentFile,subFolder,fileList in os.walk("D:/CRM/generic/home/rahul/python_language/objective_doubts/basicDataStructure/basicMathematicalProblem/alphabet"):
    print(fileList)
    data=""
    for fileName in fileList:
        with open(fileName,"r") as f1:
            data = f1.read()
            if data in list1:
                print(data," in ",fileName)
            
list1=['p','y','t']
key='p'
if key in list1:
    print("FOUND")

"""