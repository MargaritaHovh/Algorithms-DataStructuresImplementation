class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity  

    def getSize(self):
        return self.size
    
    def getCapacity(self):
        return self.capacity
    
    def push_back(self, value):         
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        self.array[self.size] = value
        self.size += 1

    def insert(self, position, value, count = 1):  
        if position < 0 or position > self.size:
            raise IndexError("Invalid Position")
        
        if self.size + count > self.capacity:
            self.resize(max(self.capacity * 2, self.size + count))

        self.array[position + count: count + self.size] = self.array[position:self.size]

        for i in range(count):
            self.array[position + i] = value

        self.size += count

    def insertList(self, position, values):
        if position < 0 or position > self.size:
            raise IndexError('Invalid Position')
        
        values_count = len(values)

        if self.size + values_count > self.capacity:
            new_capacity = (max(self.capacity*2, self.size + values_count))
            self.resize(new_capacity)

        for i in range(self.size - 1, position - 1, -1):
            self.array[i + values_count] = self.array[i]

        for i in range(values_count):
            self.array[position + i] = values[i]

        self.size += values_count

    def pop_back(self):
        if self.size > 0:
            self.size -=1
            value = self.array[self.size]
            self.array[self.size] = None
            return value
        
        else:
            raise IndexError("Array is empty")
        
    def remove(self, position, count = 1):      
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        
        for i in range(position, self.size - count):
            self.array[i] = self.array[i+count]

        for i in range(self.size - count, self.size):
            self.array[i] = None
        self.size -= count

    def shrinkToFit(self):
        self.array = self.array[:self.size]
        self.capacity = self.size
        
    def clear(self):
        for i in range(self.size):
            self.array[i] = None

        self.size = 0

    def empty(self):
        return self.size == 0

    def resize(self, new_capacity):
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity 

    def print(self):
        print("[", end = "")
        for i in range(self.size):
            print(self.array[i], end = "")
            if i != self.size - 1:
                print(", ", end = "")
        print("]")

# arr = DynamicArray()
# arr.push_back(51)
# arr.push_back(0)
# arr.push_back(8)
# arr.print()  # Expected output: [51, 0, 8]

# arr.insertList(1, [4,2])
# arr.print()  # Expected output: [51, 4, 2, 0, 8]

# arr.insert(1, 14, 2)
# arr.print()  # Expected output: [51, 14, 14, 4, 2, 0, 8]

# arr.pop_back()
# arr.print()   # Expected output: [51, 14, 14, 4, 2, 0]

# arr.remove(1, 2)
# arr.print()  # Expected output: [51, 4, 2, 0]

# print("Size:", arr.getSize())  # Expected output: Size: 4
# print("Capacity:", arr.getCapacity())  # Expected output: Capacity: 8

# arr.shrinkToFit()
# print("Capacity after shrinking:", arr.getCapacity())  # Expected output: Capacity after shrinking: 4

# arr.clear()
# print("Is array empty:", arr.empty())  # Expected output: Is array empty: True

# arr.push_back(5)
# arr.print()  # Expected output: [5]


