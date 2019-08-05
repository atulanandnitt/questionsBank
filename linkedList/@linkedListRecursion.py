

#Singly linked list

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.root=None
    
    def createLList(self,val):
        if self.root ==None:
            self.root=Node(val)
        else:
            temp=self.root
            
            while temp.next:
                temp=temp.next
            
            temp.next=Node(val)
            
    def recursive2(self,root):#without comments
        if (root.next is None):# or (root is None):
            return root;
        
        temp = root.next
        head = self.recursive(temp)
        temp.next = root
        root.next = None
        
        return head

    def recursive3(self,temp1):#without comments
        if (temp1.next is None):# or (root is None):
            return temp1;
        
        temp2 = temp1.next
        head = self.recursive(temp2)
        temp2.next = temp1
        temp1.next = None
        return head
    
    def recR(self,temp1):
        if temp1.next == None:
            return temp1
        
        temp2=temp1.next
        head = self.recR(temp2)
        
        temp2.next=temp1
        temp1.next=None
        
        return head
    
    
    def recursive(self,temp1):#with comments
        if (temp1.next is None):# or (root is None):
            return temp1;
        
        temp2 = temp1.next
        print("temp1 : ",temp1.data,"temp2 :",temp2.data)
        head = self.recursive(temp2)
        print("temp1 : ",temp1.data,"temp2 :",temp2.data, "head :",head.data)
        print("head :",head.data)
        temp2.next = temp1
        print("temp2 :",temp2.data)
        temp1.next = None
        #self.root=temp
        return head
                      

    def dispR(self,temp):
        while temp:  
            print(temp.data)
            temp=temp.next

    def disp(self):#just to show the diff
        temp =self.root
        while temp:
            print(temp.data)
            temp=temp.next
            
linkedList =  SinglyLinkedList()

for i in range(4):
     linkedList.createLList(i)

linkedList.disp()          
linkedList.dispR(linkedList.root)

print("reversed")  
#linkedList.disp(LinkedList.root)      
lastElement=linkedList.recursive(linkedList.root)
linkedList.dispR(lastElement)


#linkedList.dispR(linkedList.root)
#linkedList.disp()  