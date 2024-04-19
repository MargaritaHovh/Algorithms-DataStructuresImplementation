#Implementation of HashSet for integers
class HashSet:
    def __init__(self, initial_capacity=16, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [None] * initial_capacity
        
    def insert(self, value):
        if self.load_factor_exceeded():
            self.rehash()
        index = self.hash_function(value)
        if self.buckets[index] is None:
            self.buckets[index] = []
        if value not in self.buckets[index]:
            self.buckets[index].append(value)
            self.size += 1

    def delete(self, value):
        index = self.hash_function(value)
        if self.buckets[index] is not None and value in self.buckets[index]:
            self.buckets[index].remove(value)
            self.size -= 1

    def search(self, value):
        index = self.hash_function(value)
        return self.buckets[index] is not None and value in self.buckets[index]

    def hash_function(self, value):
        hash_value = 0
        value_str = str(value)
        for char in value_str:
            hash_value = (hash_value * 31) + ord(char)
        return abs(hash_value) % self.capacity

    def rehash(self):
        new_capacity = self.next_prime(self.capacity * 2)
        new_buckets = [None] * new_capacity
        self.size = 0
        
        for bucket in self.buckets:
            if bucket:
                for value in bucket:
                    index = self.hash_function(value)
                    if new_buckets[index] is None:
                        new_buckets[index] = []
                    if value not in new_buckets[index]:
                        new_buckets[index].append(value)
                        self.size += 1

        self.capacity = new_capacity
        self.buckets = new_buckets

    def load_factor_exceeded(self):
        return self.size // self.capacity >= self.load_factor

    def next_prime(self, n):
        while not self.is_prime(n):
            n += 1
        return n

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

my_set = HashSet()

my_set.insert(5)
my_set.insert(10)
my_set.insert(15)
my_set.insert(5)

print("Size:", my_set.size)


print(my_set.search(10))  
print(my_set.search(20))  

my_set.delete(5)

print("Size:", my_set.size)

for value in my_set.buckets:
    if value is not None:
        for item in value:
            print(item)



