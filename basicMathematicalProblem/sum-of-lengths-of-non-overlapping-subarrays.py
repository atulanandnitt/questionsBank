#https://practice.geeksforgeeks.org/problems/sum_of_lengths_of_non_overlapping_subarrays/0/?ref=self


def sum_of_lengths_of_non_overlapping_subarrays(list1,k):
    count =0
    tillNowMAx=0
    fromZeroMax=0
    fromlastMax=0
    for i in range(len(list1)):
        if k >= list1[i]:
            count += 1
            
        else:
            count =0
        tillNowMAx =max(tillNowMAx,count)
    #print("tillNowMAx :",tillNowMAx)
    
    for i in range(len(list1)):
        if k >= list1[i]:
            fromZeroMax += 1
        else:
             break
    for i in range(len(list1) -1 , -1 ,-1):
        if k >= list1[i]:
            fromlastMax += 1
        else:
            break
    #print("fromlastMax+fromZeroMax", fromZeroMax,fromlastMax,k)
    if fromlastMax == tillNowMAx and fromZeroMax == tillNowMAx:
        return tillNowMAx
    
    sol=max(fromlastMax+fromZeroMax , tillNowMAx)
    return sol


k = 1#int(input())

for _ in range(k):
    n=1#int(input())
    list1=[4,5,7,1,2,9,8,4,3,1]#list(map(int,input().strip().split()))
    k=4#int(input())
    print(sum_of_lengths_of_non_overlapping_subarrays(list1,k))
    