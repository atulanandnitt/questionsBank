# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:17:35 2018

@author: atanand
"""


import os

path ="C:\Users\atanand.ORADEV\Documents\home\rahul\python_language\objective_doubts\basicDataStructure"

if not os.path.exists(path):
    os.mkdir(path)
    
filename="inputFile.txt"

line1 = input('line 1 : ')


temp_file=open(os.path.join(path,filename),'w')
temp_file.write(line1)

temp_file.close()

