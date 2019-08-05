import os
path="D:/CRM/generic/home/rahul/python_language/objective_doubts/basicDataStructure/fileHandling/alphabets/allFiles/"

for i in range(26):
    with open(path+chr(ord('a') +i)+".txt" ,"w") as f1:
        f1.write(chr(ord('a') +i))
data=""
content=""
for parentFolder,subFolder,fileList in os.walk(path):
    print("fileList",fileList)
    for file1 in fileList:
        with open(file1,"r") as f1:
            #data += "data : "+f1.read()+" " 
            #f1.close()
            content += f1.read()
            print("content",content)
            #data += f1.read()
    print("data",data)
    print("content",content)
for item in os.walk(path):
    print(item)
    
list1=[[1,2],[3,4],[5,6]]
for item in list1:
    print(item)
        
for item1,item2 in list1:
    print(item1,item2)    