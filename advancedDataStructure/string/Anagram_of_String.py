#Anagram_of_String

def Anagram_of_String2(str1,str2):
    commonStr=""
    
    dic1={key: str1.count(key) for key in str1}
    dic2={key: str2.count(key) for key in str2}
    dic3=dict()
    for key1,value1 in dic1.items():
        print(key1)
        if dic2[key1]:
            dic3[key1] =min(dic1[key1] , dic2[key1])
            
    print(dic3)
    for key,val in dic3.items():
        for i in range(val):
            commonStr += key
        
    return commonStr

str1="aaabbc"
dict1={key : str1.count(key) for key in set(str1)}
print(dict1)
dict1['z']=11
print("dict1  :  ",dict1)
str2="aabbbccccdd"

print(Anagram_of_String2(str1,str2))


def Anagram_of_String(str1,str2):
    commonStr=""
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                commonStr += str(str1[i])
                
    return commonStr


str1="bcadeh"
dict1={key : str1.count(key) for key in set(str1)}
print(dict1)
str2="hea"

print(Anagram_of_String(str1,str2))

list1=[1,2,3,4]
list2=[2,3,4,5]

for item1,item2 in zip(list1,list2):
    print(item1+item2)
    
list3=[[3,5],
       [1,6],
       [56,87]]
list3.sort(key = lambda  y:y[0])
print(list3)
    

student={
        
        "name":"atul",
        "roll no":123,
        "height":"5ft 1 inch",
        "friends":["a","b","c","d","e"],
        "fast friends":{"p","q","r","s","t"}
        }

student["enemy"]="anand"
print(student)

student["friends"].append("srishti")
print(student)