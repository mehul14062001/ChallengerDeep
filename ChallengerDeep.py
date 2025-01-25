############
## BITSET ##
############
# Bitset is an array whose each value is either 0 or 1
# Bitset require less memory than ordinary arrays because each element in a bitset only uses one bit of memory
# N elements in a Bitset would require N bits of memory
# The values of a Bitset can be efficiently manipulated using bit operators making it possible to optimize algorithms using bit sets

class Bitset(object):
    def __init__(self,n,s=None):
        self.n=n
        self.b=[0 for _ in range(self.n)]
        if s:
            for i in range(self.n-1,-1,-1):
                if s[i] in '01':
                    self.b[self.n-i-1]=int(s[i])
    def count(self):
        return sum(self.b)
    def __and__(self,other):
        if self.n!=other.n:
            raise ValueError("Bitsets must have the same size for AND operation")
        result=Bitset(self.n)
        result.b=[self.b[i]&other.b[i] for i in range(self.n)]
        return result
    def __or__(self,other):
        if self.n!=other.n:
            raise ValueError("Bitsets must have the same size for OR operation")
        result=Bitset(self.n)
        result.b=[self.b[i]|other.b[i] for i in range(self.n)]
        return result
    def __xor__(self,other):
        if self.n!=other.n:
            raise ValueError("Bitsets must have the same size for XOR operation")
        result=Bitset(self.n)
        result.b=[self.b[i]^other.b[i] for i in range(self.n)]
        return result
    def __lshift__(self,shift):
        result=Bitset(self.n)
        if shift<self.n:
            result.b=self.b[shift:]+[0]*shift
        return result
    def __rshift__(self,shift):
        result=Bitset(self.n)
        if shift<self.n:
            result.b=[0]*shift+self.b[:self.n-shift]
        return result
    def __invert__(self):
        result=Bitset(self.n)
        result.b=[1-bit for bit in self.b]
        return result
    def __str__(self):
        return ''.join(map(str,self.b))
    def __eq__(self,other):
        return self.b==other.b
    

###########
## DEQUE ##
###########
# Deque is a dynamic array whose size can be efficiently changed at both ends of the array
# The internal implementation of a Deque is more complex than that of a Vector so a Deque is slower than a Vector
# Both adding and removing elements take O(1) time on average at both ends

class DequeNode:
    """A node in the doubly linked list."""
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class Deque:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def is_empty(self):
        return self.size==0
    def add_front(self,item):
        new_node=DequeNode(item)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.size+=1
    def add_rear(self,item):
        new_node=DequeNode(item)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1
    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove_front from empty deque")
        value=self.head.value
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        else:
            self.tail=None
        self.size-=1
        return value
    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")
        value=self.tail.value
        self.tail=self.tail.prev
        if self.tail:
            self.tail.next=None
        else:
            self.head=None
        self.size-=1
        return value
    def peek_front(self):
        if self.is_empty():
            raise IndexError("peek_front from empty deque")
        return self.head.value
    def peek_rear(self):
        if self.is_empty():
            raise IndexError("peek_rear from empty deque")
        return self.tail.value
    def __len__(self):
        return self.size
    def __str__(self):
        values=[]
        current=self.head
        while current:
            values.append(current.value)
            current=current.next
        return "Deque:"+"<->".join(map(str,values))


###########
## STACK ##
###########
# Stack is a data structure that provides two O(1) time operations: adding an element to the top and removing an element from the top
# It is only possible to access the top element of a Stack

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def __len__(self):
        return len(self.stack)
    def __str__(self):
        return "Stack:"+str(self.stack)


###########
## QUEUE ##
###########
# A Queue provides two O(1) time operations: adding an element to the end of the Queue and removing the first element in the Queue
# It is only possible to access the first element of a Queue

class QueueNode:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def is_empty(self):
        return self.size==0
    def enqueue(self,item):
        new_node=QueueNode(item)
        if self.is_empty():
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        self.size+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value=self.front.value
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        self.size-=1
        return value
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.value
    def __len__(self):
        return self.size
    def __str__(self):
        values=[]
        current=self.front
        while current:
            values.append(current.value)
            current=current.next
        return "Queue:"+"->".join(map(str,values))


####################
## PRIORITY QUEUE ##
####################
# A Priority Queue maintains a set of elements
# The supported operations are insertion and (depending on the type of the Queue) retrieval and removal of either the minimum or maximum element 
# Insertion and removal take O(logn) time and retrieval takes O(1) time
# Priority Queue is usually implemented using a Heap structure that is much simpler than a Balanced Binary Tree used in an Ordered Set

class PriorityQueue:
    def __init__(self):
        self.heap=[]
    def enqueue(self,item):
        self.heap.append(item)
        self._heapify_up(len(self.heap)-1)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty priority queue")
        self._swap(0,len(self.heap)-1)
        min_item=self.heap.pop()
        self._heapify_down(0)
        return min_item
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty priority queue")
        return self.heap[0]
    def is_empty(self):
        return len(self.heap)==0
    def _heapify_up(self,index):
        while index>0:
            parent_index=(index-1)//2
            if self.heap[index]<self.heap[parent_index]:
                self._swap(index,parent_index)
                index=parent_index
            else:
                break
    def _heapify_down(self,index):
        child_index=2*index+1
        while child_index<len(self.heap):
            right_child_index=child_index+1
            smallest_child_index=child_index
            if right_child_index<len(self.heap) and self.heap[right_child_index]<self.heap[child_index]:
                smallest_child_index=right_child_index
            if self.heap[index]<=self.heap[smallest_child_index]:
                break
            self._swap(index,smallest_child_index)
            index=smallest_child_index
            child_index=2*index+1
    def _swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    def __str__(self):
        return "Priority Queue (Min-Heap):"+str(self.heap)
