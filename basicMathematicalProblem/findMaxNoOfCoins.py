#https://www.hackerearth.com/practice/algorithms/dynamic-programming/state-space-reduction/practice-problems/algorithm/bytelandian-gold-coins/

def findMax(n):
    
    if n//2 ==0 and n//3 ==0 :#and n//4 ==0:
        return 1
        
    elif n > (n/2 + n/3 + n/4):
        return n
    
    else:
        return findMax(n//2) + findMax(n//3) + findMax(n//4)

t= 1#int(input())

for _ in range(t):
    n=12# int(input())
    print(findMax(n))