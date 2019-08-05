# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 00:42:33 2018

@author: Atul Anand
"""



def genNumber( n ):
    digits = [ 0, 1, 2, 3, 4, 5 ]
    output = []
    
    while n >= 6:
        print(n%6)
        output.append( n % 6 )
        n = n // 6
    print(n)
    output.append( n )
    output.reverse()
    return "".join( [ str( x ) for x in output ] )
    

#INPUTS
T = 1#int( input() )
for _ in range(T):
    n = 100#int( input() ) - 1
    print( genNumber( n-1 ) )
    