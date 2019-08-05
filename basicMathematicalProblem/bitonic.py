
def maximum_bitonic_subarray_sum(arr):
    last = arr[0]
    cur = arr[0]
    
    best = arr[0]
    
    up = False
    
    for num in arr[1:]:
        if last < num and not up:
            up = True
            cur = last
        elif last > num:
            up = False
        elif last == num:
            up = False
            cur = 0
        
        cur += num
        print("best : ", best,"cur : ", cur)
        best = max(best, cur)
        
        last = num

        
    return max(best, cur)

if __name__ == '__main__':
    num_cases = 1#int(input())
    
    for i in range(num_cases):
        arr_len = 12112#int(input())
        
        arr = [5,3,9,2,7,6,4]#[int(x) for x in input().split()]
        
        print(maximum_bitonic_subarray_sum(arr))
        
        