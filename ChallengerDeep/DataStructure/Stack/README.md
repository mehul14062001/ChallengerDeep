
# Stack Class Implementation in Python

The `Stack` class implements a basic stack data structure. A stack is a collection of elements that follows the **Last In, First Out (LIFO)** principle. This means the last element added is the first one to be removed.

## Class Definition and Explanation

```python
class Stack:
```
- **Line 1**: This defines the `Stack` class. A stack object will be created from this class.

### Constructor: `__init__(self)`
```python
    def __init__(self):
        self.items = []
```
- **Line 2-3**: This is the constructor method `__init__` that initializes the stack object. When an object of `Stack` is created, an empty list `self.items` is initialized to hold the elements of the stack.

### Push Method: `push(self, item)`
```python
    def push(self, item):
        self.items.append(item)
```
- **Line 4-5**: The `push` method is used to add an element (`item`) to the stack. It appends the item to the `self.items` list, which simulates adding an element to the top of the stack.

### Pop Method: `pop(self)`
```python
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
```
- **Line 6-8**: The `pop` method removes and returns the top element of the stack. It first checks if the stack is not empty (using the `is_empty` method), and if it’s not, it removes and returns the last element using `pop()`. If the stack is empty, it doesn't remove anything.

### Peek Method: `peek(self)`
```python
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
```
- **Line 9-11**: The `peek` method returns the top element of the stack without removing it. It checks if the stack is not empty before returning the last item in the list (`self.items[-1]`).

### Is Empty Method: `is_empty(self)`
```python
    def is_empty(self):
        return len(self.items) == 0
```
- **Line 12-13**: The `is_empty` method checks if the stack is empty by verifying if the length of `self.items` is zero. It returns `True` if the stack is empty, otherwise `False`.

### Size Method: `size(self)`
```python
    def size(self):
        return len(self.items)
```
- **Line 14-15**: The `size` method returns the number of elements currently in the stack by returning the length of `self.items`.

## Example Usage

Here's how you can use the `Stack` class in a Python program:

```python
# Create a Stack object
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Peek the top element
print("Top element:", stack.peek())  # Output: 30

# Pop an element
print("Popped element:", stack.pop())  # Output: 30

# Check if the stack is empty
print("Is the stack empty?", stack.is_empty())  # Output: False

# Get the size of the stack
print("Stack size:", stack.size())  # Output: 2

# Pop the remaining elements
print("Popped element:", stack.pop())  # Output: 20
print("Popped element:", stack.pop())  # Output: 10

# Check if the stack is empty after popping all elements
print("Is the stack empty?", stack.is_empty())  # Output: True
```

## Explanation of the Example

- We first create a `Stack` object.
- We push three elements onto the stack (`10`, `20`, and `30`).
- We then peek at the top element, which will be `30`.
- After popping the top element, `30` is removed and returned.
- We check if the stack is empty after popping an element, and it is still not empty (`False`).
- We check the size of the stack, which returns `2`.
- Finally, we pop the remaining elements (`20` and `10`), and the stack becomes empty, confirmed by the `is_empty` method returning `True`.
