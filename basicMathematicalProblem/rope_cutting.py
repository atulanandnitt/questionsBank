

t=1#int(input())
for _ in range(t):
    n=1#int(input())
    l=[5,1,1,2,3,5]#[int(i) for i in input().split()]
    l.sort()
    k=l[0]
    print(l)
    #k=min(l)
    for i in range(0,n):
        if(l[i]-k>0):
            print(n-i,end=" ")
            k=l[i]
            print(k)
    print("done")
        
    
   
            
        