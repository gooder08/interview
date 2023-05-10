class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items[-1]
    def size(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return len(self.items)
