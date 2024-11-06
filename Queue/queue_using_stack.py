class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def push(self, item):
        self.stack.append(item)
    
    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def pop(self):
        if self.isEmpty():
            return "Stack is already empty"
        return self.stack.pop()
        
    
class Queue:
    def __init__(self):
        self.stack1 = Stack()    
        self.stack2 = Stack()  
        self.__size = 0
    def size(self):
        return self.__size
    
    def enqueue(self, item):
        self.stack1.push(item)
        self.__size += 1
    
    def dequeue(self):
        if self.stack2.isEmpty():
            if self.stack1.isEmpty():
                return "Queue is empty"
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        self.__size -= 1
        return self.stack2.pop()
    
    def peek(self):
        if self.stack2.isEmpty():
            if self.stack1.isEmpty():
                return "Queue is empty"
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.top()
        
    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()
    
    def get_all_items(self):
        return self.stack2.stack[::-1]+self.stack1.stack 

q = Queue()

q.enqueue("Shahid")
q.enqueue("Ruma")
q.enqueue("Ayman")

print(q.size())
print(q.dequeue())
q.enqueue("Rohan")
print(q.get_all_items())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.isEmpty())
print(q.dequeue())

print(q.peek())
print(q.isEmpty())