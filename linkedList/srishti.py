import math
import random

print(5+4)
a=4
b=5
print(a+b)
list1=range(1,11)
print("list1 : ",list1)
list1=list(range(1,11))
print("list1 2nd time: ",list1)
print("list1 slicing",list1[1:-1])

for i in range(1,11):
    print(i)

def summation():
    a=5
    b=9
    c=a+b
    return c

print(summation())


def summation(a,b):
    c=a+b
    return c

a=5
b=9
print(summation(a,b))


for i in range(26):
    print(chr(ord('A')+i))

for i in range(0,26,1):
    print(chr(ord('a')+i))



sol3=[]    
for i in range(16):
    sol3.append(chr(ord('a')+i +random.randint(1,10)))    
    
print(sol3) 
set1=set(sol3)

dict1={ key1 : sol3.count(key1) for key1 in set1 }
print(dict1)
   