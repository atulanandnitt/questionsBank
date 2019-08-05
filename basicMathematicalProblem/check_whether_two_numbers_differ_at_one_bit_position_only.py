
def check_whether_two_numbers_differ_at_one_bit_position_only(a,b):
    c = a^b
    binC = bin(c)
    strC=""
    for chr1 in binC:
        strC += str(chr1)
    print(strC, type(strC))
    if strC.count('1') ==1:
        return 1
    else:
        return 0
    
    
t = 1#int(input())
for _ in range(t):
    a,b = 13,9#map(int, input().strip().split())
    
    print(check_whether_two_numbers_differ_at_one_bit_position_only(a,b))