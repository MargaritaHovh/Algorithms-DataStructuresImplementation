#Implementation of HashMap for strings.
class HashMap:
    def __init__(self, initial_capacity=16, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [None] * initial_capacity

    def insert(self, key, value):
        if self.load_factor_exceeded():
            self.rehash()
        index = self.hash_function(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])
        self.size += 1

    def delete(self, key):
        index = self.hash_function(key)
        if self.buckets[index] is not None:
            for pair in self.buckets[index]:
                if pair[0] == key:
                    self.buckets[index].remove(pair)
                    self.size -= 1
                    return

    def search(self, key):
        index = self.hash_function(key)
        if self.buckets[index] is not None:
            for pair in self.buckets[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def hash_function(self, key):
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return abs(hash_value) % self.capacity

    def rehash(self):
        new_capacity = self.next_prime(self.capacity * 2)
        new_buckets = [None] * new_capacity

        for bucket in self.buckets:
            if bucket:
                for pair in bucket:
                    index = self.hash_function(pair[0])
                    if new_buckets[index] is None:
                        new_buckets[index] = []
                    new_buckets[index].append(pair)

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

my_map = HashMap()

my_map.insert("name", "Ana")
my_map.insert("age", 21)
my_map.insert("city", "New York")

print("Name:", my_map.search("name"))
print("Age:", my_map.search("age"))
print("City:", my_map.search("city"))

my_map.delete("age")

print("Size:", my_map.size)
