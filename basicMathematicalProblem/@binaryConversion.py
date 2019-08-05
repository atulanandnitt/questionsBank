
def findBitDiff(a,b):
    c=bin(a^b)[2:].count('1')
    print(bin(a^b))
    return c

t = int(input())

for _ in range(t):
    a,b = map(int, input().strip().split())

    print(findBitDiff(a,b))
    