

def check_if_the_number_is_balanced(n):
    list1=[]
    while n>9:
        list1.insert(0,n%10)
        n = n//10
    list1.insert(0,n)
    print("list1 ", list1)
    leftSum = sum(list1[:(len(list1)//2)])
    rightSum = sum(list1[(len(list1)//2)+1:])
    return leftSum,rightSum
    if leftSum == rightSum:
        return 1
    else:
        return 0

t = 1# int(input())
for _ in range(t):
    n = 1234006#int(input())
    
    print(check_if_the_number_is_balanced(n))