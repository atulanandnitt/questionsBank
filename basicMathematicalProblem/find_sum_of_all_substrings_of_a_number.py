
#code
import itertools

def find_sum_of_all_substrings_of_a_number(n):
    str1 = str(n)
    print(str1)
    list1 = []
    for chr1 in str1:
        list1.append(int(chr1))
        
    sol =0
    for i in range(1,len(list1)):
        for t1 in itertools.combinations(list1,i):
            print(t1, type(t1))
            sol += sum(t1)
    return sol


    
def find_sum_of_all_substrings_of_a_number_2(n):
    sum1=0
    for i in range(len(n)):
        for j in range(i+1,len(n)+1):
            print(" sum1 :", sum1, "n[i:j] :",n[i:j] )
            sum1 = sum1 + int(n[i:j])
    return (sum1)
    
    
t = 1#int(input())
for _ in range(t):
    n = "1234"#int(input())
    #print(find_sum_of_all_substrings_of_a_number(n))
    print(find_sum_of_all_substrings_of_a_number_2(n))