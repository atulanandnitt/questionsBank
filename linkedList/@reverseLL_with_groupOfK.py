# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:58:12 2018

@author: Atul Anand
"""

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        
class LL:

    def __init__(self):
        self.head=None

    def createLL(self,val):
        if self.head :
            temp=self.head
            
            while temp.next:
                temp=temp.next
            temp.next=Node(val)
        else:
            self.head=Node(val)
            
    def rev(self):
        p=self.head
        q=self.head.next
        r= self.head.next.next
        p.next=None
        
        while q.next != None:
            q.next = p
            p=q
            q=r
            if q.next:
                r=q.next
                
        q.next=p
        self.head=q
        
    def revWithK(self,k):
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
        
    def disp(self):
        print(self.head.data)
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

            
ll=LL()
for item in range(11):
    ll.createLL(item)       

ll.disp()     
ll.rev()
ll.disp()

print("reverse with group of k")
k=3
ll.revWithK(k)
ll.disp()