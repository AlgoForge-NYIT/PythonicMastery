class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # Add value to storage array
        self.storage.append(value)

        def reheapify(index):
            # Calculate parent index
            parent_index = (index - 1) // 2
            # Base case: value <= parent or root reached
            if parent_index < 0 or self.storage[index] <= self.storage[parent_index]:
                return f'value added to index {index}'
            # Recursive case: swap with parent
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            return reheapify(parent_index)

        return reheapify(len(self.storage) - 1)

    def remove_max(self):
        if len(self.storage) == 0:
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()

        max_value = self.storage[0]
        self.storage[0] = self.storage.pop()

        def reheapify(index):
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            max_index = index

            if left_child < len(self.storage) and self.storage[left_child] > self.storage[max_index]:
                max_index = left_child
            if right_child < len(self.storage) and self.storage[right_child] > self.storage[max_index]:
                max_index = right_child
            if max_index != index:
                self.storage[index], self.storage[max_index] = self.storage[max_index], self.storage[index]
                reheapify(max_index)

        reheapify(0)
        return max_value

# Test 1: Insertion and removal of a single element
heap = Heap()
heap.insert(10)
print(heap.remove_max(), '== 10')  # Expected: 10

# Test 2: Insert multiple elements and remove max
heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(17)
heap.insert(10)
heap.insert(84)
heap.insert(19)
heap.insert(6)
heap.insert(22)
heap.insert(9)
print(heap.remove_max(), '== 84')  # Expected: 84 (the max value)

# Test 3: Continuous insertions and removals
heap = Heap()
values_to_insert = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for value in values_to_insert:
    heap.insert(value)
removed_values = [heap.remove_max() for _ in range(len(values_to_insert))]
print(removed_values, '== [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]')  # Expected: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (in descending order)
