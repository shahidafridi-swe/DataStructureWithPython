def heapify(arr, n, index):
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right 
    
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, n, largest)
    
def heapSort(arr):
    n = len(arr)
    
    # convert the arr to maxheap arr
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    
    # Sorting 
    for i in range(n-1, 0 ,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
arr = [4,24,24,2,5,34,54,32,1,6,7]
print(arr)
heapSort(arr)
print(arr)
    
    
        