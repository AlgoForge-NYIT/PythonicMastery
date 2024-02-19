class Stack:
    def __init__(self, capacity=float('inf')):
        self._capacity = capacity
        self._storage = {}
        self._count = 0

    def push(self, value):
        if self._count < self._capacity:
            self._storage[self._count] = value
            self._count += 1
            return self._count
        return 'Max capacity already reached. Remove element before adding a new one.'

    def pop(self):
        if self._count == 0:
            return 'No element inside the stack. Add element before popping.'
        self._count -= 1
        value = self._storage.pop(self._count)
        return value

    def peek(self):
        if self._count > 0:
            return self._storage[self._count - 1]
        return 'Stack is empty'

    def count(self):
        return self._count


# Test 1: Push and count
my_stack = Stack(3)
print(my_stack.push('a'), '== 1')
print(my_stack.push('b'), '== 2')
print(my_stack.count(), '== 2')

# Test 2: Max capacity and pop
print(my_stack.push('c'), '== 3')
print(my_stack.push('d'), '== Max capacity already reached. Remove element before adding a new one.')
print(my_stack.pop(), '== c')
print(my_stack.count(), '== 2')

# Test 3: Peek and empty pop
print(my_stack.peek(), '== b')
print(my_stack.pop(), '== b')
print(my_stack.pop(), '== a')
print(my_stack.pop(), '== No element inside the stack. Add element before popping.')

