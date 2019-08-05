# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:06:14 2018

@author: atanand
"""

#remove all the files in the particular folder

import os
import shutil


path="./newdir"
srcFile=path+"/tempo"
destFile=path+"/tempo_backup"
newName=path+"/tempo_new"

if os.path.exists(path):
    if os.path.isFile(srcFile):
        shutil.copy(srcFile.destFile)
        os.rename(srcFile,newName)

        