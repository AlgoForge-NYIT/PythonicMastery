class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, headValue=None):
        if headValue is None:
            raise ValueError('Must provide value for first node')
        self.head = Node(headValue)
        self.tail = self.head

    def forEach(self, callback):
        node = self.head
        while node:
            callback(node.value)
            node = node.next

    def print(self):
        result = []
        self.forEach(lambda value: result.append(str(value)))
        return ', '.join(result)

    def insertAfter(self, node, value):
        oldNext = node.next
        newNext = Node(value)
        node.next = newNext
        newNext.next = oldNext
        if self.tail == node:
            self.tail = newNext
        return newNext

    def removeAfter(self, node):
        removedNode = node.next
        if not removedNode:
            return 'Nothing to remove'
        newNext = removedNode.next
        node.next = newNext
        removedNode.next = None
        if removedNode == self.tail:
            self.tail = node
        return removedNode

    def insertHead(self, value):
        newHead = Node(value)
        oldHead = self.head
        self.head = newHead
        newHead.next = oldHead
        return newHead

    def removeHead(self):
        if not self.head:
            return 'Nothing to remove'
        oldHead = self.head
        self.head = oldHead.next
        oldHead.next = None
        return oldHead

    def findNode(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return None

    def appendToTail(self, value):
        newTail = Node(value)
        self.tail.next = newTail
        self.tail = newTail
        return newTail


# Test 1: Insertion and Print
ll = LinkedList(1)
ll.appendToTail(2)
ll.insertHead(0)
ll.insertAfter(ll.head.next, 1.5)  # Inserting between 1 and 2
print("Test 1 - Expected: 0, 1, 1.5, 2 - Actual:", ll.print())

# Test 2: Removal
ll.removeHead()  # Removing head (0)
removedNode = ll.removeAfter(ll.head)  # Removing node after head (1.5)
print(f"Test 2 - Removed: {removedNode.value} - Expected: 1, 2 - Actual:", ll.print())

# Test 3: Find
foundNode = ll.findNode(2)
if foundNode:
    print("Test 3 - Found node with value:", foundNode.value)
else:
    print("Test 3 - Node not found")
