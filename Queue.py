class Queue:
    def __init__(self):
        self.items = []

    def top(self):
        if not self.is_empty():
            return self.items[0]

        else:
            raise Exception("Queue is empty")
        
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise Exception("Queue is empty")

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Top item:",queue.top())

queue.dequeue()

print("Current size:", queue.size())
print("Top item:",queue.top())
queue.dequeue()
queue.dequeue()

print("Is stack empty?", queue.is_empty())


