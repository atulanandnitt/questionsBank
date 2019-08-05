# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:00:26 2018

@author: atul
"""

#cycle chk
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
    
    def createCycle(self):
        temp=self.head
        i=0
        while i <5:
            temp=temp.next
            i +=1
        temp.next=self.head
    
    def disp(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
        
singleLL= SingleLL()    

for i in range(11):
    singleLL.createLL(i)            

singleLL.disp()
    
print(singleLL.isCyclic())

singleLL.createCycle()

print(singleLL.isCyclic())
