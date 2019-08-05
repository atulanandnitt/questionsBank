# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 08:08:50 2018

@author: atul
"""

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None


class Tree:
    def __init__(self):
        self.root=None
    
    def createTree(self,val):
        if self.root :
            temp=self.root
            
            while 1:
                    
                if val<temp.data:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=Node(val)
                        break
                elif temp.data<val:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=Node(val)
                        break
        else:
            self.root=Node(val)
    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
    
    def breathFirstTravel(self):
        self.root.level=0
        tempList=[self.root]
        tempLevel=self.root.level
        result=[]
        
        while len(tempList)>0:
            
            temp=tempList.pop(0)
            

            if temp.level > tempLevel:
                tempLevel +=1
                result.append('\n')
            
            result.append(temp.data)
            
            if temp.left:
                temp.left.level=tempLevel+1
                tempList.append(temp.left)
                
            if temp.right:
                temp.right.level=tempLevel+1
                tempList.append(temp.right)
        
        print("complete level order Traversal")
        print(result)
        
            
          
    
    
    def rightViewOfTree(self):
        self.root.level=0
        tempList=[self.root]
        tempLevel=self.root.level
        rightView=[]
        result=[]
        
        while len(tempList)>0:
            
            temp=tempList.pop(0)
            

            if temp.level > tempLevel:
                tempLevel +=1
                result.append('\n')
            
            result.append(temp.data)
            
            if temp.left:
                temp.left.level=tempLevel+1
                tempList.append(temp.left)
                
            if temp.right:
                temp.right.level=tempLevel+1
                tempList.append(temp.right)
        
        prev = None
        for item in result:
            if prev is None:
                prev=item
                
            if item =='\n':
                rightView.append(prev)
            
            prev=item
            #print("prev item is",prev)
        
        print(rightView)
            
          
    
    
    
    def leftViewOfTree(self):
        self.root.level=0
        temp_level=self.root.level        
        tempList=[self.root]
        leftViewList=[]
        leftViewList.append(self.root.data)
        while len(tempList) >0:
            #print("tempList",tempList,"")
            temp=tempList.pop(0)
            
            if temp.level > temp_level:
                temp_level +=1
                leftViewList.append(temp.data)
            
            if temp.left:
                temp.left.level=temp_level +1
                tempList.append(temp.left)
                
            if temp.right:
                temp.right.level= temp_level +1
                tempList.append(temp.right)
                
        print(leftViewList)
    

    def topView(self):
        self.root.level=0
        self.root.leftFlag=0
        self.root.rightFlag=0
        tempLevel=self.root.level
        result=[]
        topviewList=[]
        tempList=[self.root]
        
        while len(tempList) >0:
            
            temp =tempList.pop(0)
            
            if tempLevel < temp.level:
                tempLevel +=1
                result.append('\n')
            
            result.append(temp)
            
            if temp.left:
                temp.left.level=tempLevel+1
                tempList.append(temp.left)
                temp.left.leftFlag=1
            
            if temp.right:
                temp.right.level=tempLevel+1
                tempList.append(temp.right)        
                temp.right.rightFlag=1
        
        for item in result:
            if (item.leftFlag ==1 and item.rightFlag == 0) or (item.leftFlag ==0 and item.rightFlag ==1):
                topviewList.append(item)
        
        print(topviewList)
        
    
    def trimbst(self,tree,minVal,maxVal): 
    #O(n) as we are basically performing post order Traversal of the tree
        
        if not tree:
            return
        
        tree.left = self.trimbst(tree.left,minVal,maxVal)
        tree.right = self.trimbst(tree.right,minVal,maxVal)
        
        if minVal <=tree.val <= maxVal:
            return tree
        
        if tree.val < minVal:
            return tree.right
        
        if tree.val > maxVal:
            return tree.left
        
        
        
    def isLeftChild(self):
        return self.parent and self.parent.leftChild ==self
    
    def isrightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isroot(self):
        return not self.parent
    
    def isLeaf(self):
        return self
        
    def removeNode(self,temp):
        
        if temp.isLeaf(): #Leaf
            if temp.parent.leftChild == None:
                temp.parent.leftChild =None
            else:
                temp.parent.rightChild =None
        elif temp.hasBothChildren():#interior
            
            succ=temp.findSuccessor()
            succ.spliceOut()
            temp.key = succ.key
            temp.payload = succ.payload
        
        else: #node eonly have 1 child
            if temp.left:
                if temp.isleftChild():
                    temp.leftChild.parent=temp.parent
                    temp.parent.leftChild=temp.leftChild
                elif temp.isrightChild():
                    temp.rightChild.parent = temp.parent
                    temp.parent.rightChild=temp.rightChild
                else:
                    temp.replaceNodeData(temp.leftChild.key,
                                         temp.leftChild.payload,
                                         temp.leftChild.leftChild,
                                         temp.leftChild.rightChild)
            else:
                if temp.isleftChild():
                    temp.rightChild.parent = temp.parent
                    temp.parent.leftChild = temp.rightChild
                elif temp.isrightChild():
                    temp.rightChild.parent = temp.parent
                    temp.parent.rightChild = temp.rightChild
                else:
                    temp.replaceNodeData(temp)
                
                    
        
        
            
bst=Tree()
items = [8,3,1,6,4,7,10,14,13,12,11,15,16,17,18,2,5,9]
for item in items:
    bst.createTree(item)            

bst.inorder(bst.root)

print("levelOrderTraversal :  ")
bst.breathFirstTravel()


print("bst.leftViewOfTree() : ")
bst.leftViewOfTree()
print("bst.rightViewOfTree() : ")
bst.rightViewOfTree()

print("bst.topView() : HAS SOME ISSUE   ?????")
#bst.topView()


print("bst.removeNode() : HAS SOME ISSUE   ?????")
#bst.removeNode()

