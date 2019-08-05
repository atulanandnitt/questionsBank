def fibo(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def fibo_dp(n):
    a,b = 1,1
    for i in range(n):
        a,b = b, a+b

    return a

def generic(stepsAtATime, n):
    if n == 0 or n ==1:
        return 1
    else:
        for step in stepsAtATime:
            return fibo(n-1) + fibo(n-2)


for i in range(5):
    stepsAtATime = [1,3,5]
    # print(i , ":", fibo(i))
    # print(i , ":", fibo_dp(i))
    print(i, ":", generic(stepsAtATime, i))
