for i in range(10):
    if i ==5:
        continue
    
    print(i)

else:
    print(" I have completed cleanly the loop")
    
    
    
for i in range(10):
    if(i==5):
        break;
    print(i)

else:
    print(" I have completed cleanly the loop")
    
x=int(input())    
for i in range(2,(x//2) +1):
    if x %i ==0:
        print("not prime")
        break
else:
    print("prime")


    
def isPrime(x):
    for i in range(2,(x//2) +1):
        if x %i ==0:
            return ("not prime")
            
    else:
        return ("prime")
        
print(isPrime(11))        
        
