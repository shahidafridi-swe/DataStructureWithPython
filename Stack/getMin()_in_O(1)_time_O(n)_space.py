class Stack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        if self.isEmpty() or self.minStack[-1] >= item:
            self.minStack.append(item)
        self.stack.append(item)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        if self.top() == self.minStack[-1]:
            self.minStack.pop()
        return self.stack.pop()
        
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[-1]
    
    def getMin(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.minStack[-1]
    
    
st = Stack()

st.push(5)
st.push(8)
st.push(2)
st.push(10)
st.pop()
st.pop()
st.pop()
st.pop()

print(st.stack)
print(st.minStack)
print(st.top())
print(st.getMin())