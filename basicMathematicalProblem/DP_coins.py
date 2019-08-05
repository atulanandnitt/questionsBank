def minNoOfCoinsReq(coins,val):
    
    mini=[9999 for item in range(val+1)]
    mini[0]=0    
    
    for coin in coins:
        for j in range(val+1):
            mini[j]=min(mini[j] , 1+mini[j - coin])
    
    
    return mini[val]




def noOfWaysOfChange(coins,val):
    noOfways=[0 for item in range(val+1)]
    noOfways[0]=1
    for coin in coins:
        for j in range(coin,val+1):
            noOfways[j] += noOfways[j - coin]
        
    return noOfways[val]


coins = [3,5,7]
val=15

print(minNoOfCoinsReq(coins,val))

print(noOfWaysOfChange(coins,val))