''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import itertools
def findNumPairs(list1):
    counter = 0
    pairs = list()
    for t1 in itertools.combinations(list1,2):
        if t1[0] > t1[1]:
            counter += 1
            pairs.append(t1)
    return len(pairs), pairs




def main():

 # Write code here
    list1 = [4,1,2,3]#list(map(int, input().split().strip()))
    s1, pairs = findNumPairs(list1)
    print(s1)
    print(pairs)
    # s2 = findS2(list1,)


main()

