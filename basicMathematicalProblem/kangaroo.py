#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2 and x1 != x2:
        return "NO"
    
    elif v1 > v2:
        while x1 < x2:
            x1=x1+v1
            x2=x2+v2
            if x1 == x2:
                return "YES"
        return "NO"
            
    
    elif v1 < v2:
        while x1 > x2:
            x1=x1+v1
            x2=x2+v2
            if x1 == x2:
                return "YES"
        return "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = [43,2,70,2]

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
