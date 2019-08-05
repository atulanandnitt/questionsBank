from itertools import combinations

def findTripletsSumToZero(list1):
    for item in combinations(list1,3):
        if sum(item) ==0:
            print("sum to 0")
        else:
            print(item)
        

list1=[2,3,4,5,1,2,4,-4,-3,-1]        
findTripletsSumToZero(list1)        