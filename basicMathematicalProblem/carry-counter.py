def carry_counter(m,n):
    count =0
    mStr=str(m)
    nStr=str(n)
    mLen=len(mStr)
    nLen=len(nStr)
    for i in range(min(mLen,nLen)):
        print(int(mStr[0-i-1]) + int(nStr[0-i-1]))
        if (int(mStr[0-i-1]) + int(nStr[0-i-1]) ) > 9:
            count += 1
            mStr[0-i-2] += 1
            if mStr[0-i-2] >9:
                mStr[0-i-3] +=1
    return count
        
    
    

t=1# int(input())

for _ in range(t):
    m,n= 191,2229#map(int,input().strip().split())
    print(carry_counter(m,n))


"""
def carry_counter(m,n):
    count =0
    mStr=str(m)
    nStr=str(n)
    mLen=len(mStr)
    nLen=len(nStr)
    for i in range(min(mLen,nLen)):
        print(int(mStr[0-i-1]) + int(nStr[0-i-1]))
        if (int(mStr[0-i-1]) + int(nStr[0-i-1]) ) > 9:
            count += 1
            mStr[0-i-2] = int(mStr[0-i-2]) + 1
            
            
            if mStr[0-i-2] >9 :
                try:
                    mStr[0-i-3] = int(mStr[0-i-3]) + 1
                except:
                    continue
    return count
    

t= int(input())

for _ in range(t):
    m,n= list(map(int,input().strip().split()))
    print(carry_counter(m,n))
    
"""    