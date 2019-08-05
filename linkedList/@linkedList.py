#linkelist

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        
    def create(self,val):
        if self.head == None:
            self.head =Node(val)
        
        else:
            temp = self.head
            
            while 1:
                if temp.next :
                    temp =temp.next
                else:
                    temp.next=Node(val)
                    break
            
            
    """    
    def disp(self):
        temp =self.head
        while 1:
            if temp:
                print(temp.data)
                temp=temp.next
            else:
                break
    """
    def reverse(self):
        temp =self.head
        q=temp.next
        r=q.next
        temp.next=None
        while temp:
            
            q.next=temp
            temp=q
            q=r
            
            if r.next:
                #print("r",r)
                r=r.next
            
            if q.next == None:
                #print("q",q)
                #q.next=temp
                q.next=temp
                self.head=r
                break
            
    def recR(self,temp1):
        if temp1.next == None:
            return temp1
        
        temp2=temp1.next
        head = self.recR(temp2)
        temp1.next=None        
        temp2.next=temp1

        
        return head
    
    def dispR(self,temp):
        #temp =self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
    def disp(self):
        temp =self.head
        while temp:
            print(temp.data)
            temp=temp.next
        
    def insert(self,pos,val):
        temp = self.head
        
        for i in range(pos):
            temp=temp.next
        
        q=temp.next

        temp.next=Node(val)        
        temp.next.next=q
    
    def deleted(self,pos):
        temp = self.head
        
        for i in range(pos-1):
            temp=temp.next
        
        temp.next =temp.next.next
        
        
    def add(self,linkedlist1,linkedlist2):
        linkedlist1.disp()
        linkedlist1.reverse()
        #print("after reverse") 
        #linkedlist1.disp()
        
        linkedlist2.disp()
        linkedlist2.reverse()
        print("after reverse") 
        linkedlist2.disp()
        
        temp1=linkedlist1.head
        temp2=linkedlist2.head
        temp3=0
        reminder =0
        
        
        for i in range(1,11):
            temp3=(temp1.data+temp2.data +reminder)%10
            reminder= int((temp1.data+temp2.data+reminder)/10)
            temp1=temp1.next
            temp2=temp2.next
            self.create(temp3)
        linkedlist3.disp()
        linkedlist3.reverse()
        print("after reverse,actual sum of linkedlist 1 and linkedlist2") 
        linkedlist3.disp()
            
            
        
        
        
        
linkedlist1 =LinkedList()
linkedlist2 =LinkedList()
linkedlist3 =LinkedList()
  

for i in range(1,10):
    linkedlist2.create(i)
print("list2")    
linkedlist2.disp()    


linkedlist2.reverse()
print("List2 reversed")
linkedlist2.disp()


lastElement=linkedlist2.recR(linkedlist2.head)
print("List2 reversed again by recR: ")
linkedlist2.dispR(lastElement)


"""

arr = [8,3,1,6,4,7,10,14,13,200]
for i in arr:
    linkedlist1.create(i)
linkedlist1.disp()  
linkedlist2.insert(5,5555)
print("linkedlist2 after inserted new element : ")
linkedlist2.disp()


linkedlist2.deleted(5)
print("linkedlist2 after deleting an element : ")
linkedlist2.disp()


#linkedlist1.disp()
#linkedlist2.disp()
#linkedlist3.disp()

#linkedlist3=
linkedlist3.add(linkedlist1,linkedlist2)
#linkedlist3.disp()


print("after reverse")            
linkedlist1.reverse()    
linkedlist1.disp()
"""