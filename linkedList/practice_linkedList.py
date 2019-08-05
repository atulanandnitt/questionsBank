# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:32:02 2018

@author: atul
"""

#linkelist

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.root = None
        
    def create(self,val):
        if self.root == None:
            self.root =Node(val)
        
        else:
            temp = self.root
            
            while 1:
                if temp.next :
                    temp =temp.next
                else:
                    break
            
            temp.next=Node(val)
    """    
    def disp(self):
        temp =self.root
        while 1:
            if temp:
                print(temp.data)
                temp=temp.next
            else:
                break
    """
    def reverse(self):
        temp =self.root
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
                self.root=q
                break
            

        
    def disp(self):
        temp =self.root
        while temp:
            print(temp.data)
            temp=temp.next
        

linkedlist =LinkedList()

arr = [8,3,1,6,4,7,10,14,13,200]
for i in arr:
    linkedlist.create(i)

linkedlist.disp()

print("after reverse")            
linkedlist.reverse()    

linkedlist.disp()