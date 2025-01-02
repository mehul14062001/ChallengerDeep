class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def push(self,item):
        new_node=Node(item)
        if self.is_empty():
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        self.size+=1
    def pop(self):
        if not self.is_empty():
            removed_data=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            self.size-=1
            return removed_data
    def is_empty(self):
        return self.front is None
    def size(self):
        return self.size
    def front(self):
        if not self.is_empty():
            return self.front.data