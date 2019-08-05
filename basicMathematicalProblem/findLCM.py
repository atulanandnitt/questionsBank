#code

import itertools

def findLCM(a,b):
    
    mini = min(a,b)
    maxi = max(a,b)
    for i in range(1,mini+1):
        print(maxi *i)
        if (( maxi *i ) % mini) ==0:
            return maxi *i
            


t = 1#int(input())
for _ in range(t):
    n = 5#int(input())
    list1=[i for i in range(1,n+1)]
    lcmTemp=1
    lcmMax=1
    for t1 in itertools.combinations(list1,4):
        lcm1 = findLCM(t1[0],t1[1])
        lcm2 = findLCM(t1[2],t1[3])
        lcmTemp = findLCM(t1[2],t1[3])
        
        lcmMax = max(lcmMax , lcmTemp)
    
    print(lcmMax)
        