# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:14:29 2018

@author: atul
"""

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
            
    def recursive(self,root):
        if (root.next is None) or (root is None):
            return root;

        temp = root.next
        head = self.recursive(temp)
            
        temp.next = root
        root.next = None
        #self.root=temp
        return head
    
    def reverse(self):
        temp=self.root
        p=self.root
        q=p.next
        r=q.next
        temp.next=None
        while 1:
            temp=q
            temp.next=p
            p=temp
            #p=temp.next
            q=r            
            if r.next:
                r=r.next
            print(temp.data,p.data,q.data,r.data)
            if temp==p==q:
                break
        print("outside")
        self.root=r
        
    def disp(self):
        temp =self.root
        while temp:
            print(temp.data)
            temp=temp.next
            
    def dispR(self,temp):
        while temp:
            print(temp.data)
            temp=temp.next


linkedList =  SinglyLinkedList()

for i in range(11):
     linkedList.createLList(i)

linkedList.disp()          
linkedList.dispR(linkedList.root)

print("reversed")  
#linkedList.disp(LinkedList.root)      
lastElement=linkedList.recursive(linkedList.root)
linkedList.dispR(lastElement)

linkedList.dispR(linkedList.root)
linkedList.disp()  