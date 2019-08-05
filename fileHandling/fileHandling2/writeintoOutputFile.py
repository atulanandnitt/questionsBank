# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:18:02 2018

@author: atanand
"""

#file handling

def writeintoaFile():
    val=open(input('input.txt'))
    print(val)
    
writeintoaFile()


#closer of the file is taken care by with statement.we dont need to close it explicitly
with open('output.txt','w') as f:
    f.write("Hi there")    