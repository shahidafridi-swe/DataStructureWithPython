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
    
    return(postfix)

def infix_to_prefix(s):
    s = s[::-1]
    s = "".join(['(' if char==')' else ')' if char=='(' else char for char in s])
    
    prefix = ""
    stack = Stack()
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    for char in s:
        if char.isalnum():
            prefix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.top() != '(':
                prefix += stack.pop()
            stack.pop()
        else:
            while not stack.isEmpty() and stack.top() != '(' and precedence[char] < precedence[stack.top()]:
                prefix += stack.pop()
            stack.push(char)
    while not stack.isEmpty():
        prefix += stack.pop()
    
    prefix = prefix[::-1]
    return prefix
    
def postfix_to_infix(s):
    stack = Stack()
    
    for char in s:
        if char.isalnum():
            stack.push(char)
        else:
            x1 = stack.pop()
            x2 = stack.pop()
            stack.push(f"({x2}{char}{x1})")
    return stack.pop()

def prefix_to_infix(s):
    stack = Stack()
    for char in reversed(s):
        if char.isalnum():
            stack.push(char)
        else:
            x1 = stack.pop()
            x2 = stack.pop()
            stack.push(f"({x1}{char}{x2})")
    return stack.pop()
    

while True:
    print("\n-------------------------------------------------\n")
    print('Hello, Which expression will you want to convert?')
    print('1 : Infix ')
    print('2 : Postfix ')
    print('3 : Prefix ')
    print('0 : Exit ')
    n = input("Type here (1/2/3/0): ")
    
    
    if n == '1':
        while True:
            print('\nFrom INFIX to which expression you want?')
            print('1 : Prefix ')
            print('2 : Postfix ')
            print('0 : Main Menu ')
            x = input("Type here (1/2/0): ")
            if x == '0':
                break
            if x != '1' and x != '2':
                print("--------Invalid Input !!! Try Again !!!--------")
                continue
            
            exp = input('Write your INFIX expression: ')
            if x == '1':
                print('Infix :', exp)
                print('Prefix :', infix_to_prefix(exp))
                break
            elif x == '2':
                print('Infix :', exp)
                print('Postfix :', infix_to_postfix(exp))
                break
                
                
    elif n == '2':
        while True:
            print('\nFrom POSTFIX to which expression you want?')
            print('1 : Infix ')
            print('2 : Prefix ')
            print('0 : Main Menu ')
            x = input("Type here (1/2/0): ")
            if x == '0':
                break
            if x != '1' and x != '2':
                print("--------Invalid Input !!! Try Again !!!--------")
                continue
            
            exp = input('Write your POSTFIX expression: ')
            if x == '1':
                print('Postfix :', exp)
                print('Infix :', postfix_to_infix(exp))
                break
            elif x == '2':
                print('Postfix :', exp)
                print('Prefix :', infix_to_prefix(postfix_to_infix(exp)))
                break
                
                
    elif n == '3':
        while True:
            print('\nFrom PREFIX to which expression you want?')
            print('1 : Infix ')
            print('2 : Postfix ')
            print('0 : Main Menu ')
            x = input("Type here (1/2/0): ")
            if x == '0':
                break
            if x != '1' and x != '2':
                print("--------Invalid Input !!! Try Again !!!--------")
                continue
            
            exp = input('Write your PREFIX expression: ')
            if x == '1':
                print('Prefix :', exp)
                print('Infix :', prefix_to_infix(exp))
                break
            elif x == '2':
                print('Prefix :', exp)
                print('Postfix :', infix_to_postfix(prefix_to_infix(exp)))
                break
    
    elif n == '0':
        print("\n-------THANK YOU, SEE YOU AGAIN-------")
        break

    else:
        print("--------Invalid Input !!! Try Again !!!--------")
                
      

   
