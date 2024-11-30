class Heap:
    def __init__(self):
        self.heap = []
    
    def is_empty(self):
        return len(self.heap)==0
    
    def size(self):
        return len(self.heap)
    
    def peek(self):
        if self.is_empty():
            return None 
        return self.heap[0]
    
    def push(self, value):
        self.heap.append(value)
        self._heapify_up(self.size()-1)
    
    def pop(self):
        if self.is_empty():
            return None
        self._swap_data(0,len(self.heap)-1)
        data = self.heap.pop()
        self._heapify_down(0)
        return data
    
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            self._swap_data(parent,index)
            self._heapify_up(parent)
        # while index > 0 and self.heap[parent] > self.heap[index]:
        #     self._swap(parent,index)
        #     parent = index
    
    def _heapify_down(self, index):
        largest = index
        left = index*2 +1
        right = index*2 + 2
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
            
        if largest != index:
            self._swap_data(index, largest)
            self._heapify_down(largest)
        
    def _swap_data(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
    
class PriorityQueue:
    def __init__(self):
        self.heap = Heap()
    
    def push(self, value):
        self.heap.push(value)
        
    def pop(self):
        return self.heap.pop()
    
    def peek(self):
        return self.heap.peek()
        
    def is_empty(self):
        return self.heap.is_empty()
    
    def size(self):
        return self.heap.size()


pq = PriorityQueue()

# print(pq.peek())
pq.push(3)
pq.push(10)
pq.push(200)
pq.pop()
pq.pop()
print(pq.peek())
print(pq.heap.heap)