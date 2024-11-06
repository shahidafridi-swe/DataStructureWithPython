class Stack:
    def __init__(self):
        self.stack = []
        self.min_val = None
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        if self.isEmpty():
            self.min_val = item
            self.stack.append(item)
        elif item > self.min_val:
            self.stack.append(item)
        else:
            self.stack.append((2*item)-self.min_val)
            self.min_val = item
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        elif self.stack[-1] > self.min_val:
            return self.stack.pop()
        else:
            pop_val = (self.min_val*2) - self.stack[-1]
            self.min_val = (self.min_val*2) - self.stack[-1]
            self.stack.pop()
            return pop_val
            
        
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        elif self.stack[-1] > self.min_val:
            return self.stack[-1]
        else:
            return (self.min_val*2) - self.stack[-1]
            
    
    def getMin(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.min_val
    
    
st = Stack()

st.push(5)
st.push(8)
st.push(2)
st.push(10)
print("pop",st.pop())
print("pop",st.pop())


print("stack",st.stack)
print("min_val:",st.min_val)
print("top",st.top())
print("getMin:",st.getMin())