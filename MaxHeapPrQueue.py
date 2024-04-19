#Implementation of Max Heap priority queue using strings

class MaxHeapStringPriorityQueue:
    def __init__(self):
        self.heap = []

    def left_child(self, parent_index):
        left_child_index = 2 * parent_index + 1
        if left_child_index < len(self.heap) and left_child_index > 0:
            return left_child_index
        return None
    
    def right_child(self, parent_index):
        right_child_index = 2 * parent_index + 2
        if right_child_index < len(self.heap) and right_child_index > 1:
            return right_child_index
        return None
    
    def parent_node(self, child_index):
        if child_index > 0 and child_index < len(self.heap):
            return (child_index - 1) // 2
        return None
    
    def max_heapify(self, index, end_index):
        left_index = self.left_child(index)
        right_index = self.right_child(index)
        largest = index
        if left_index is not None and left_index <= end_index and self.heap[left_index] > self.heap[index]:
            largest = left_index
        if right_index is not None and right_index <= end_index and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest, end_index)

    def build_max_heap(self):
        n = len(self.heap)
        for index in range(n // 2 - 1, -1, -1):
            self.max_heapify(index, n - 1)

    def heap_sort(self):
        self.build_max_heap()
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.max_heapify(0, i - 1)  

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def extract_max(self):
        if  not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop()
        self.max_heapify(0, len(self.heap) - 1)
        return max_value

    def increase_key(self, index, new_value):
        if index < 0 or index >= len(self.heap) or new_value <= self.heap[index]:
            return
        self.heap[index] = new_value

        while index > 0:
            parent_index = self.parent_node(index)
            if parent_index is not None and self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parent_index = self.parent_node(index)
            if parent_index is not None and self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break



# max_heap = MaxHeapStringPriorityQueue()

# max_heap.insert("A")
# max_heap.insert("B")
# max_heap.insert("C")


# print("Max Heap after insertion:", max_heap.heap)

# max_heap.heap_sort()
# print("Max Heap after sorting:", max_heap.heap)

# maximum_element = max_heap.extract_max()
# print(f"Extracted maximum element: {maximum_element}")

# max_heap.increase_key(1, "D")

# print("Max Heap after increasing key:", max_heap.heap)
            
