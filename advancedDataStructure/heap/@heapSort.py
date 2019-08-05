#heapSort

from heapq import heappop,heappush,heapify

items=[5,4,6,3,7,2,8,1,9]
heapList=[]
heapList2=[]

for item in items:
    heappush(heapList,item)
    
#while heapList:
#    print(heappop(heapList))


print("len(heapList)",len(heapList))
for _ in range(len(items)):
    print(heappop(heapList))

    
heapify(items)
print(items)

print("heapList type",type(heapList))

print(len(heapList))