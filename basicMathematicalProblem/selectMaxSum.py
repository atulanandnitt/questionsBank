def selectEvens(list1):
    if len(list1) % 2 == 1:
        solList.append(list1.pop())


def selectMaxSum(list1):
    sumAtEven = sum(list1[::2])
    sumAtOdd = sum(list1[1::2])
    #print(sumAtEven , sumAtOdd,sum(list1))
    if sumAtEven > sumAtOdd:
        print(selectEvens(list1))
    
    
list1=[18,20,15,30,10,14]   
print(selectMaxSum(list1)) 