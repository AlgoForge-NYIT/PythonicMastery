class Queue:
    def __init__(self, capacity=float('inf')):
        self._capacity = capacity
        self._storage = {}
        self._head = 0
        self._tail = 0

    def enqueue(self, value):
        if self.count() < self._capacity:
            self._storage[self._tail] = value
            self._tail += 1
            return self.count()
        return 'Max capacity already reached. Remove element before adding a new one.'

    def dequeue(self):
        if self._head < self._tail:
            element = self._storage.pop(self._head)
            self._head += 1
            return element
        return None

    def peek(self):
        return self._storage.get(self._head)

    def count(self):
        return self._tail - self._head

    def contains(self, value):
        for i in range(self._head, self._tail):
            if self._storage[i] == value:
                return True
        return False

    def until(self, value):
        for i in range(self._head, self._tail):
            if self._storage[i] == value:
                return i - self._head + 1
        return None



# Test 1: Enqueue and Dequeue
q = Queue(3)
assert q.enqueue(1) == 1, "Enqueue failed"
assert q.enqueue(2) == 2, "Enqueue failed"
assert q.dequeue() == 1, "Dequeue failed"
assert q.count() == 1, "Count failed"

# Test 2: Peek and Contains
assert q.peek() == 2, "Peek failed"
assert q.contains(2) == True, "Contains failed"
assert q.contains(1) == False, "Contains failed"

# Test 3: Until
q.enqueue(3)
assert q.until(3) == 2, "Until failed"
assert q.until(4) == None, "Until failed"
