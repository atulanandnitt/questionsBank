

def def_print_k_smallest_elements_in_their_original_order(list1,k):
    sortedList2 = sorted(list1)
    print(list1, sortedList2)
    solStr =""
    for i in range(k):
        for j in range(len(list1)):

            if list1[j] in sortedList2[:k]:
                solStr += str(list1[j])
                print(sortedList2.pop(j))
                break
            
    return solStr.strip()
    
    


t = 1#int(input())

for _ in range(t):
    waste,k = 5,3#map(int,input().strip().split())
    list1= [5,4,2,1,2]#list(map(int, input().strip().split()))
    print(list1)
    print(def_print_k_smallest_elements_in_their_original_order(list1,k))
    
    
def k_smallest(k, arr):
    check = []
    for i in range(10 ** 5 + 1):
        check.append(0)

    b =sorted(arr)
    for i in range(k):
        check[b[i]] += 1
    res = []
    for i in range(n):
        if check[arr[i]]:
            res.append(arr[i])
            check[arr[i]] -= 1
    return res


if __name__ == '__main__':
    t = 1#int(input())
    for i in range(t):
        n, k = 5,3#[int(i) for i in input().split()][0:2]
        arr = [5,4,2,1,2]#[int(i) for i in input().split()][0:n]
        print(*k_smallest(k, arr))
    