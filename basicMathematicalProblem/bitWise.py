#code

def findBitDif(a,b):
    sol = a ^ b
    solStr = str(bin(sol))
    count = 0
    for i in range(len(solStr)):
        print("solStr[i]",solStr[i])
        if solStr[i] == '1':
            count += 1
    return count
    
t = 1#int(input())
for _ in range(t):
    a, b = 10,20#map(int, input().strip().split())
    print(findBitDif(a,b))