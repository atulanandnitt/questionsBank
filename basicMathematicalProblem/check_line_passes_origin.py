# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:04:55 2018

@author: atanand
"""

def check_line_passes_origin(p1,p2):
    return p1[1] * (p2[0] - p1[0]) == p1[0] * (p2[1] - p1[1])


p1=[10,0]
p2=[20,0]

p1=[10,0]
p2=[20,1]
print(check_line_passes_origin(p1,p2))
    