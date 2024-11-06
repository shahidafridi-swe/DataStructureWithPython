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


def infix_to_postfix(s):
    stack = Stack()
    postfix = ""
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    for char in s:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.top() != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while not stack.isEmpty() and stack.top() != '(' and precedence[stack.top()] >= precedence[char]:
                postfix += stack.pop()
            stack.push(char)
    
    while not stack.isEmpty():
        postfix += stack.pop()
    
    print(postfix)



# Example usage
exp = "a+b*(c^d-e)^(f+g*h)-i"
infix_to_postfix(exp)
