class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            poped_item = self.items.pop()
            return poped_item
        else:
            raise Exception("Stack is empty")
            
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top item:",stack.top())

stack.pop()

print("Current size:", stack.size())

stack.pop()
stack.pop()

print("Is stack empty?", stack.is_empty())


