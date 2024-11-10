class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None 
        self.next = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count 
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print(f"{data} inserted at begin.")
            
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print(f"{data} inserted at end.")
        
    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_begin(data)
        elif index == self.size():
            self.insert_at_end(data)
        elif 0 < index < self.size():
            current = self.head 
            position = 0
            while position+1 != index:
                current = current.next
                position += 1
            new_node = Node(data)
            
            new_node.next = current.next
            new_node.prev = current
            new_node.next.prev = new_node
            current.next = new_node
            print(f"{data} inserted at index {index}")
        else:
            print("Invalid Index")
            
    def delete_from_begin(self):
        if self.head is None:
            print("List is already empty.")
            
        elif self.head.next is None:
            self.head = self.tail = None 
            print("Deleted from begin.")
        else:
            self.head = self.head.next
            print("Deleted from begin.")
        
    def delete_from_end(self):
        if self.head is None:
            print("List is already empty.")
        elif self.head.next is None:
            self.head = self.tail = None
            print("Deleted from end.")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            print("Deleted from end.")
    
    def delete_from_index(self, index):
        if index == 0:
            self.delete_from_begin()
        elif index == self.size()-1:
            self.delete_from_end()
        elif 0 < index < self.size()-1:
            current = self.head
            position = 0
            while position+1 != index:
                current = current.next
                position += 1
            current.next = current.next.next
            current.next.prev = current 
            print(f"Deleted from index {index}")
        else:
            print("Invalid Index")
    
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            current = self.head
            while current:
                print(f"{current.data}-->",end="")
                current = current.next
            print("")
        
    
       
dll = DoublyLinkedList()

dll.insert_at_begin(10)
dll.insert_at_begin(20)
dll.insert_at_end(30)
dll.insert_at_index(50,3)
dll.insert_at_index(55,4)

dll.insert_at_end(80)
dll.insert_at_end(90)

print(dll.size())
dll.display()
dll.delete_from_index(6)
dll.insert_at_end(100)
# dll.delete_form_end()

dll.display()
