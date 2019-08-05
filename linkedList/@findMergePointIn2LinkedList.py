# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:52:33 2018

@author: Atul Anand
"""

class Node:
    
    def __init__(self,val):
        self.data = val
        self.next= None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def addNode(self,val):
        if self.head == None:
            self.head = Node(val)
        else:
            temp= self.head
            
            while temp.next:
                temp = temp.next
            
            temp.next=Node(val)
            
    def rev(self,temp):
        p,q,r=temp,temp.next,temp.next.next
        p.next=None
        while temp:
            print(p.data, "from while loop")
            q.next= p
            p=q
            q=r
            if r.next == None:
                q.next= p
                p=q
                q=r
                self.head=p
                break
            else:
                r=r.next
            
            
    def disp(self,temp):
        while temp:
            print(temp.data)
            temp= temp.next
            
            
ll=LinkedList()            

for item in range(11):
    ll.addNode(item)            
    
ll.disp(ll.head)    
ll.rev(ll.head)
ll.disp(ll.head)
        