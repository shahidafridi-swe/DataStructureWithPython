class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
        
    def insert_at_index(self, data, index):
        if index==0:
            self.insert_at_begin(data)
        elif index == self.length():
            self.insert_at_end(data)
        elif 0 < index < self.length():
            position = 0
            current_node = self.head
                
            while position+1 != index:
                current_node = current_node.next
            
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node 
        else:
            print("Invalid Index")
            
    def print(self):
        itr = self.head
        while itr:
            print(f"{itr.data} --> ",end="")
            itr = itr.next
  
    def updateNode(self, value, index):
        current_node = self.head 
        position = 0
        if index == 0:
            self.head.data = value
        
            
    


ll = LinkedList()
ll.insert_at_begin(25)
ll.insert_at_begin(36)
ll.insert_at_index(3,1)
ll.insert_at_index(11,3)

ll.print()
            
            
            
        
        