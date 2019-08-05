
#cycle chk

"""
To DO
1: find merge point of 2 linked list
2: revWithGroupOfK
3: add
4: remove the cycle

"""

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
 
class SingleLL:
    def __init__(self):
        self.head=None
    
    def createLL(self,val):
        if self.head==None:
            self.head = Node(val)
        else:
            temp=self.head
            
            while temp.next:
                temp=temp.next
            
            temp.next=Node(val)
    #WHY NOT WORKING ?????            
    def revWithGroupOfK(self,k):
        p=self.head
        q=self.head.next
        for i in range(k):
            q=q.next
        r= self.head.next.next
        for i in range(k):
            r=r.next
        p.next=None
        
        while q.next != None:
            q.next = p
            p=q
            q=r
            if q.next:
                r=q.next
                
        q.next=p
        self.head=q
        
        
    def isCyclic(self):
        temp1=self.head.next
        temp2=self.head.next.next
        
        while temp2.next:
            if temp1 ==temp2:
                return True
            else:
                temp1=temp1.next
                temp2=temp2.next.next
        
        return False
        
        
    #Your task is to complete this function
    #Functioon should return 1/0 only
    def detectLoop(self):
        ptr = self.head
        dptr = self.head
        
        while ptr and dptr and dptr.next:
            ptr = ptr.next
            dptr = dptr.next.next
            if ptr == dptr:
                print("loop detected")
                return ptr
            
        return False
    
    def removeTheLoop(self):
        loopPtr = self.detectLoop()
        
        
        if not loopPtr:
            return 1
            
        ptr = self.head
        while ptr:
            if ptr.next == loopPtr:
                ptr.next = loopPtr.next
                return 1
            ptr = ptr.next
        
        
        
    def createCycle(self):
        temp=self.head
        while temp.next:
            temp=temp.next
         
        print("temp : ", temp, temp.data)
        #temp.next=self.head
    

    def ReverseRecursive(self,temp1):#with comments
        if (temp1.next is None):# or (head is None):
            return temp1;
        
        temp2 = temp1.next
        print("temp1 : ",temp1.data,"temp2 :",temp2.data)
        head = self.ReverseRecursive(temp2)
        print("temp1 : ",temp1.data,"temp2 :",temp2.data, "head :",head.data)
        print("head :",head.data)
        temp2.next = temp1
        print("temp2 :",temp2.data)
        temp1.next = None
        #self.head=temp
        return head

    def reverse(self):
        temp =self.head
        q=self.head.next
        r=self.head.next.next
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
            

            
    def disp(self):
        temp =self.head
        
        while temp:
            print(temp.data)
            temp=temp.next
            
    def dispAsAList(self):
        list1=list()
        temp =self.head
        
        while temp:
            list1.append(temp.data)
            temp=temp.next
        print("list :", list1)
            
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
        
    #not working ????    
    def add(self,linkedlist1,linkedlist2,lengthOfBoth):
        linkedlist1.disp()
        linkedlist1.reverse()
        print("after reverse") 
        linkedlist1.disp()
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
        
        
        for i in range(1,lengthOfBoth):
            temp3=(temp1.data+temp2.data +reminder)%10
            reminder= int((temp1.data+temp2.data+reminder)/10)
            temp1=temp1.next
            temp2=temp2.next
            self.createLL(temp3)
        linkedlist3.disp()
        linkedlist3.reverse()
        print("after reverse,actual sum of linkedlist 1 and linkedlist2") 
        linkedlist3.disp()
            
            
        
        
        
        

        
singleLL= SingleLL()    

for i in range(11):
    singleLL.createLL(i)            

singleLL.disp()
    
print("singleLL.isCyclic() : ", singleLL.isCyclic())


singleLL.createCycle()

"""

print("singleLL.isCyclic() : ", singleLL.isCyclic())
singleLL.removeTheLoop()
singleLL.disp()
    
print("singleLL.isCyclic() : ", singleLL.isCyclic())
#singleLL.removeCycle()
"""




print("reverse with group of k")
k=3
singleLL.revWithGroupOfK(k)
singleLL.disp()

print("reverse LL recursive")
singleLL.head=singleLL.ReverseRecursive(singleLL.head)
singleLL.disp()


linkedlist1 =SingleLL()
linkedlist2 =SingleLL()
linkedlist3 =SingleLL()
lengthOfBoth=5
for i in range(lengthOfBoth):
    linkedlist1.createLL(i)
for i in range(lengthOfBoth):
    linkedlist2.createLL(i)
linkedlist1.dispAsAList()
linkedlist2.dispAsAList()    
    
linkedlist3.add(linkedlist1,linkedlist2,lengthOfBoth)
linkedlist3.dispAsAList()