class HashTable:
    def __init__(self, tableSize):
        self._size = tableSize
        self._storage = [None] * tableSize
        self._count = 0

    def simple_hash(self, string):
        hash = 0
        for i, char in enumerate(string):
            hash += ord(char) * (i + 1)
        return hash % self._size

    def find(self, key):
        hash = self.simple_hash(key)
        if self._storage[hash] is None:
            self._storage[hash] = []
        bucket = self._storage[hash]
        match = None
        match_index = None
        for index, item in enumerate(bucket):
            if key in item:
                match = item
                match_index = index
                break
        return {'match': match, 'bucket': bucket, 'match_index': match_index}

    def resize(self, new_size):
        old_storage = self._storage
        self._size = new_size
        self._count = 0
        self._storage = [None] * new_size
        for bucket in old_storage:
            if bucket is not None:
                for item in bucket:
                    for key, value in item.items():
                        self.set(key, value)

    def set(self, key, value):
        result = self.find(key)
        match = result['match']
        bucket = result['bucket']
        if match:
            match[key] = value
        else:
            new_item = {key: value}
            self._count += 1
            bucket.append(new_item)
            if self._count > 0.75 * self._size:
                self.resize(2 * self._size)
        return self

    def get(self, key):
        match = self.find(key)['match']
        return match[key] if match else None

    def has(self, key):
        return self.find(key)['match'] is not None

    def delete(self, key):
        result = self.find(key)
        match = result['match']
        if match:
            bucket = result['bucket']
            match_index = result['match_index']
            del bucket[match_index]
            self._count -= 1
            if self._count < 0.25 * self._size:
                self.resize(int(0.5 * self._size))
            return True
        return False

    def count(self):
        return self._count

    def for_each(self, callback):
        for bucket in self._storage:
            if bucket is not None:
                for item in bucket:
                    callback(item)


# Test 1: Set and Get
ht = HashTable(10)
ht.set('key1', 'value1')
print(ht.get('key1'), '== value1')  # Expected: value1

# Test 2: Has
print(ht.has('key1'), '== True')  # Expected: True
print(ht.has('nonexistent'), '== False')  # Expected: False

# Test 3: Delete and Count
ht.set('key2', 'value2')
print(ht.delete('key1'), '== True')  # Expected: True (key1 is deleted)
print(ht.delete('nonexistent'), '== False')  # Expected: False (key does not exist)
print(ht.count(), '== 1')  # Expected: 1 (only key2 remains)

# Note: Use == for equality checks in the print statements for clarity in test output.

