#https://practice.geeksforgeeks.org/problems/c-visible-numbers/0/?ref=self

def visibleNos(str1):
    dict1={key:str1.count(key) for key in set(str1)}
    print(dict1)
    len1=len(str1)
    print(len1 //3)
    for key1,val1 in dict1.items():
        if val1 > (len1 //3):
            print("key",key1)
            
visibleNos("122323232")