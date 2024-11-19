class maxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, index):
        return (index-1)//2
    
    def left_child(self, index):
        return (2*index)+1
    
    def right_child(self, index):
        return (2*index)+2
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    def heapify_up(self, index):
        while index>0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)] 
            index = self.parent(index)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < len(self.heap) and self.heap[left] > self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] > self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)
        
    
    
mh = maxHeap()

print(mh.heap)
mh.insert(12)
mh.insert(13)
mh.insert(7)
mh.insert(10)
mh.insert(15)
mh.extract_max()
mh.extract_max()
mh.extract_max()
print(mh.heap)
        