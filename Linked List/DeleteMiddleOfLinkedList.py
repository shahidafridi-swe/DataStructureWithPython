class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
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
                position += 1
            
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node 
        else:
            print("Invalid Index")
            
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def update_by_index(self, data, index):
        if 0 <= index < self.length():
            current = self.head
            count = 0
            while count != index:
                count += 1
                current = current.next
            current.data = data
            print(f"{index} indexed Data Updated to {data} Successfully!")
        else:
            print("Invalid Index")

    def update_by_data_all(self, old_data, new_data):
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
            current = current.next
        print(f"All {old_data} Updated to {new_data} Successfully!")
    
    def update_by_data_first_one(self, old_data, new_data):
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                break
            current = current.next
        print(f"First {old_data} Updated to {new_data} Successfully!")

    def delete_first_node(self):
        if self.head is None:
            return None 
        temp = self.head
        self.head = self.head.next
        return temp.data
    
    def delete_last_node(self):
        if self.head is None:
            return None 
        if self.head.next is None:
            return self.delete_first_node()
        current = self.head
        while current.next.next is not None:
            current = current.next
        del_val = current
        current.next = None
        return del_val.data
    
    def delete_at_index(self, index):
        if index==0:
            self.delete_first_node()
        elif index == self.length():
            self.delete_last_node()
        elif 0 < index < self.length():
            position = 0
            current_node = self.head
                
            while position+1 != index:
                current_node = current_node.next
                position += 1
            
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node 
        else:
            print("Invalid Index")
     
    def get_middle(self):
        if self.head is None:
            return None
        current = self.head
        x = self.length() // 2
        while x:
            current = current.next
            x -= 1
        return current.data
    
    def delete_middle_of_linked_list(self):
        if self.head.next is None:
            self.head = None
            return
        middle = self.head
        last = self.head
        
        while last:
            if last.next.next:
                last = last.next.next
            else:
                last = last.next
            if last.next is None:
                break
            middle = middle.next
        middle.next = middle.next.next
    
       
    def print(self):
        current = self.head
        while current:
            print(f"{current.data} --> ",end="")
            current = current.next
        print("")
    


    
    


ll = SinglyLinkedList()
ll.insert_at_begin(25)
ll.insert_at_begin(15)
# ll.insert_at_begin(36)
# ll.insert_at_end(88)
# ll.insert_at_index(3,1)
# ll.insert_at_begin(25)
# ll.insert_at_index(111, 4)


ll.print()


print("Middle:", ll.get_middle())

ll.delete_middle_of_linked_list()

# print(ll.search(36))
print("Length:",ll.length())

ll.print()
            
            
            
        
        