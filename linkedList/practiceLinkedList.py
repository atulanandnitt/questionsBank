#linkedList
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
    
    def createLL(self,val):
        if self.head is None:
            self.head=Node(val)
        else:
            temp=self.head
            
            while temp.next:
                temp=temp.next
            
            temp.next=Node(val)
    
    def disp(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    
    def rev(self):
        p=self.head
        q=p.next
        r=q.next
        p.next=None
        
        while 1:
            q.next=p
            p=q
            q=r
            if r.next:
                r=r.next
            if q.next ==None:
                q.next=p
                self.head=q
                break
            
    def insert(self,key,val):
        temp1=self.head
        while temp1:
            #print("temp1.data",temp1.data)
            if temp1.data == key:
                temp2=temp1.next
                temp1.next=Node(val)
                temp1.next.next=temp2
                #print(val, "inserted ")
                break
            temp1=temp1.next
            print("searching for correct val")

    def insertAtPosition(self,pos,val):
        temp1=self.head
        for i in range(pos-1):
            temp1=temp1.next
            
        temp2=temp1.next
        temp1.next=Node(val)
        temp1.next.next=temp2
        print(val, "inserted ")
       
ll=LinkedList()
for item in range(11):
    ll.createLL(item)

ll.disp()
print("reversing the linked list:")
ll.rev()
ll.disp()   

print("inserting 555 after node having val of 5")
ll.insert(5,555)
ll.disp()


ll.insertAtPosition(6,666)
ll.disp()

print(ord('A'))