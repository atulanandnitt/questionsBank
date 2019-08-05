#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    result=[]
    for grade in grades:
        if grade < 38:
            result.append(grade)
        elif grade % 5 ==0:
            result.append(grade)
        elif (grade +1) % 5 ==0:
            result.append(grade+1)
        elif (grade +2) % 5 ==0:
            result.append(grade+2)
        else:
            result.append(grade)
    
    return result
        

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    n = 4#int(input())

    grades = [73,67,38,33]

    result = gradingStudents(grades)
    
    print(result)
