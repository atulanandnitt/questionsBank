
#code
def find_swap_two_nibbles_in_a_byte(n):
    binStr = bin(n)
    print(binStr)
    binLeft, binRight = binStr[:-4], binStr[-4:]
    print(binLeft, binRight)
    binLeft, binRight = binRight, binLeft
    intN = int(binStr,2)
    print(intN, binLeft, binRight, len(binRight), type(binRight))
    binRight2 = binRight[2:]
    print(binRight2)
    while len(binRight2) != 4:
        binRight2 = "0" + binRight2
    
    print(binLeft , binRight2)
    newBinStr = binLeft + binRight2
    print(int(newBinStr,2))
    
t = 1#int(input())

for _  in range(t):
    n = 19#int(input())
    print(find_swap_two_nibbles_in_a_byte(n))