# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 00:37:39 2018

@author: Atul Anand
"""

# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):#maxHeap
    indexOfLargest = i # Initialize indexOfLargest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        indexOfLargest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[indexOfLargest] < arr[r]:
        indexOfLargest = r
 
    # Change root, if needed
    if indexOfLargest != i:
        arr[i],arr[indexOfLargest] = arr[indexOfLargest],arr[i] # swap
 
        # Heapify the root.
        heapify(arr, n, indexOfLargest)
 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
        print("after heapify arr :", arr)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
        print("****arr :",arr)

     
 
# Driver code to test above
arr = [ 5,300,1,2,4]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
# This code is contributed by Mohit Kumra
