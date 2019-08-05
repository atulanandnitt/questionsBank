# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:02:56 2018

@author: atanand
"""

# file handling for LRG

import csv

def FindDetailsOfParticularFile(absfileName):
    result=[]
    
    print(absfileName)
    with open(absfileName,'r') as f:
        for line in f:
            if 'starttime=' in line:
                result.append(line)
                print(line)
                
    
    with open(absfileName,'r') as f:
        for line in f:
            if 'endtime=' in line:
                result.append(line)
                print(line)
    
                
    with open(absfileName,'r') as f:
        for line in f:
            if 'out: Row Count = ' in line:
                result.append(line)
                print(line)
            
    with open(absfileName,'r') as f:
        for line in f:
            if 'ref: Row Count = ' in line:
                result.append(line)
                print(line)
                
    f = open('csvfile.csv','w')
    resultstr=str(result[0])+","+str(result[1])+","+str(result[2])+","+str(result[3])
    f.write(resultstr)
    f.close()
"""
  for item in result:
        f.write(str(item)) #Give your csv text here.
    ## Python will convert \n to os.linesep
"""
    

"""
    with open('csvfile.csv','wb') as file:
        for line in result:
            file.write(line)
            file.write('\n')
"""
absfileName ="REL8_QM_ActualSeasonality_1.dif"
#FindDetailsOfParticularFile('D:\CRM\Sprint\R13_18-05_sprint6_Partner Program\REST_API\python\objective_doubts\basicDataStructure\fileHandling\REL8_QM_ActualSeasonality_1.dif')
FindDetailsOfParticularFile(absfileName)

"""            
    f_contents = f.read()
    print(f_contents)
    for item in f_contents:
        print(item)
        
"""


n = int(input())
print(n, type(n))


