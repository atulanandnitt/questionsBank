#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/what-is-the-string-made-of-2/
# Write your code here

def findNoOfStick(str1):
    sticks=0
    for num in str1:
        if num =="1": sticks += 2
        if num =="2": sticks += 5
        if num =="3": sticks += 5
        if num =="4": sticks += 4
        if num =="5": sticks += 5
        if num =="6": sticks += 6
        if num =="7": sticks += 3
        if num =="8": sticks += 7
        if num =="9": sticks += 6
        if num =="0": sticks += 6
    
    return sticks
    
t = 1#int(input())

for _ in range(t):
    str1="12134"# input()
    print(findNoOfStick(str1))