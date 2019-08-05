# YouTube Video: https://www.youtube.com/watch?v=SQHvcLvqq_Q    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.root = None

    def append(self, data):
        if self.root is None:
            new_node = Node(data)
            new_node.prev = None
            self.root = new_node
        else:
            new_node = Node(data)
            temp = self.root
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None


    def print_list(self):
        temp = self.root
        while temp:
            print(temp.data)
            temp = temp.next



    def reverse(self):
        tmp = None
        temp = self.root
        while temp:
            tmp = temp.prev
            temp.prev = temp.next
            temp.next = tmp
            temp = temp.prev
        if tmp:
            self.root = tmp.prev


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()


dllist.reverse()
dllist.print_list()