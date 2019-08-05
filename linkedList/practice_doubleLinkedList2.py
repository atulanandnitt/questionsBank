# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:14:50 2018

@author: atul
"""

#practice doubly linked list

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None
        
class DoublyLL:
    def __init__(self):
           self.head=None
           self.tail=None
    
    def createDoublyLL(self,val):
        
        if self.head:
                
            temp=self.head
            
            while temp.next:
                temp=temp.next
            
            temp.next=Node(val)
            
            temp.next.prev=temp
        else:
            self.head=Node(val)
            #self.tail=self.head
        
        temp2 =self.head
        while temp2.next:
            temp2=temp2.next
        self.tail=temp2
        
    def dispForward(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    
    def dispBackward(self):
        temp=self.tail
        while temp:
            print(temp.data)
            temp=temp.prev
            
doublyLL = DoublyLL()

for i in range(11):
    doublyLL.createDoublyLL(i)
doublyLL.dispForward()

print("iterate backward")
doublyLL.dispBackward()