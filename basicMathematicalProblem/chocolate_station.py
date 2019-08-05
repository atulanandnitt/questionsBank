

def chocolate_station(list1,wt):
    list1.insert(0,0)
    dif=0
    maxTillNowDiff=-99999
    for i in range(len(list1) -1):
        dif += list1[i] - list1[i+1]
        maxTillNowDiff=max(maxTillNowDiff,dif - list1[i] - list1[i+1])
    return -1*maxTillNowDiff*wt
    
    

t = 1#int(input())

for _ in range(t):
    list1=[1,2,3]#list(map(int,input().strip().split()))
    wt=10#int(input())
    print(chocolate_station(list1,wt))    