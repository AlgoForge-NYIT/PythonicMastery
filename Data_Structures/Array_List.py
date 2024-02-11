class ArrayList:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def push(self, value):
        self.data[self.length] = value
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        ans = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return ans
    
    def get(self, index):
        return self.data.get(index, None)
    
    def delete(self, index):
        if index >= self.length or index < 0:
            return None
        ans = self.data[index]
        self._collapse_to(index)
        return ans
    
    def _collapse_to(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1

    def serialize(self):
        return [self.data[i] for i in range(self.length)]

### Test 1 ###
list1 = ArrayList()
list1.push(1)
list1.push(2)
list1.push(3)
print("Test 1 - Push: Expected [1, 2, 3], got", list1.serialize())

popped = list1.pop()
print("Test 1 - Pop: Expected 3, got", popped)
print("After Pop: Expected [1, 2], got", list1.serialize())

### Test 2 ###
list2 = ArrayList()
for i in range(5):
    list2.push(i+1)  # Adds 1, 2, 3, 4, 5
print("Test 2 - Before Delete: Expected [1, 2, 3, 4, 5], got", list2.serialize())

deleted = list2.delete(2)  # Deletes '3'
print("Test 2 - Delete: Expected 3, got", deleted)
print("After Delete: Expected [1, 2, 4, 5], got", list2.serialize())

### Test 3 ###
list3 = ArrayList()
list3.push('a')
deleted = list3.delete(5)  # Non-existent index
print("Test 3 - Delete Non-existent Index: Expected None, got", deleted)

list3.pop()  # This should empty the list
popped = list3.pop()  # Attempt to pop again from an empty list
print("Test 3 - Pop from Empty List: Expected None, got", popped)
