#code
import math

def gcd(b, n):
    if n % b ==0:
        return b
    else:
        return gcd(b,n%b)
    
    
def isRelativePrime(b,n):
    if gcd(b, n) == 1 :
        return 1
    else:
        return 0
    
    
def isCarmichael(n):
    for b in range(n):
        if isRelativePrime(b,n):
            if pow(b, n-1) % n == 1:
                return "Yes"
    else:
        return "No"
            


if __name__ == '__main__':
    num_cases = int(input())
    
    for i in range(num_cases):
        n = int(input())
        
        print(isCarmichael(n))
        
        
