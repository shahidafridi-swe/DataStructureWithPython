class Queue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
        
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
        
class Stack:
    def __init__(self):
        self.queue = Queue()
    
    def isEmpty(self):
        return self.queue.isEmpty()
    
    def size(self):
        return self.queue.size()
        
    def push(self, item):
        self.queue.enqueue(item)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        n = self.size()
        for _ in range(n-1):
            self.queue.enqueue(self.queue.dequeue())
        return self.queue.dequeue()
    
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        n = self.size()
        for _ in range(n-1):
            self.queue.enqueue(self.queue.dequeue())
        
        top_val = self.queue.dequeue()
        self.queue.enqueue(top_val)
        return top_val
    
        
        
stack = Stack()

print(stack.isEmpty())
stack.push(2)
stack.push(4)
print(stack.isEmpty())
print(stack.top())
print(stack.pop())
print(stack.top())

