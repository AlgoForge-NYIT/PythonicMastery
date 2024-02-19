class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
class BST:
    def __init__(self, root):
        if root is not None:
            self.root = Node(root)
        else:
            self.root = None

    def insert(self, key):
        self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.val:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)
                