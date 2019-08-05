
#linkedList
class Node:
    def __init__(self,val):
        self.data=val
        self.next=0
    
class LinkedList:
        
    def __init__(self):
        self.head=None
        
    def XOR(self,a,b):
        
        c = int(a)^int(b)
        print("val of c is :",c)
        return map(Node,c)
    
    def insert(self,val):
        
        tmp = Node(val)
 
        tmp.next = self.XOR(self.head, None)
        
        
        if self.head is not None:
            nextTmp = self.XOR(self.head, None)
            self.head.next = self.XOR(tmp,nextTmp)
            
        self.head = tmp
            

    def disp(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

ll=LinkedList()
for item in range(11):
    ll.insert(item)
    
ll.disp()