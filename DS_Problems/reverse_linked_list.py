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

    def appendToTail(self, value):
        newTail = Node(value)
        if self.tail is not None:
            self.tail.next = newTail
        self.tail = newTail
        if self.head is None:  # If list was initially empty
            self.head = newTail
        return newTail

    def reverse(self):
        self.head = reverse_linked_list(self.head)
        # Update tail after reversal
        current = self.head
        while current and current.next:
            current = current.next
        self.tail = current

# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        raise ValueError('Must provide a non-empty list of values')
    linkedList = LinkedList(values[0])
    for value in values[1:]:
        linkedList.appendToTail(value)
    return linkedList

# Function to print the linked list
def print_list(linkedList):
    current = linkedList.head
    while current:
        print(current.value, end=' ')
        current = current.next
    print()  # For newline

# Rewritten reverse_linked_list method
def reverse_linked_list(head):
    if head is None:
        return None
    
    previous_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node

values = [1, 3, 5, 7, 9]
my_linked_list = create_linked_list(values)
print("Original list:")
print_list(my_linked_list)

### REVERSED LINKED LIST IN-PLACE ###
my_linked_list.reverse()  # Using the reverse method of LinkedList class
print("Reversed list:")
print_list(my_linked_list)
