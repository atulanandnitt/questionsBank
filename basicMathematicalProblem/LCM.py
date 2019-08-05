# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:43:58 2018

@author: atul
"""


     

#LCM

def lcm(a,b):
    if a<b:
        a,b=b,a
    count =1
    for i in range(a,(a*b)):
        print (count)
        if (a*count) %b ==0:
            return a*count
        count +=1

a=10
b=11
print("lcm is :",lcm(a,b))        
c=20
print("lcm is :",lcm(c,lcm(a,b)))


#HCF

def hcf(a,b):
    if a<b:
        a,b=b,a
    
    for i in range(b,0,-1):
        if a%i ==0 and b%i ==0:
            return i
a=10
b=110

print("hcf is :" ,hcf(a,b))     


#to binary

def binaryToDecimal(binaryNo):
    decimalNo=0
    power =0
    
    while binaryNo >0:
        decimalNo += 2 ** power *int((binaryNo % 10))
        print("decimalNo",decimalNo,"binaryNo",binaryNo)
        binaryNo //=10 #binaryNo = binaryNo /10
        power += 1
    
    return decimalNo

binaryNo =1010
print(binaryToDecimal(binaryNo))



def decimalToBinary(decimalNo):
    power =0
    binaryNo=0
    
    while decimalNo >0:
        binaryNo += 10 ** power * int(decimalNo % 2)
        decimalNo = decimalNo /2
        power +=1
    return binaryNo

print(decimalToBinary(9))   



def convert(fromNum,fromBase,toBase):
    power =0
    toNum=0
    
    while fromNum >0:
        toNum += fromBase ** power * int(fromNum % toBase )
        fromNum //= toBase
        power +=1
    return toNum

print(convert(22,10,2))
print(convert(10110,2,10))    

print(convert(22,16,10))
print(convert(34,10,16))    


def hexadecimalToDecimal(n):
    print (n)
    for ch in str(n):
        print(ch)
        
n="ab"
print(hexadecimalToDecimal(n))

x=4.89        
y1=str(x)
print(type(y1))

y2=print(x)
print(type(y2))