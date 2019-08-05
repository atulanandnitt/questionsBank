# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:05:04 2018

@author: atanand
"""

#Regex
# file duplication

# Import the os module, for the os.walk function
import os

#os.path.walk in python2 is same as os.path in python3

# Set the directory you want to start from
rootDir = 'D:/CRM/generic/home/rahul/python_language/objective_doubts/basicDataStructure/fileHandling'
"""
for dirName, subdirList, fileList in os.walk(rootDir,topdown = True):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
"""        

print("atul's way")        
for item in os.walk(rootDir,topdown =True,top=True,onerror = None,followlinks = False):#by default topdown =True
    print(item)        
    
print("atul's way 2 ")      
for item in os.walk(rootDir,topdown =False):
    print(item)        

print("atul's way 3")  
for item in os.walk(rootDir):
    print(item)            
    
import os
 
# The top argument for walk
topdir = '.'
 
# The extension to search for
exten = '.py'
 
for dirpath, subdirList, fileList in os.walk(topdir):
    for fname in fileList:
        if fname.lower().endswith(exten):
            print(os.path.join(dirpath, fname))    
            

