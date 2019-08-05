
def findSol(list1):
    sol = 0
    # 1, 2, 3
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            print("i and j : ",i,j)
            temp = 0
            if i == j:
                temp = list1[i] ** 2
                print("if : temp : ", temp)
            else:
                temp = sum(list1[i:j+1]) * max(list1[i:j+1])
                print(list1[i:j])
                # print("else : temp : ", temp, sum(list1[i:j]) , "max(list1[i:j] :", max(list1[i:j]), list1[i:j])
            sol += temp
            print(sol, temp, list1[i:j])
    return sol


def findSol2(list1):
    sol = 0
    n = len(list1)
    solList = [list1[i:j+1] for i in range(n) for j in range(i,n)]
    solList2 = [item[0] * item[0] if len(item) == 1 else sum(item) * max(item) for item in solList]

    return sum(solList2)

import time
start = time.time()


n = 9999
list1 = list()
for item in range(1,n+1):
    list1.append(item)
# print(list1[0:1])

# print(findSol(list1))
print(findSol2(list1))
end = time.time()
print(end - start)


"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    N = int(input())
    list1 = list()
    for _ in range(N):
        list1.append(int(input()))
    sol = 0
    n = len(list1)
    solList = [list1[i:j+1] for i in range(n) for j in range(i,n)]
    solList2 = [item[0] * item[0] if len(item) == 1 else sum(item) * max(item) for item in solList]

    print( sum(solList2) , end="")

main()


"""