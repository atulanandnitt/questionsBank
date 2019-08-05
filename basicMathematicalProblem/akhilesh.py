def findSol(arrde):

        arrde.sort(key=lambda x:x[0])
        n = len(arrde)
        solList=[arrde[0]]
        for x in range(1,n):
            print("solList : ",solList, "arrde[x]", arrde[x][0])
            if arrde[x][0] +1 <= solList[-1][1]:
                    solList[-1][1] = max(solList[-1][1] , arrde[x][1])
            else:
                solList.append(arrde[x])
                    
        return (solList)
    
list1=[ [3,6],
       [12,15],
       [4,4],
       [1,6],
       [11,15],
       [7,10]]

list1.sort(key=lambda x:x[0])
print("list1 :", list1)
print(findSol(list1))





arrList = [[2, 5],
           [1,3],
           [1,7],
           [12,14],
           [20,22]]

arrList=[[3,5],
              [6,8],
              [17,22],
              [1,4],
              [21,30],
              [16,16],
              [31,33],
              [11,15]]









def fun_lis(list1):
    
    lis=[1 for i in range(len(list1))]
    print(lis)
    for i in range(len(list1)):
        for j in range(i):
            if list1[j] < list1[i]:
                lis[i] = max(lis[i], lis[j]+1)
    print(lis)
    return max(lis)


list1=[4,5,3,6,2,7,1,8,9]
print(fun_lis(list1))

def lcs(str1,str2,m,n):
    if m==0 or n==0:
        return 1
    elif str1[m-1] == str1[n-1]:
        return 1+lcs(str1,str2,m-1,n-1)
    else:
        return max(lcs(str1,str2,m-1,n),lcs(str1,str2,m,n-1))
    
    
str1="atul"
str2="anand"
m=len(str1)-1
n=len(str2)-1  
print(lcs(str1,str2,m,n))    


def lcs(X,Y,m,n):#str1:X str2:Y m=len(str1) n=len(str2)
    if m==0 or n==0:
        return 0
    
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X,Y,m-1,n-1)
    
    else:
        return max(lcs(X,Y,m-1,n), lcs(X,Y,m,n-1))
    
str1="atul"
str2="anand"
print(lcs(str1,str2,len(str1),len(str2)))    
