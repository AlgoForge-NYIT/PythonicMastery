### DOUBLY LINKED LIST ###


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

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
        newNext.prev = node
        newNext.next = oldNext
        if oldNext:
            oldNext.prev = newNext
        if self.tail == node:
            self.tail = newNext
        return newNext

    def removeAfter(self, node):
        removedNode = node.next
        if not removedNode:
            return 'Nothing to remove'
        newNext = removedNode.next
        node.next = newNext
        if newNext:
            newNext.prev = node
        removedNode.next = None
        removedNode.prev = None
        if removedNode == self.tail:
            self.tail = node
        return removedNode

    def insertHead(self, value):
        newHead = Node(value)
        oldHead = self.head
        self.head = newHead
        newHead.next = oldHead
        oldHead.prev = newHead
        return newHead

    def removeHead(self):
        if not self.head.next:
            return 'Nothing to remove'
        oldHead = self.head
        newHead = oldHead.next
        self.head = newHead
        newHead.prev = None
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
        newTail.prev = self.tail
        self.tail = newTail
        return newTail

    def insertBefore(self, node, value):
        if node == self.head:
            return self.insertHead(value)
        oldPrev = node.prev
        newPrev = Node(value)
        node.prev = newPrev
        newPrev.next = node
        newPrev.prev = oldPrev
        oldPrev.next = newPrev
        return newPrev

    def removeBefore(self, node):
        if node == self.head:
            return 'Nothing to remove'
        removedNode = node.prev
        if removedNode == self.head:
            self.head = node
            node.prev = None
            removedNode.next = None
            return removedNode
        newPrev = removedNode.prev
        if newPrev:
            newPrev.next = node
        node.prev = newPrev
        removedNode.next = None
        removedNode.prev = None
        return removedNode

# Test 1: Insertion
ll = LinkedList(1)
ll.appendToTail(3)
ll.insertHead(0)
ll.insertAfter(ll.head.next, 2)  # Insert between 1 and 3
print("Test 1 - Expected: 0, 1, 2, 3 - Actual:", ll.print())

# Test 2: Removal
ll.removeHead()
ll.removeAfter(ll.head)  # Remove 2
print("Test 2 - Expected: 1, 3 - Actual:", ll.print())

# Test 3: Traversal and Insertion
node = ll.findNode(1)
ll.insertBefore(node, 0)
ll.insertAfter(node, 2)
print("Test 3 - Expected: 0, 1, 2, 3 - Actual:", ll.print())
